import flet as ft

def main(page: ft.Page):
    page.title = "Tip Calculator"
    page.theme = ft.Theme(color_scheme_seed="green")
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.Text("Bill Amount"),                                
            ],
            
            alignment=ft.MainAxisAlignment.CENTER,
        ),        
        ft.Row(
            [
                ft.TextField(label="Enter Bill Amount ex: $100.00", icon=ft.icons.ATTACH_MONEY,border=ft.InputBorder.UNDERLINE),
            ],
            
            alignment=ft.MainAxisAlignment.CENTER,
        ),         
        ft.Row(
            [
                ft.Text("Tip % "),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                ft.TextField(value="10", text_align=ft.TextAlign.RIGHT, width=100),
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.Text("Tip Amount"),                                
            ],
            
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.TextField(value= "$10", icon=ft.icons.ATTACH_MONEY,border=ft.InputBorder.UNDERLINE),                                
            ],
            
            alignment=ft.MainAxisAlignment.CENTER,
        ),        
        ft.Row(
            [
                ft.Text("Total Bill Amount"),                                
            ],
            
            alignment=ft.MainAxisAlignment.CENTER,
        ),                    
        ft.Row(
            [
                ft.TextField(value= "$110", icon=ft.icons.ATTACH_MONEY,border=ft.InputBorder.UNDERLINE),                                

            ],
            
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.ElevatedButton(text="Generate New"),                                               
            ],
            
            alignment=ft.MainAxisAlignment.CENTER,
        ),                                 
    )

ft.app(main)

