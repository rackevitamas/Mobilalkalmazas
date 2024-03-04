import flet as ft


def main(page: ft.Page) -> None:

    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.title="Two Containers"

    c1 = ft.Container(
        width=200,
        height=200,
        bgcolor='red',
        
    )

    c2 = ft.Container(
        width=200,
        height=200,
        bgcolor='blue'
    )

    page.add(
        ft.Row(
            controls=[c1, c2],
            spacing= 100,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.update()


if __name__=='__main__':
    ft.app(target=main)
