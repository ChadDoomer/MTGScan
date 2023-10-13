import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import flet as ft
import MTG_API
import MTG_CV
import ImageCrop

def main(page: ft.Page):
    # declaring the images, input will eventually be the picture
    # and the output will be the result of the API script
    inputImage = 'Test_Images/malfegor.jpg'
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

ft.app(target=main)
