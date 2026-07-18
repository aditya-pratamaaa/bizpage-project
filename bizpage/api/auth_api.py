import frappe
from frappe import _
from frappe.utils import random_string, get_url, now_datetime, add_to_date

@frappe.whitelist(allow_guest=True)
def custom_sign_up(email, full_name, password):
	email = email.strip().lower()

	if frappe.db.exists("User", email):
		frappe.throw(_("Email sudah terdaftar"))

	user = frappe.get_doc({
		"doctype": "User",
		"email": email,
		"first_name": full_name,
		"enabled": 0,
		"user_type": "Website User",
		"send_welcome_email": 0,
	})
	user.insert(ignore_permissions=True)

	user.new_password = password
	user.save(ignore_permissions=True)

	_create_and_send_token(email)

	frappe.db.commit()
	return {"message": "Registrasi berhasil, silakan cek email untuk verifikasi akun."}


def _create_and_send_token(email):

	old_tokens = frappe.get_all(
		"Email Verification Token",
		filters={"user": email, "is_used": 0},
	)
	for t in old_tokens:
		frappe.delete_doc("Email Verification Token", t.name, ignore_permissions=True)

	token = random_string(32)
	expires_at = add_to_date(now_datetime(), hours=24)

	frappe.get_doc({
		"doctype": "Email Verification Token",
		"user": email,
		"token": token,
		"expires_at": expires_at,
		"is_used": 0,
	}).insert(ignore_permissions=True)

	verify_url = get_url(
		f"/api/method/bizpage.api.auth_api.verify_email?token={token}&email={email}"
	)

	frappe.sendmail(
		recipients=email,
		subject="Verifikasi Akun Kamu",
		message=f"""
			Halo,<br><br>
			Klik link berikut untuk verifikasi akun kamu (berlaku 24 jam):<br>
			<a href="{verify_url}">{verify_url}</a><br><br>
			Kalau kamu tidak merasa mendaftar, abaikan email ini.
		""",
	)

@frappe.whitelist(allow_guest=True)
def verify_email(token, email):
	email = email.strip().lower()

	token_doc = frappe.get_all(
		"Email Verification Token",
		filters={"user": email, "token": token, "is_used": 0},
		fields=["name", "expires_at"],
		limit=1,
	)

	if not token_doc:
		frappe.local.response["type"] = "redirect"
		frappe.local.response["location"] = "/bizpage/login?verify=invalid"
		return

	token_doc = token_doc[0]

	if now_datetime() > token_doc.expires_at:
		frappe.local.response["type"] = "redirect"
		frappe.local.response["location"] = "/bizpage/login?verify=expired"
		return

	frappe.db.set_value("Email Verification Token", token_doc.name, "is_used", 1)

	frappe.db.set_value("User", email, "enabled", 1)
	frappe.db.commit()

	frappe.local.response["type"] = "redirect"
	frappe.local.response["location"] = "/bizpage/login?verify=success"

@frappe.whitelist(allow_guest=True)
def resend_verification(email):
	email = email.strip().lower()

	if not frappe.db.exists("User", email):
		frappe.throw(_("Email tidak ditemukan"))

	if frappe.db.get_value("User", email, "enabled"):
		frappe.throw(_("Akun ini sudah terverifikasi, silakan login."))

	_create_and_send_token(email)
	frappe.db.commit()

	return {"message": "Email verifikasi baru sudah dikirim."}
