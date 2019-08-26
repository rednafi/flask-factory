import art
from .ascii_art import text


def draw_ascii(text=text):
    art_1 = art.text2art(text)
    return art_1
