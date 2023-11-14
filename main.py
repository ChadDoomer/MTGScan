import flet as ft
import cv2
import MTG_API
import ImageCrop

def main(page: ft.Page):

    url = ""
    # file picker function
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
                    "Pick file",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False
                    ),
                ),
                selected_files,
            ]
        )
    )

    def url_button(e):
        if not txt_url.value:
            txt_url.error_text = "Please enter the url"
            page.update()
        else:
            url = txt_url.value + "/video"
            print(url)
            a = ft.ElevatedButton("Open Camera", on_click=camera(url))

    txt_url = ft.TextField(label="Download IP Webcam on your Android device and enter the IPv4 value.")
    page.add(txt_url, ft.ElevatedButton("Access the camera.", on_click=url_button))

    def camera(url):
        cap = cv2.VideoCapture(url)
        while (True):
            ret, frame = cap.read()
            if frame is not None:
                cv2.imshow('frame', frame)
            q = cv2.waitKey(1)
            if q == ord("q"):
                cv2.imwrite("picture.jpg", frame)
                ImageCrop.rotate("picture.jpg")
                break
        cv2.destroyAllWindows()

    # function that runs the program
    def run_program(e):
        if txt_url.value == "":
            inputImage = f'Test_Images/{selected_files.value}'
        else:
            inputImage = 'rotated_picture.jpg'
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

