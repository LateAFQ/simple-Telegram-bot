import database
import base64
import os
from io import BytesIO
from PIL import Image
import time


girls_info = database.get_catgirl()
females = [*girls_info]
print(len(females))
for info_cats in range(len(girls_info)):
    print(info_cats)

#len(str(info_cats))