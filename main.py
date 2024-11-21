import flet as ft

def main(page: ft.Page):
    # Add this at the beginning of main function
    global click_counter
    click_counter = 0
    
    page.title = "Tip Calculator"
    page.theme = ft.Theme(color_scheme_seed="deeppurple")
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER    
    tip_percent_field = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    
    def theme_changed(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        theme_icon.icon = "dark_mode" if page.theme_mode == ft.ThemeMode.LIGHT else "light_mode"
        page.update()

    theme_icon = ft.IconButton(
        icon="light_mode",
        tooltip="Toggle light/dark theme",
        on_click=theme_changed,
    )    

    click_counter = 0

    def trigger_easter_egg(e):
        
        wv = ft.TextButton(text="Click me!", 
                    url="https://r.mtdv.me/watch?v=5RguAO3MO4",
                    tooltip="You know you want to...")
        
        page.add(wv)
        page.update()

    def clear(e):
        global click_counter
        click_counter += 1
        
        tip_percent_field.value = "0"
        bill_field.value = ""
        total_amount_field.value = ""
        tip_amount_field.value = ""
        
        if click_counter >= 5:
            trigger_easter_egg(e)
            click_counter = 0
        
        page.update()
    def minus_click(e):
        current_value = int(tip_percent_field.value)
        if current_value > 0:  # Prevent negative tips
            tip_percent_field.value = str(current_value - 1)
            update_total_amount(e)
        page.update()
        
    def plus_click(e):
        current_value = int(tip_percent_field.value)
        tip_percent_field.value = str(current_value + 1)
        update_total_amount(e)
        page.update()

    def update_bill_amount(e):
        update_total_amount(e)
        
    def update_total_amount(e):
        try:
            bill_amount = float(bill_field.value or 0)
            tip_percent = float(tip_percent_field.value or 0)
            tip_amount = bill_amount * (tip_percent / 100)
            total = bill_amount + tip_amount
            
            tip_amount_field.value = f"{tip_amount:.2f}"
            total_amount_field.value = f"{total:.2f}"
            page.update()
        except ValueError:
            pass

    bill_field = ft.TextField(
        label="Enter Bill Amount ex: $100.00",
        icon=ft.icons.ATTACH_MONEY,
        border=ft.InputBorder.UNDERLINE,
        on_change=update_bill_amount
    )
    
    tip_amount_field = ft.TextField(
        value="0.00",
        icon=ft.icons.ATTACH_MONEY,
        border=ft.InputBorder.UNDERLINE,
        read_only=True
    )
    
    total_amount_field = ft.TextField(
        value="0.00",
        icon=ft.icons.ATTACH_MONEY,
        border=ft.InputBorder.UNDERLINE,
        read_only=True
    )

    page.add(
        ft.Container(
            content=ft.Column(
                [        
                    ft.Container(
                        content=ft.Column(
                            [ft.Row([ft.Text("Bill Amount", size=30, weight=ft.FontWeight.BOLD,),], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([bill_field], alignment=ft.MainAxisAlignment.CENTER),]                        
                        ),   
                        bgcolor=ft.colors.INVERSE_PRIMARY,
                        padding=20,
                        border_radius=10,                        
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Row(
                                [
                                    ft.Text("Tip % ", size=25, weight=ft.FontWeight.BOLD),
                                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                                    tip_percent_field,
                                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),]
                        ),
                        bgcolor=ft.colors.INVERSE_PRIMARY,
                        padding=20,
                        border_radius=10,                        
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Row([ft.Text("Tip Amount",size=25, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([tip_amount_field], alignment=ft.MainAxisAlignment.CENTER),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        bgcolor=ft.colors.INVERSE_PRIMARY,
                        padding=20,
                        border_radius=10,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Row([ft.Text("Total Bill Amount",size=25, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([total_amount_field], alignment=ft.MainAxisAlignment.CENTER),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        bgcolor=ft.colors.INVERSE_PRIMARY,
                        padding=20,
                        border_radius=10,
                    ),


                    ft.Row([ft.ElevatedButton(text="Generate New",on_click=clear)], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([theme_icon], alignment=ft.MainAxisAlignment.END),        
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=ft.colors.PRIMARY_CONTAINER,
            padding=20,
            border_radius=10,
            width=400,
            alignment=ft.alignment.center
        )        
    )

ft.app(main)