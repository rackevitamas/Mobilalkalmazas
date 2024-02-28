import flet as ft
def main(page: ft.Page) -> None:
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    c1 = ft.Container(
        content=ft.Text(value="Sose bízd emberre egy komputer munkáját."),
        height=300,
        # width=600,
        bgcolor=ft.colors.DEEP_PURPLE,
        alignment=ft.alignment.center,
        margin= -10
    )
    page.add(c1)
    page.update()
if __name__=='__main__':
    ft.app(target=main)