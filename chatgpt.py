import openai
import flet as ft


def main(page: ft.Page) -> None:
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

# Az API kulcsot itt kell megadni
    api_key = 'sk-proj-zO6LNh5AjjS93VRYnHlzT3BlbkFJCQanAg4huDsWatz718HH'

# ChatGPT üzenetgeneráló függvény
    def chat(prompt, engine='davinci'):
        openai.api_key = api_key
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()


    page.add(ft.Text("Üdvözöllek a ChatGPT programban! Kilépéshez írd be: 'exit'"))
        
    while True:
        user_input = ft.TextField(value="Te: ")
        page.add(user_input)
        if user_input.value == 'exit':
            ft.Text("Köszönöm, hogy használtad a ChatGPT programot!")
            break
            
        page.add(response = chat(user_input))
        page.update()
        # print(response)
        page.add(
            ft.Text(f"ChatGPT: {response}")
        )
        page.update()


if __name__ == "__main__":
    ft.app(target=main)
