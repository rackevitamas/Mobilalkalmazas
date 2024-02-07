import flet as ft
import datetime
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    szoveg = ft.Text(
        value = "Azokon a szép kék hegyeken túl\nFogsz te élni, kedvesem, ezentúl,\nOtt fogsz élni boldog férjed mellett,\nKit boldoggá egyedűl szived tett;\nNapkeletről messzebb napkeletre",
        bgcolor = ft.colors.RED_400,
        color = ft.colors.GREY_400,
        italic = True,
        font_family = "Kanit",
        selectable = True,
        size = 50,
        text_align = ft.TextAlign.CENTER,
        theme_style = ft.TextThemeStyle.DISPLAY_MEDIUM,
        weight = ft.FontWeight.W_600,
        )
    page.add(szoveg)
    def toggle_icon_button(e):
        e.control.selected = not e.control.selected
        e.control.update()
    page.add(
        ft.IconButton(
            icon=ft.icons.FAVORITE_BORDER,
            selected_icon=ft.icons.FAVORITE,
            on_click=toggle_icon_button,
            selected=False,
            style=ft.ButtonStyle(color={"selected": ft.colors.RED, "": ft.colors.RED}),
        )
    )
    datum = ft.Text(
        value=str(datetime.datetime.now())[:10],
        color = ft.colors.RED_500,
        )
    page.add(datum)
    page.update()
if __name__ == '__main__':
    ft.app(target=main)