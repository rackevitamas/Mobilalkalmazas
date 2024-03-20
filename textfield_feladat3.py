import flet as ft

def main(page: ft.Page) -> None:
    page.title="Textfield"
    def button_clicked(e):
        nev = tx.value.split()
        t1.value = f"A szövegmező tartalma:\nVezetékneve: '{nev[0]}'\nKeresztneve: '{nev[1]}'."
        page.update()
    t1 = ft.Text()
    tx = ft.TextField(
        label="Full Name",
        hint_text="Ide beírod a teljes nevedet",
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