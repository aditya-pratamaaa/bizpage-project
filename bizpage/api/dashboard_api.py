import frappe


@frappe.whitelist()
def mark_notification_read(name):
    notif = frappe.get_doc("Notification Log", name)

    if notif.for_user != frappe.session.user:
        frappe.throw("Anda tidak punya izin mengubah notifikasi ini.", frappe.PermissionError)

    notif.db_set("read", 1)
    return {"success": True}


@frappe.whitelist()
def mark_all_notifications_read():
    frappe.db.set_value(
        "Notification Log",
        {"for_user": frappe.session.user, "read": 0},
        "read",
        1,
    )
    return {"success": True}

@frappe.whitelist()
def get_owner_profile():
	owner = frappe.db.get_value(
		"Owner",
		{"user": frappe.session.user},
		["name", "owner_name", "gender", "phone_number", "birthday"],
		as_dict=True,
	)

	if not owner:
		return {
			"exists": False,
			"owner_name": "",
			"gender": "",
			"phone_number": "",
			"birthday": "",
		}

	owner["exists"] = True
	return owner


@frappe.whitelist()
def save_owner_profile(owner_name=None, gender=None, phone_number=None, birthday=None):
	existing_name = frappe.db.get_value("Owner", {"user": frappe.session.user}, "name")

	if existing_name:
		doc = frappe.get_doc("Owner", existing_name)
	else:
		doc = frappe.new_doc("Owner")
		doc.user = frappe.session.user

	doc.owner_name = owner_name
	doc.gender = gender
	doc.phone_number = phone_number
	doc.birthday = birthday
	doc.save(ignore_permissions=True)

	return {"success": True, "name": doc.name}


@frappe.whitelist()
def update_avatar(file_url):
	frappe.db.set_value("User", frappe.session.user, "user_image", file_url)
	return {"success": True}
