// Copyright (c) 2025, Dhruv and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client Side Scripting", {
 	// refresh(frm) {
    //     // frappe.msgprint("Refresh")
    //     frappe.throw("Refresh")
 	// },

   //  onload(frm) {
   //      // frappe.msgprint("Refresh")
   //      frappe.throw("Onload")
 	// },

   after_save(frm){
      frappe.msgprint(__("The Full Name is {}",
         [frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name]
      ))


      for(let row of frm.doc.family_members)
      {
         frappe.msgprint(__("{}. The family members area 1 is {} & located in {}", [row.idx, row.area_1, row.area_3]))
      }
   },

   // refresh(frm){
   //    frm.set_intro('Now you can create a new DocType')


   //    if(frm.is_new()){
   //       frm.set_intro('Hare Krishna')
   //    }
   // }

   // validate(frm){
   //    // frm.set_value('email', frm.doc.first_name + " " + frm.doc.middle_name+ " " + frm.doc.last_name)


   //    let row = frm.add_child('family_members',
   //       {
   //          area_1:'Paldi',
   //          area_2:'Vikas Rd',
   //          area_3:'Ahmedabad'
   //       }
   //    )
   // }

      // enanle(frm){
      //    // frm.set_df_property('first_name', 'reqd', 1)

      //    // frm.set_df_property('middle_name', 'read_only', 1)

      //    // frm.toggle_reqd('age',true)
      // }
   
      // refresh(frm){
      //    frm.add_custom_button('Click Me Button',() => {
      //       frappe.msgprint(__('You Clicked Me!!'));
      //    })

      //    frm.add_custom_button('Click Me1', () => 
      //    {
      //       frappe.msgprint(__('You clicked 1!!'))
      //    }, 'click_me')

      //    frm.add_custom_button('Click Me 2', () => {
      //       frappe.msgprint(__('You Clicked 2!!'))
      //    }, 'click_me')
      // }

 });
