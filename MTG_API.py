import json
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import flet as ft
import MTG_CV
import requests
from PIL import Image
import urllib.request


def search():
    # %3A == "="
    response = requests.get("https://api.scryfall.com/cards/random")

    cardArt = response.json()['image_uris']['art_crop']

    urllib.request.urlretrieve(cardArt, "art.jpg")

    img = Image.open("art.jpg")
    img.show()