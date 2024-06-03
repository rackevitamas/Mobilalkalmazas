import openai
import flet as ft
import os
import time
import threading


def main(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    api_key = os.getenv('sk-proj-zO6LNh5AjjS93VRYnHlzT3BlbkFJCQanAg4huDsWatz718HH')

    def chat(prompt, engine='davinci'):
        openai.api_key = api_key
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    greeting_text = ft.Text("Üdvözöllek a ChatGPT programban! Kilépéshez írd be: 'exit'")
    user_input = ft.TextField(label="Te", width=400)
    chat_output = ft.Column()

    def send_message(e):
        prompt = user_input.value
        if prompt.lower() == 'exit':
            chat_output.controls.append(ft.Text("Köszönöm, hogy használtad a ChatGPT programot!"))
            page.update()
            
            def delayed_close():
                time.sleep(3)
                page.window_close()
            
            threading.Thread(target=delayed_close).start()
            return
        
        response_text = chat(prompt)
        chat_output.controls.append(ft.Text(f"Te: {prompt}"))
        chat_output.controls.append(ft.Text(f"ChatGPT: {response_text}"))
        user_input.value = ""
        page.update()

    send_button = ft.ElevatedButton(text="Küldés", on_click=send_message)

    page.add(greeting_text)
    page.add(user_input)
    page.add(send_button)
    page.add(chat_output)

if __name__ == "__main__":
    ft.app(target=main)