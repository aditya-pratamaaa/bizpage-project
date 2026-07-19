app_name = "bizpage"
app_title = "Bizpage"
app_publisher = "Bizpage"
app_description = "Bizpage"
app_email = "bizpage@gmail.com"
app_license = "mit"

# bizpage/permissions.py
#
# Fungsi ini didaftarkan di hooks.py, bikin Frappe OTOMATIS nambahin
# filter "WHERE business = <business milik user ini>" ke SETIAP query
# get_list/report_view untuk Product, Portfolio, Custom Request dll.
# Jadi walaupun frontend nakal ngirim business_id lain, backend tetap
# cuma ngasih data yang emang milik user itu.

import frappe


def get_business_for_user(user):
	"""Ambil business_id milik user yang login. Sesuaikan field/doctype-nya."""
	return frappe.db.get_value("Business", {"owner": user}, "name")


def product_query_conditions(user):
	if not user:
		user = frappe.session.user

	# Admin boleh lihat semua produk semua bisnis
	if "Admin" in frappe.get_roles(user):
		return ""

	business = get_business_for_user(user)
	if not business:
		# User login tapi belum punya business -> jangan tampilkan apa-apa
		return "1=0"

	return f"`tabProduct`.`business` = {frappe.db.escape(business)}"


def portfolio_query_conditions(user):
	if not user:
		user = frappe.session.user

	if "Admin" in frappe.get_roles(user):
		return ""

	business = get_business_for_user(user)
	if not business:
		return "1=0"

	return f"`tabPortfolio`.`business` = {frappe.db.escape(business)}"


# Contoh has_permission tambahan (buat cek pas akses 1 dokumen spesifik,
# bukan cuma list) -> mencegah orang akses /api/resource/Product/xxx
# punya bisnis lain langsung lewat ID.
def product_has_permission(doc, ptype, user):
	if "Admin" in frappe.get_roles(user):
		return True

	business = get_business_for_user(user)
	return doc.business == business

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "bizpage",
# 		"logo": "/assets/bizpage/logo.png",
# 		"title": "Bizpage",
# 		"route": "/bizpage",
# 		"has_permission": "bizpage.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bizpage/css/bizpage.css"
# app_include_js = "/assets/bizpage/js/bizpage.js"

# include js, css files in header of web template
# web_include_css = "/assets/bizpage/css/bizpage.css"
# web_include_js = "/assets/bizpage/js/bizpage.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bizpage/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "bizpage/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "bizpage.utils.jinja_methods",
# 	"filters": "bizpage.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bizpage.install.before_install"
# after_install = "bizpage.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bizpage.uninstall.before_uninstall"
# after_uninstall = "bizpage.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "bizpage.utils.before_app_install"
# after_app_install = "bizpage.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "bizpage.utils.before_app_uninstall"
# after_app_uninstall = "bizpage.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bizpage.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bizpage.tasks.all"
# 	],
# 	"daily": [
# 		"bizpage.tasks.daily"
# 	],
# 	"hourly": [
# 		"bizpage.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bizpage.tasks.weekly"
# 	],
# 	"monthly": [
# 		"bizpage.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "bizpage.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bizpage.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bizpage.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["bizpage.utils.before_request"]
# after_request = ["bizpage.utils.after_request"]

# Job Events
# ----------
# before_job = ["bizpage.utils.before_job"]
# after_job = ["bizpage.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"bizpage.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

