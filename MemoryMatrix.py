import flet as ft
import random
import time


clicked_number = 0
highest_level = 1

class GenerateGrid(ft.UserControl):
    def __init__(self, difficulty):
        self.grid = ft.Column(
            opacity=0,
            animate_opacity=300
        )
        self.blue_tiles: int = 0
        self.correct: int = 0
        self.incorrect: int = 0
        self.difficulty: int = difficulty
        super().__init__()
        
    def show_color(self, e):
        if e.control.data == "#4cbbb5":
            e.control.bgcolor = "#4cbbb5"
            e.control.opacity = 1
            e.control.update()
            self.correct += 1
            e.page.update()
            
        else:
            e.control.bgcolor = "#982c33"
            e.control.opacity = 1
            e.control.update()
            self.incorrect +=1
            e.page.update()

    def build(self):
        rows: list = [
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=54,
                        height=54,
                        animate=300,
                        on_click=lambda e: self.show_color(e),
                    )
                    for _ in range(5)
                ],
            )
            for _ in range(5)
        ]
        
        colors: list = ["#5c443b", "#4cbbb5"]
        
        for row in rows:
            for container in row.controls[:]:
                container.bgcolor = random.choices(
                    colors, weights=[10, self.difficulty]
                    ) [0]
                container.data = container.bgcolor
                if container.bgcolor == "#4cbbb5":
                    self.blue_tiles += 1

        self.grid.controls = rows
        return self.grid
    
    

def main(page: ft.Page) -> None:
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    stage = ft.Text(size=13, weight="bold")
    result = ft.Text(size=13, weight="bold")
    record = ft.Text(size=13, weight="bold")
    
    
    start_button = ft.Container(
        content = ft.ElevatedButton(
            on_click = lambda e: start_game(e, GenerateGrid(2)),
            content = ft.Text("Kezdés!", size=13, weight="bold"),
            style = ft.ButtonStyle(
                shape = {"": ft.RoundedRectangleBorder(radius = 8)},
                color = {"": "white"}
            ),
            height = 45,
            width = 255,
        )
    )
    
    def start_game(e, level):
        global highest_level
        global clicked_number
        if clicked_number < 2:
            start_button.disabled = True
        result.value = ""
        grid = level
        page.controls.insert(3, grid)
        page.update()
        
        grid.grid.opacity = 1
        grid.grid.update()
        
        stage.value = f"{grid.difficulty - 1}. szintű"
        stage.update()
        
        
        
        start_button.disabled = True
        start_button.update()
        
        time.sleep(1.5)
        
        #Itt kell megszüntetni a konténerbe kattintást!
        
        for rows in grid.controls[0].controls[:]:
            for container in rows.controls[:]:
                if  container.bgcolor == "#4cbbb5":
                    container.bgcolor = "#5c443b"
                    container.update()
                    
        
        while True:
            if grid.correct == grid.blue_tiles:
                grid.grid.disabled: bool = True
                grid.grid.update()

                result.value: str = "SZÉP MUNKA! Eltaláltad mindet!"
                result.color = "green700"
                result.update()
                
                time.sleep(2)
                result.value = ""
                page.controls.remove(grid)
                page.update()
                
                difficulty = grid.difficulty + 1
                
                if difficulty - 1 > highest_level:
                    highest_level = difficulty - 1
                    record.value = f"Rekord: {highest_level}. szint"
                    record.update()
                
                start_game(e, GenerateGrid(difficulty))
                break
        
            if grid.incorrect == 3:
                result.value = "Bocsi, elfogyott a probálkozási lehetőséget. Probálkozz újra!"
                result.color = "red700"
                result.update()
                time.sleep(2)
                page.controls.remove(grid)
                page.update()
                start_button.disabled = False
                start_button.update()
                break
        
    
    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "Memória Mátrix",
                    size=22,
                    weight="bold")
            ]),
        ft.Row(
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [result]
        ),
        ft.Row(
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [record]
        ),
        ft.Divider(height=10, color="transparent"),
        ft.Divider(height=10, color="transparent"),
        
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER, controls=[stage]
            ),
        ft.Divider(height=10,color="transparent"),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[start_button],
        )
    )
    
    
    page.update()
if __name__ == "__main__":
    ft.app(target=main)