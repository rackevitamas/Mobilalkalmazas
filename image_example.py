import flet as ft


def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.scroll = ft.ScrollMode.HIDDEN

    img = ft.Container(
        bgcolor='red',
        content=ft.Image(
            src="kep1.webp",
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN,
            color_blend_mode=ft.BlendMode.DARKEN,
            error_content=ft.Text("Hiba történt, nem található a kép")
        ),
        
    )
    
    
    images = ft.Row(wrap=False, scroll=ft.ScrollMode.ALWAYS)

    page.add(img, images)

    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    c1 =  ft.Container(
        image_src="kep.jpg",
        width=450,
        height=300,
        image_repeat=ft.ImageRepeat.REPEAT_X,
        border_radius=ft.border_radius.all(20)
    )
    page.add(c1)
    page.update()


ft.app(target=main)
