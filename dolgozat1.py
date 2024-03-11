import flet as ft
def main(page: ft.Page) -> None:
    page.title='Dolgozat'
    page.scroll = ft.ScrollMode.AUTO
    c1 = ft.Container(
        ft.Text(value='Hello'),
        alignment=ft.alignment.top_left
    )
    c2 = ft.Container(
        ft.Text(value='world'),
        alignment=ft.alignment.top_right
    )
    page.add(
        ft.Row(
            controls=[c1, c2],
            spacing=1175 #nem mükődik az igazítás
        )
    )
    betu = ft.Container(
        content=ft.Text(value='A'),
        bgcolor=ft.colors.BLUE_200,
        height=200,
        margin=-10,
        alignment=ft.alignment.center
    )
    page.add(
        betu
    )
    co1 = ft.Container(
        bgcolor='yellow',
        width=200,
        height=200,
        margin=10
    )
    co2 = ft.Container(
        bgcolor='blue',
        width=200,
        height=200,
        margin=10
    )
    co3 = ft.Container(
        bgcolor='green',
        width=200,
        height=200,
        margin=10
    )
    co4 = ft.Container(
        bgcolor='black',
        width=200,
        height=200,
        margin=10
    )
    co5 = ft.Container(
        bgcolor='red',
        width=200,
        height=200,
        margin=10
    )
    page.add(
        ft.Row(
            controls=[co1, co2, co3, co4, co5],
            wrap=True
        )
    )
    page.update()
if __name__=='__main__':
    ft.app(target=main)