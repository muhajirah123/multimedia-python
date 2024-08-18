import pygame
from PIL import Image
import cv2
import moviepy
import pydub
import tkinter as tk
import pkg_resources

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", Image.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    print("✅ MoviePy version:", moviepy.__version__)
    print("✅ Pydub version:", pkg_resources.get_distribution('pydub').version)
    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()
