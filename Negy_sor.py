import flet as ft

def main(page: ft.page) -> None:
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Négyen egy sorban?"

    text = ft.Text(
        value="Négyen egy sorban?",
        theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
        text_align=ft.TextAlign.CENTER,
        color='white'
    )
    
    # Az oldal szélességének a harmada
    third_of_width = page.width // 3

    c1 = ft.Container(
        width=third_of_width + 50,
        height=100,
        bgcolor='red',
    )
    
    c2 = ft.Container(
        width=third_of_width + 100,
        height=100,
        bgcolor='blue'
    )

    c3 = ft.Container(
        width=third_of_width + 150,
        height=100,
        bgcolor='black'
    )

    c4 = ft.Container(
        width=third_of_width + 200,
        height=100,
        bgcolor='green'
    )

    # Minden konténer egy sorban, Wrap opcióval, hogy ha nem férnek el, akkor a következő sorba kerüljenek
    page.add(text)
    page.add(ft.Row(controls=[c1, c2, c3, c4], wrap=True))
    page.update()

if __name__ == '__main__':
    ft.app(target=main)
