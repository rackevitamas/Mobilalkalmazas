import flet as ft

def main(page: ft.Page) -> None:
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    
    current_container = None
    image_src = None

    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            selected_files.value = e.files[0].name
            image_src.src = e.files[0].path
        else:
            selected_files.value = "Cancelled!"
            image_src.src = ""
        selected_files.update()
        image_src.update()

    def button_clicked(e):
        nonlocal current_container
        page.controls.clear()
        page.add(red_button, green_button, blue_button)
        
        if e.control.text == "Piros":
            current_container = red
        elif e.control.text == "Zöld":
            current_container = green
        elif e.control.text == "Kék":
            current_container = blue
        
        if current_container:
            page.add(
                ft.Row(
                    [
                        ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                        current_container,
                        ft.IconButton(ft.icons.ADD, on_click=plus_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        
        page.update()
    
    def minus_click(e):
        if current_container.opacity > 0:
            current_container.opacity -= 0.1
        page.update()
        
    def plus_click(e):
        if current_container.opacity < 1:
            current_container.opacity += 0.1
        page.update()
    
    
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    image_src = ft.Image()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
    red = ft.Container(
        bgcolor=ft.colors.RED,
        width=150,
        height=150,
        opacity=1
    )
    
    green = ft.Container(
        bgcolor=ft.colors.GREEN,
        width=150,
        height=150,
        opacity=1
    )
    
    blue = ft.Container(
        bgcolor=ft.colors.BLUE,
        width=150,
        height=150,
        opacity=1
    )
    
    red_button = ft.ElevatedButton(
        text="Piros",
        on_click=button_clicked
    )
    
    green_button = ft.ElevatedButton(
        text="Zöld",
        on_click=button_clicked
    )
    
    blue_button = ft.ElevatedButton(
        text="Kék",
        on_click=button_clicked
    )

    page.add(image_src)
    page.add(red_button, green_button, blue_button)
    
if __name__ == "__main__":
    ft.app(target=main)
