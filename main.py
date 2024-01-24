import flet as mobil
def main(page: mobil.Page) -> None:
    page.add(
        mobil.Text(value='Hello user!', color='red')
    )
    page.update()
if __name__== '__main__':
    mobil.app(target=main)