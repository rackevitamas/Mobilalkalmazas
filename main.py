import flet as mobil
def main(page: mobil.Page) -> None:
    page.add(
        mobil.Text(value='Rác Kevi Tamás vagyok.', color='blue'),
        mobil.Text(value='A kedvenc filmem: Bright.', color='red'),
        mobil.Text(value='Ahová szeretnék utazni: szinte bárhova, de elsőre tengerre.', color='yellow'),
    )
    page.update()
if __name__== '__main__':
    mobil.app(target=main)