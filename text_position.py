import flet as ft
def main(page: ft.Page) -> None:
    page.title = "Igazítás"
    c1 = ft.Container(
        content=ft.Text("Első sor."),
        alignment=ft.alignment.right,
    )
    c2 = ft.Container(
        content=ft.Text("Második sor."),
        alignment=ft.alignment.center,

    )
    c3 = ft.Container(
        content=ft.Text("Harmadik sor."),
        alignment=ft.alignment.left,

    )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ft.Row([c1,c2,c3], alignment=ft.MainAxisAlignment.CENTER))
    page.update()
if __name__=='__main__':
    ft.app(target=main)