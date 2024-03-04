import flet as ft

def main(page: ft.page) -> None:

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    c1 = ft.Container(
        width=300,
        height=300,
        bgcolor='red'
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
        ft.Row(
            controls=[c1, c2, c3]
        )
    )
    page.update()
if __name__=='__main__':
    ft.app(target=main)