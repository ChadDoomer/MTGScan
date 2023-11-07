import flet as ft
import MTG_API
import ImageCrop

def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False
                    ),
                ),
                selected_files,
            ]
        )
    )

    def run_program(e):
        inputImage = f'Test_Images/{selected_files.value}'
        print(inputImage)
        outputImage = 'art.jpg'

        ImageCrop.crop(inputImage)

        # calls the card search function and outputs the name
        name = ft.Text(MTG_API.searchForCard('top.jpg'), size=30)

        # this is the flet stuff, outputImageFlet needs to be formatted
        # like this, so it can output correctly
        inputImageFlet = ft.Image(src=inputImage, width=400, height=400)
        outputImageFlet = ft.Image(src=outputImage, width=400, height=400)
        page.add(inputImageFlet)
        page.add(outputImageFlet)
        page.add(ft.Text("Your card is:", size=30), name)
        page.update()

        output_text = ft.Text()

        page.add(output_text)
        # declaring the images, input will eventually be the picture
        # and the output will be the result of the API script

    b = ft.ElevatedButton("Run the Program", on_click=run_program)
    page.add(b)

ft.app(target=main)

