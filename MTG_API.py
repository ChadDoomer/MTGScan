import json
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import flet as ft
import MTG_CV
import requests
from PIL import Image
import urllib.request


def searchForCard(inputImage):
    final_ID = 0
    value = 0
    query = MTG_CV.findText('name.jpg')
    # %3A == "="
    # for requesting from API
    # dataraw = requests.get(f"https://api.scryfall.com/cards/search?q=o:{query}")
    dataraw = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={query}")

    data = dataraw.json()
    print(data)

    try:
        cardArt = data['image_uris']['art_crop']
    except:
        try:
            for x in data['card_faces']:
                cardArt = x['image_uris']['art_crop']
        except:
            print("This card is not found in the database, sorry.")
            return "Not Found."

    # writes the card art to art.jpg
    urllib.request.urlretrieve(cardArt, "art.jpg")

    # calls the CV comparision function
    # and if the value is the highest so far
    # then it becomes the current best
    tempval = MTG_CV.compare(inputImage, "art.jpg")


    # this outputs the final card, might change to separate function
    name = data['name']
    urllib.request.urlretrieve(cardArt, "art.jpg")
    return name
