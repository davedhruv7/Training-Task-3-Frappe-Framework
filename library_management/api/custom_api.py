import frappe

@frappe.whitelist(allow_guest=True)  # allow_guest=True lets non-logged-in users access this API
def hello_world(name=None):
    """A simple API that returns a greeting."""
    if name:
        return {"message": f"Hello, {name}!"}
    else:
        return {"message": "Hello, World!"}
