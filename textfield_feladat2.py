import flet as ft
def main(page: ft.Page) -> None:
    page.title="Textfield"
    def button_clicked(e):
        if int(tx.value) % 2 == 0:
            t1.value = f"A szám páros:\t{tx.value}."
        else:
            t1.value = f"A szám páratlan:\t{tx.value}."
        page.update()
    t1 = ft.Text()
    tx = ft.TextField(
        label="Szám",
        hint_text="Ide beírod a számot",
        width=300
    )
    button = ft.ElevatedButton(
        text="Submit",
        on_click=button_clicked
    )
    page.add(tx, button, t1)
    page.add(ft.Divider())
    page.update()



if __name__=='__main__':
    ft.app(target=main)