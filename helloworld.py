import flet as ft
def main(page: ft.Page) -> None:
    page.add(
        ft.Text(value='Hello world!', color= 'red')
    )
    page.update()
if __name__== '__main__':
    ft.app(target=main)