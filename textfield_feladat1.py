import flet as ft
def main(page: ft.Page) -> None:
    page.title="Textfield"
    def button_clicked(e):
        t1.value = f"A szövegmező tartalma:\n'{tx.value}'."
        page.update()
    t1 = ft.Text()
    tx = ft.TextField(
        label="Name",
        hint_text="Ide beírod a nevedet",
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