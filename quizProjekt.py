import flet as ft
def main(page: ft.Page) -> None:

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Quiz"
    page.scroll = ft.ScrollMode.AUTO

    t1 = ft.Text(
        value="Az alábbiak közül melyik Spanyolország fővárosa?"
    )


    t1R = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Madrid", label="Madrid", width=300),
            ft.Radio(value="Malaga", label="Malaga", width=300),
            ft.Radio(value="Barcelona", label="Barcelona", width=300)
        ])
    )


    t2 = ft.Text(
        value="Milyen fajta vitamin az A-vitamin?"
    )

    t2R = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="vízben oldódó", label="Vízben oldódó", width=300),
            ft.Radio(value="zsírban oldódó", label="Zsírban oldódó", width=300),
        ])
    )

    t3 = ft.Text(
        value="Ford gyártók helyek?"
    )


    t3R1 = ft.Checkbox(label="Köln", value=False)
    t3R2 = ft.Checkbox(label="Saarlouis", value=False)
    t3R3 = ft.Checkbox(label="Budapest", value=False)
    t3R4 = ft.Checkbox(label="London", value=False)



    t4 = ft.Text(
        value="Ford cég eredeti termékeny cég volt-e?"
    )


    t4R = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Igaz"),
            ft.dropdown.Option("Hamis")
        ]
    )


    t5 = ft.Text(
        value="Mandy's Alap keveréke?"
    )

    t5R1 = ft.Checkbox(label="Kakkukfű", value=False)
    t5R2 = ft.Checkbox(label="Galaj", value=False)
    t5R3 = ft.Checkbox(label="Fahéj", value=False)
    t5R4 = ft.Checkbox(label="Eper", value=False)

    container = ft.Container()

    page.add(t1, t1R, t2, t2R, t3, t3R1, t3R2, t3R3, t3R4, t4, t4R)
    page.update()


if __name__ == '__main__':
    ft.app(target=main)