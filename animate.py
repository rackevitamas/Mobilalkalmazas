import flet as ft
def main(page: ft.Page):
    def on_hover(e):
        e.control.bgcolor = "blue" if e.data == "true" else "red"
        e.control.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    c1 = ft.Container(
        content = ft.Text("A szemed\nNagy, mély szemed\nreámragyog sötéten\nS lelkemben halkan fuvoláz a vágy.\nMint ifú pásztor künn a messzi réten\nSubáján fekve méláz fényes égén\nS kezemben búsan sírdogál a nád."),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        width=300,
        height=300,
        border = 5,
        border_radius=10,
        bgcolor=ft.colors.DEEP_PURPLE,
        ink=False,
        on_hover=on_hover,
        on_click=lambda e: page.launch_url(url='https://szerelmes-versek.info/azokon-szep-kek-hegyeken-tul-petofi-sandor.vers')
    ),
    c2 = ft.Container(
        content = ft.Text("A szemed\nNagy, mély szemed\nreámragyog sötéten\nS lelkemben halkan fuvoláz a vágy.\nMint ifú pásztor künn a messzi réten\nSubáján fekve méláz fényes égén\nS kezemben búsan sírdogál a nád."),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        width=300,
        height=300,
        border = 5,
        border_radius=10,
        bgcolor=ft.colors.DEEP_PURPLE,
        ink=False,
        on_hover=on_hover,
        on_click=lambda e: page.launch_url(url='https://szerelmes-versek.info/azokon-szep-kek-hegyeken-tul-petofi-sandor.vers')
    )
            

    page.add(ft.Row(controls=[c1, c1], alignment=ft.MainAxisAlignment.CENTER, )  )
        
if __name__ == '__main__':
    ft.app(target=main)