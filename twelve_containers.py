import flet as ft

def main(page: ft.Page) -> None:
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Twelve containers"
    page.auto_scroll

    spacing = 20

    container_size = 200

    container_row = ft.Row(
        controls=[
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20) 
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            ft.Container(
                width=container_size,
                height=container_size,
                bgcolor='orange',
                margin=(20, 20, 20, 20)
            ),
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=spacing,
        wrap=True
    )
    
    page.add(container_row)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)
