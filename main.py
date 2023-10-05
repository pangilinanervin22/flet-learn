import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    number_text = ft.Text(0)
    
    def add_click(e):
        number_text.value = str(int(number_text.value) + 1)
        page.update()
        print(number_text.value)

    page.add(
        number_text, 
        ft.ElevatedButton("Add", on_click=add_click, )
    )
    
      
ft.app(target=main)


# if __name__ == "__main__":
#     ft.app(port=5000, target=main)

# to run
# flet run main.py -r