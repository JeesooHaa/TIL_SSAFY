import requests
import random

font = requests.get('http://artii.herokuapp.com/fonts_list')

font_choice = random.choice(font.text)

print(font.text)
print(type(font.text))
