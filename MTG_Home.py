import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import flet as ft
import MTG_CV

def main(page: ft.Page):
    comparison = ft.Text(MTG_CV.compare('Test_Images/Scotch_1.jpg', 'Test_Images/Scotch_12.jpg'))
    page.controls.append(comparison)
    page.update()

ft.app(target=main)
