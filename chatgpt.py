import openai
import flet as ft


def main(page: ft.Page) -> None:
    

# Az API kulcsot itt kell megadni
    api_key = 'your_openai_api_key'

# ChatGPT üzenetgeneráló függvény
    def chat(prompt, engine='davinci'):
        openai.api_key = api_key
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

def main():
    print("Üdvözöllek a ChatGPT programban! Kilépéshez írd be: 'exit'")
        
    while True:
        user_input = input("Te: ")
            
        if user_input.lower() == 'exit':
            print("Köszönöm, hogy használtad a ChatGPT programot!")
            break
            
        response = chat(user_input)
        print("ChatGPT: ", response)

if __name__ == "__main__":
    ft.app(target=main)
