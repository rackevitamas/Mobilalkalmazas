from tkinter.tix import COLUMN
import flet as ft

def main(page: ft.page) -> None:

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Three Containers"

    text = ft.Text(
        value="3 containers",
        theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
        text_align=ft.TextAlign.RIGHT,
        color='white'
    )
    
    icon = ft.Icon(name=ft.icons.HOME_OUTLINED, size=48, color='white') 

    c1 = ft.Container(
        width=300,
        height=300,
        bgcolor='red',
        content=COLUMN([
            icon
        ])
    )
    
    c2 = ft.Container(
        width=300,
        height=300,
        bgcolor='blue'
    )

    c3 = ft.Container(
        width=300,
        height=300,
        bgcolor='black'
    )

    page.add(
        text,
        ft.Row(
            controls=[c1, c2, c3],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.update()

if __name__ == '__main__':
    ft.app(target=main)
