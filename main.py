import flet as ft

def main(page: ft.Page):
    page.title = "Tip Calculator"
    page.theme = ft.Theme(color_scheme_seed="green")
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    tip_percent_field = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    
    def clear(e):
        tip_percent_field.value = "0"
        bill_field.value = ""
        total_amount_field.value = ""
        tip_amount_field.value = ""
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
        ft.Row([ft.Text("Bill Amount")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([bill_field], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [
                ft.Text("Tip % "),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                tip_percent_field,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row([ft.Text("Tip Amount")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([tip_amount_field], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.Text("Total Bill Amount")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([total_amount_field], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text="Generate New",on_click=clear)], alignment=ft.MainAxisAlignment.CENTER),
        
    )

ft.app(main)