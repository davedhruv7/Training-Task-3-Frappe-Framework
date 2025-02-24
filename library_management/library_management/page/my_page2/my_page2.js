frappe.pages['my-page2'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Page ',
		single_column: true,
		
	});
	page.set_title('My Page')
	page.set_title_sub('Subtitle')
	page.set_indicator('Pending', 'orange')
	// let $btn = page.set_primary_action('New', () => create_new(), 'octicon octicon-plus')
	page.clear_primary_action()
	let $btn = page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync')
	page.add_menu_item('Send Email', () => open_email_dialog())
	page.add_menu_item('Send Email', () => open_email_dialog(), true)
	page.clear_menu()
	page.add_action_item('Delete', () => delete_items())
	page.add_inner_button('Update Posts', () => update_posts())

	page.change_inner_button_type('Update Posts', null, 'primary');
	page.change_inner_button_type('Delete Posts', 'Actions', 'danger');
	page.remove_inner_button('Update Posts')

	page.remove_inner_button('New Posts', 'Make')
	page.clear_inner_toolbar()

	let field = page.add_field({
		label: 'Status',
		fieldtype: 'Select',
		fieldname: 'status',
		options: [
			'Open',
			'Closed',
			'Cancelled'
		],
		change() {
			console.log(field.get_value());
		}
	});











}


