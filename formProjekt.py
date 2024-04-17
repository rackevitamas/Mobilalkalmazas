import flet as ft
def main(page: ft.Page) -> None:
    def button_clicked(e):
        t1.value = f"Név: {tx1.value}, neme: {dd.value}, {radiogroup.value}-ban lakik és hobbija {chxgroup.value}."
        page.update() 
    page.title = "Form"
    page.scroll = ft.ScrollMode.AUTO
    
    tx1 = ft.TextField(
        label="Név",
        width=300
    )

    dd = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Női"),
            ft.dropdown.Option("Férfi")
        ]
    )

    radiogroup = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(label="Főváros", width=300),
            ft.Radio(label="Város", width=300),
            ft.Radio(label="Falu", width=300),
            ft.Radio(label="Tanya", width=300)
        ])
    )

    chxgroup = ft.CupertinoCheckbox(
        ft.Checkbox(label="Sport", width=300),
        ft.Checkbox(label="Főzés", width=300),
        ft.Checkbox(label="Számítógépes játék", width=300),
        ft.Checkbox(label="Állatok", width=300)
    )

    

    form = ft.Container(
        border=ft.border.all(3, 'red'),
        padding=20,
        alignment=ft.alignment.center,
        content = ft.Column([tx1, dd, radiogroup, chxgroup, button])
    )

    button = ft.ElevatedButton(
        text="Submit",
        on_click=button_clicked
    )

    t1 = ft.Text()
    page.add(form, t1)

if __name__ == '__main__':
    ft.app(target=main)