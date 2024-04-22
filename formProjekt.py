import flet as ft
def main(page: ft.Page) -> None:
    def button_clicked(e):
        t1.value = f"Név: {tx1.value}, neme: {dd.value}, {radiogroup.value}-ban lakik és hobbija {c1.value}, {c2.value}, {c3.value}, {c4.value}."
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
            ft.Radio(value="főváros", label="Főváros", width=300),
            ft.Radio(value="város", label="Város", width=300),
            ft.Radio(value="falu", label="Falu", width=300),
            ft.Radio(value="tanya", label="Tanya", width=300)
        ])
    )

    
    c1 = ft.Checkbox(label="Sport", width=300, value="sport"),
    c2 = ft.Checkbox(label="Főzés", width=300, value="főzés"),
    c3 = ft.Checkbox(label="Számítógépes játék", width=300, value="számítógépes játék"),
    c4 = ft.Checkbox(label="Állatok", width=300, value="állatok")
    

    button = ft.ElevatedButton(
        text="Submit",
        on_click=button_clicked
    )

    form = ft.Container(
        border=ft.border.all(3, 'red'),
        padding=20,
        alignment=ft.alignment.center,
        content = ft.Column([tx1, dd, radiogroup, c1, c2, c3, c4, button])
    )

    

    t1 = ft.Text()
    page.add(form, t1)

if __name__ == '__main__':
    ft.app(target=main)