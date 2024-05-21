import flet as ft
from tkinter import Tk, filedialog, messagebox, simpledialog
from PIL import Image, ImageOps, ExifTags
import io
import base64

def main(page: ft.Page) -> None:
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    
def open_image_dialog():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    root.destroy()
    return file_path

def resize_image(image):
    root = Tk()
    root.withdraw()
    new_width = simpledialog.askinteger("Átméretezés", "Új szélesség:")
    new_height = simpledialog.askinteger("Átméretezés", "Új magasság:")
    root.destroy()
    if new_width and new_height:
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
        return resized_image
    else:
        messagebox.showerror("Hiba", "Érvénytelen méretek")
        return None

def show_metadata(image):
    info = image._getexif()
    if info:
        metadata = {}
        for tag, value in info.items():
            tag_name = ExifTags.TAGS.get(tag, tag)
            metadata[tag_name] = value
        metadata_str = "\n".join(f"{k}: {v}" for k, v in metadata.items())
        root = Tk()
        root.withdraw()
        messagebox.showinfo("Metaadatok", metadata_str)
        root.destroy()
    else:
        root = Tk()
        root.withdraw()
        messagebox.showinfo("Metaadatok", "Nincs metaadat a képhez")
        root.destroy()

def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def main(page: ft.Page):
    page.title = "Képek Példa"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()

    def on_open_image(e):
        file_path = open_image_dialog()
        if file_path:
            image = Image.open(file_path)
            img_base64 = image_to_base64(image)
            img_control = ft.Image(src_base64=img_base64, width=300, height=300, fit=ft.ImageFit.CONTAIN)
            page.controls.append(img_control)
            page.update()
    
    def on_resize_image(e):
        file_path = open_image_dialog()
        if file_path:
            image = Image.open(file_path)
            resized_image = resize_image(image)
            if resized_image:
                img_base64 = image_to_base64(resized_image)
                img_control = ft.Image(src_base64=img_base64, width=300, height=300, fit=ft.ImageFit.CONTAIN)
                page.controls.append(img_control)
                page.update()
    
    def on_show_metadata(e):
        file_path = open_image_dialog()
        if file_path:
            image = Image.open(file_path)
            show_metadata(image)
    
    def on_show_color_channel(e, channel):
        file_path = open_image_dialog()
        if file_path:
            image = Image.open(file_path)
            channels = image.split()
            if channel == 'R':
                img = ImageOps.colorize(channels[0], black="black", white="red")
            elif channel == 'G':
                img = ImageOps.colorize(channels[1], black="black", white="green")
            elif channel == 'B':
                img = ImageOps.colorize(channels[2], black="black", white="blue")
            img_base64 = image_to_base64(img)
            img_control = ft.Image(src_base64=img_base64, width=300, height=300, fit=ft.ImageFit.CONTAIN)
            page.controls.append(img_control)
            page.update()

    open_image_btn = ft.ElevatedButton(text="Kép megnyitása", on_click=on_open_image)
    resize_image_btn = ft.ElevatedButton(text="Kép átméretezése", on_click=on_resize_image)
    show_metadata_btn = ft.ElevatedButton(text="Metaadatok megjelenítése", on_click=on_show_metadata)
    show_red_channel_btn = ft.ElevatedButton(text="Csak vörös", on_click=lambda e: on_show_color_channel(e, 'R'))
    show_green_channel_btn = ft.ElevatedButton(text="Csak zöld", on_click=lambda e: on_show_color_channel(e, 'G'))
    show_blue_channel_btn = ft.ElevatedButton(text="Csak kék", on_click=lambda e: on_show_color_channel(e, 'B'))

    page.add(open_image_btn, resize_image_btn, show_metadata_btn, show_red_channel_btn, show_green_channel_btn, show_blue_channel_btn)

ft.app(target=main)
