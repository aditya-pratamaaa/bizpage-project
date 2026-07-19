# bizpage/permissions.py
#
# Filter data (Product, Portfolio, dll) berdasarkan business milik user,
# dan cek "admin atau bukan" berdasarkan Role Profile user tersebut.

import frappe


def get_role_profile(user):
	return frappe.db.get_value("User", user, "role_profile_name")


def is_admin(user):
	return get_role_profile(user) == "Admin"


def get_business_for_user(user):
	"""Ambil business_id milik user yang login. Sesuaikan field/doctype-nya."""
	return frappe.db.get_value("Business", {"owner": user}, "name")


def product_query_conditions(user):
	if not user:
		user = frappe.session.user

	# Admin (Role Profile "Admin") boleh lihat semua produk semua bisnis
	if is_admin(user):
		return ""

	business = get_business_for_user(user)
	if not business:
		# User login tapi belum punya business -> jangan tampilkan apa-apa
		return "1=0"

	return f"`tabProduct`.`business` = {frappe.db.escape(business)}"


def portfolio_query_conditions(user):
	if not user:
		user = frappe.session.user

	if is_admin(user):
		return ""

	business = get_business_for_user(user)
	if not business:
		return "1=0"

	return f"`tabPortfolio`.`business` = {frappe.db.escape(business)}"


# Contoh has_permission tambahan (buat cek pas akses 1 dokumen spesifik,
# bukan cuma list) -> mencegah orang akses /api/resource/Product/xxx
# punya bisnis lain langsung lewat ID.
def product_has_permission(doc, ptype, user):
	if is_admin(user):
		return True

	business = get_business_for_user(user)
	return doc.business == business
