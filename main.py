import dearpygui.dearpygui as dpg

def button_click(sender, app_data, user_data):
    # This function will be called when a button is clicked
    print(f"Button {user_data} clicked")

dpg.create_context()
dpg.create_viewport(title='Calculator', width=600, height=300)
dpg.setup_dearpygui()

with dpg.handler_registry():
    with dpg.window(label="Calculator"):
            with dpg.child(width=-1):
                for i in range(3):
                    with dpg.group(horizontal=True):
                        for j in range(3):
                            button_num = i * 3 + j + 1  # Calculate the number for this button
                            dpg.add_button(label=str(button_num), callback=button_click, user_data=button_num)
                with dpg.group(horizontal=True):
                    dpg.add_spacing()
                    dpg.add_spacing()
                    dpg.add_spacing()
                    dpg.add_button(label="0", callback=button_click, user_data=0)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()