// Copyright (c) 2025, Dhruv and contributors
// For license information, please see license.txt

frappe.query_reports["Server Side Scripting Script Report"] = {
	"filters": [
		{
			"fieldname":"first_name",
			"label": __("First Name"),
			"fieldtype": "Data"
		},
		{
			"fieldname":"last_name",
			"label": __("Last Name"),
			"fieldtype": "Data"
		},
		{
			"fieldname":"dob",
			"label": __("DOB"),
			"fieldtype": "Data"
		},
		{
			"fieldname":"email",
			"label": __("Email"),
			"fieldtype":"Data"
		},
		{
			"fieldname":"age",
			"label": __("Age"),
			"fieldtype":"Data"
		}

	]
};
