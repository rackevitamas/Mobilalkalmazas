import flet as ft
import datetime
def main(page: ft.Page):
    szoveg = ft.Text(
        value = "Azokon a szép kék hegyeken túl\nFogsz te élni, kedvesem, ezentúl,\nOtt fogsz élni boldog férjed mellett,\nKit boldoggá egyedűl szived tett;\nNapkeletről messzebb napkeletre",
        bgcolor = ft.colors.INDIGO_400,
        color = ft.colors.AMBER_300,
        italic = True,
        font_family = "Kanit",
        selectable = True,
        size = 50,
        text_align = ft.TextAlign.CENTER,
        theme_style = ft.TextThemeStyle.DISPLAY_MEDIUM,
        weigth = ft.FontWeigth.W_600,
        )
    datum = ft.Text(
        datum = datetime.datetime.now()
    )
ft.app(target=main)