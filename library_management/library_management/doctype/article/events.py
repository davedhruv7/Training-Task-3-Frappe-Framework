import frappe

def send_sms(doc, event):
    print(f"\n\n\n {doc}, {event} \n\n\n")
    frappe.throw('Function reached')


def validate(self):
    if self.age <= 18:
        frappe.throw("Person's age must be at least 18")
