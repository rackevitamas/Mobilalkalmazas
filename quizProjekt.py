import flet as ft

def main(page: ft.Page) -> None:

    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Quiz"
    page.scroll = ft.ScrollMode.AUTO

    t1 = ft.Text(
        value="Ezek közül melyik Európa Unió tagja?"
    )

    c1 = ft.Checkbox(label="Németország", value=False)
    c2 = ft.Checkbox(label="Franciaország", value=False)
    c3 = ft.Checkbox(label="Szerbia", value=False)
    c4 = ft.Checkbox(label="Görögország", value=False)

    t2 = ft.Text(
        value=""
    )

    t3 = ft.Text(
        value=""
    )

    t4 = ft.Text(
        value=""
    )

    t5 = ft.Text(
        value=""
    )

    t6 = ft.Text(
        value=""
    )
    
    t7 = ft.Text(
        value=""
    )

    t8 = ft.Text(
        value=""
    )
    

    page.add()


if __name__ == '__main__':
    ft.app(target=main)