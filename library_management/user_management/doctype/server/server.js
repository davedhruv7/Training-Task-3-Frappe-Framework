// Copyright (c) 2025, Dhruv and contributors
// For license information, please see license.txt

frappe.ui.form.on("Server", {
	enable(frm) {
        frappe.call({
            method: "apps.library_management.library_management.user_management.doctype.client_side_scripting.client_side_scripting.frappe_call",
            args:{
                msg: "Hello"
            },
            frappe: true,
            freeze_message: __('Calling frappe_call Method'),
            callback: function(r) {
                frappe.msgprint(r.method)
            }
        })
	},
});
