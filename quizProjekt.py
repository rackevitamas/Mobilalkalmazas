import flet as ft

def main(page: ft.Page) -> None:
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Quiz"
    page.scroll = ft.ScrollMode.AUTO

    # Define correct answers
    correct_answers = {
        "q1": "Madrid",
        "q2": "zsírban oldódó",
        "q3": ["Köln", "Saarlouis"],
        "q4": "Igaz",
        "q5": ["Kakkukfű", "Galaj", "Fahéj"],
        "q6": "RAM",
        "q7": "Igaz",
        "q8": "World Health Organization"
    }

    # Question 1
    q1 = ft.Text(value="Az alábbiak közül melyik Spanyolország fővárosa?")
    q1_options = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Madrid", label="Madrid", width=300),
            ft.Radio(value="Malaga", label="Malaga", width=300),
            ft.Radio(value="Barcelona", label="Barcelona", width=300)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    # Question 2
    q2 = ft.Text(value="Milyen fajta vitamin az A-vitamin?")
    q2_options = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="vízben oldódó", label="Vízben oldódó", width=300),
            ft.Radio(value="zsírban oldódó", label="Zsírban oldódó", width=300),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    # Question 3
    q3 = ft.Text(value="Ford gyártók helyek?")
    q3_options = ft.Container(
        ft.Column([
            ft.Checkbox(label="Köln", value=False),
            ft.Checkbox(label="Saarlouis", value=False),
            ft.Checkbox(label="Budapest", value=False),
            ft.Checkbox(label="London", value=False)
        ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=300)

    # Question 4
    q4 = ft.Text(value="Ford cég eredeti termékeny cég volt?")
    q4_options = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Igaz"),
            ft.dropdown.Option("Hamis")
        ]
    )

    # Question 5
    q5 = ft.Text(value="Mandy's Alap keveréke?")
    q5_options = ft.Container(
            ft.Column([
                ft.Checkbox(label="Kakkukfű", value=False),
                ft.Checkbox(label="Galaj", value=False),
                ft.Checkbox(label="Fahéj", value=False),
                ft.Checkbox(label="Eper", value=False)
            ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            width=300)

    # Question 6
    q6 = ft.Text(value="Számítógép részei:")
    q6_options = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Professzor", label="Professzor", width=300),
            ft.Radio(value="Nyomtató", label="Nyomtató", width=300),
            ft.Radio(value="RAM", label="RAM", width=300)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    # Question 7
    q7 = ft.Text(value="Világegyetem matekból áll?")
    q7_options = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="Igaz", label="Igaz", width=300),
            ft.Radio(value="Hamis", label="Hamis", width=300)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    # Question 8
    q8 = ft.Text(value="Minek a rövidítése WHO-nak?")
    q8_options = ft.TextField(width=300)

    # Function to calculate the score
    def calculate_score(e):
        score = 0
        total_questions = 8

        # Check answers
        if q1_options.value == correct_answers["q1"]:
            score += 1
        if q2_options.value == correct_answers["q2"]:
            score += 1
        selected_q3 = [cb.label for cb in q3_options.controls if isinstance(cb, ft.Checkbox) and cb.value]
        if selected_q3 == correct_answers["q3"]:
            score += 1
        if q4_options.value == correct_answers["q4"]:
            score += 1
        selected_q5 = [cb.label for cb in q5_options.controls if isinstance(cb, ft.Checkbox) and cb.value]
        if selected_q5 == correct_answers["q5"]:
            score += 1
        if q6_options.value == correct_answers["q6"]:
            score += 1
        if q7_options.value == correct_answers["q7"]:
            score += 1
        if q8_options.value.strip() == correct_answers["q8"]:
            score += 1

        # Calculate percentage
        percentage = (score / total_questions) * 100

        # Display score
        result.value = f"Your score is: {percentage}% ({score}/{total_questions} correct)"
        page.update()

    # Submit button
    submit_button = ft.ElevatedButton(text="Ellenőrzés!", on_click=calculate_score)

    # Result text
    result = ft.Text()

    # Container for all questions and submit button
    c1 = ft.Container(
        content=ft.Column([
            q1, q1_options, 
            q2, q2_options, 
            q3, q3_options, 
            q4, q4_options, 
            q5, q5_options, 
            q6, q6_options, 
            q7, q7_options, 
            q8, q8_options,
            submit_button,
            result
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        alignment=ft.alignment.center
    )

    # Add the container to the page
    page.add(c1)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)
