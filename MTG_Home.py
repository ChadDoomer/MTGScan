import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import flet as ft
import MTG_CV

def main(page: ft.Page):
    # declaring the images, input will eventually be the picture
    # and the output will be the result of the API script
    inputImage = 'Test_Images/Scotch_1.jpg'
    outputImage = 'Test_Images/Scotch_12.jpg'

    # this will probably be moved to API script
    comparison = ft.Text(MTG_CV.compare(inputImage, outputImage), size=30)

    # this is the flet stuff, outputImageFlet needs to be formatted
    # like this, so it can output correctly
    outputImageFlet = ft.Image(src=outputImage, width=400, height=400)
    page.add(outputImageFlet)
    page.add(ft.Text("Your card scored:", size=30), comparison)

ft.app(target=main)
