import frappe
from frappe import _

@frappe.whitelist()  # This decorator exposes the function as an API endpoint
def get_all_server_data():
    """
    API endpoint to fetch all columns of all records from the 'Server' doctype.
    Accessible via: /api/method/library_management.api.get_all_server_data
    """
    server_data = frappe.db.get_list("Server", fields=["*"])
    return {"server_data": server_data}

@frappe.whitelist() 
def get_all_server_name():
    server_name = frappe.db.get_list("Server", plunk="name")
    return {"server_name": server_name}