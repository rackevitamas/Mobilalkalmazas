import flet as ft
def main(page: ft.Page) -> None:

    page.title = "Login"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    def button_clicked(e):
        t1.value = f"User: {tx1.value}\nPassword: {tx2.value}"
        page.update()

    t1 = ft.Text()
    tx1 = ft.TextField(
        label="User",
        width=300
    )

    tx2 = ft.TextField(
        label="Password",
        width=300,
        password=True,
        can_reveal_password=True
    )

    button = ft.ElevatedButton(
        text="Submit",
        on_click=button_clicked
    )

    belepes = ft.Container(
        border_radius=15,
        width=400,
        padding=10,
        border=ft.border.all(2, 'red'),
        bgcolor='yellow',
        alignment=ft.alignment.center,
        content=ft.Column([tx1, tx2, button])
    )

    page.add(belepes, t1)    
    page.update()

if __name__=='__main__':
    ft.app(target=main)