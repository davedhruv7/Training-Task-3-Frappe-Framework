frappe.pages['my-page'].on_page_load = function(wrapper) {
    // Create the page layout with a title and a single-column layout
    let page = frappe.ui.make_app_page({
        parent: wrapper,       // 'wrapper' is passed by Frappe and represents the page container.
        title: 'My Page',
        single_column: true    // Set to true to hide the sidebar.
    });

    // Add custom HTML content to the page body
    $(page.body).append(`
        <div style="margin: 20px;">
            <h3>Welcome to My Custom Page!</h3>
            <p>This is an example of a custom page created using Frappe's Page API.</p>
        </div>
    `);

    // Optionally, add a primary button with a click handler
    page.set_primary_action('Click Me', () => {
        frappe.msgprint('Primary Action Button clicked!');
    });
};
