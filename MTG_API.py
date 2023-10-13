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
    query = MTG_CV.findText('bottom.jpg')
    # %3A == "="
    # for requesting from API
    dataraw = requests.get(f"https://api.scryfall.com/cards/search?q=o:{query}")

    data = dataraw.json()
    print(data)

    # this function is fucked
    # it works perfectly until an arbitrary
    # number is reached then it says Error
    # nevermind it works now
    for i in data['data']:
        tempval = 0

        # the below blurb extracts the card ID and image
        ID = i['id']
        try:
            imageURI = i['image_uris']
        except:
            for x in i['card_faces']:
                imageURI = x['image_uris']
        cardArt = imageURI['art_crop']

        # writes the card art to art.jpg
        urllib.request.urlretrieve(cardArt, "art.jpg")

        # calls the CV comparision function
        # and if the value is the highest so far
        # then it becomes the current best
        tempval = MTG_CV.compare(inputImage, "art.jpg")
        if tempval > value:
            value = tempval
            final_ID = ID

    # this outputs the final card, might change to separate function
    finalCard = requests.get(f"https://api.scryfall.com/cards/{final_ID}")
    name = finalCard.json()['name']
    cardArt = finalCard.json()['image_uris']['art_crop']
    urllib.request.urlretrieve(cardArt, "art.jpg")
    return name
