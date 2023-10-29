import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import flet as ft
import MTG_API
import MTG_CV
import ImageCrop

def main(page: ft.Page):
    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        inputImage = f'Test_Images/{color_dropdown.value}.jpg'
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
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("acclaimed_contender"),
            ft.dropdown.Option("archivist-of-oghma"),
            ft.dropdown.Option("arwen"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)
    # declaring the images, input will eventually be the picture
    # and the output will be the result of the API script
    # inputImage = 'Test_Images/acclaimed_contender.jpg'


ft.app(target=main)

