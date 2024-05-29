import openai
import flet as ft


def main(page: ft.Page) -> None:
    

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

def main(page: ft.Page) -> None:
    ft.Text("Üdvözöllek a ChatGPT programban! Kilépéshez írd be: 'exit'")
        
    while True:
        user_input = ft.TextField(value="Te: ")
        if user_input == 'exit':
            ft.Text("Köszönöm, hogy használtad a ChatGPT programot!")
            break
            
        response = chat(user_input)
        ft.Text(f"ChatGPT: {response}")
        
    page.add()

if __name__ == "__main__":
    ft.app(target=main)
