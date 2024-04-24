import flet as ft

def main(page: ft.Page) -> None:

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.DARK

    def button_clicked(e):
        name = tx1.value.strip()  
        words = name.split()  

        
        if len(words) < 2:
            t1.value = "Legalább két szóból kell állnia a névnek!"
            page.update()
            return

        if not all(word.istitle() for word in words):
            t1.value = "Minden szónak nagybetűvel kell kezdődnie!"
            page.update()
            return
        

        t1.value = f"Név: {tx1.value}, neme: {dd.value}, {radiogroup.value}-ban lakik és hobbija \n\tSport: {c1.value}, \n\tFőzés: {c2.value}, \n\tSzámítógépes játék: {c3.value}, \n\tÁllatok {c4.value}."
        page.update() 

        

    page.title = "Form"
    page.scroll = ft.ScrollMode.AUTO
    
    tx1 = ft.TextField(
        label="Név",
        width=300
    )

    t2 = ft.Text(
        value="Mi a nemed?"
    )

    dd = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Női"),
            ft.dropdown.Option("Férfi")
        ]
    )

    t3 = ft.Text(
        value="Hol laksz?"
    )

    radiogroup = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="főváros", label="Főváros", width=300),
            ft.Radio(value="város", label="Város", width=300),
            ft.Radio(value="falu", label="Falu", width=300),
            ft.Radio(value="tanya", label="Tanya", width=300)
        ])
    )

    t4 = ft.Text(
        value="Mi a hobbid?"
    )

    c1 = ft.Checkbox(label="Sport", value=False)
    c2 = ft.Checkbox(label="Főzés", value=False)
    c3 = ft.Checkbox(label="Számítógépes játék", value=False)
    c4 = ft.Checkbox(label="Állatok", value=False)
    

    button = ft.ElevatedButton(
        text="Submit",
        on_click=button_clicked
    )

    form = ft.Container(
        border=ft.border.all(3, 'red'),
        padding=20,
        width=600,
        alignment=ft.alignment.center,
        content = ft.Column([tx1, t2, dd, t3, radiogroup, t4, c1, c2, c3, c4, button])
    )

    

    t1 = ft.Text()
    page.add(form, t1)

if __name__ == '__main__':
    ft.app(target=main)