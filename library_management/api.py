import frappe
from frappe import _

@frappe.whitelist()  # Makes it callable via API
def get_server_names_api():
    """
    API endpoint to fetch server names.
    Accessible via: /api/method/library_management.api.get_server_names_api
    """
    return {"server_names": frappe.db.get_list("Server", pluck="name")}
