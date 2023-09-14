import database
import base64
import os
from io import BytesIO
from PIL import Image
import time


#binary1 = database.get_catgirl()[0][6]
#img = base64.b64decode(binary1)
#my_file = open("lucky_img/image.png", "wb")
##my_file.write(img)


image = Image.open(database.get_catgirl()[0][6])

image.show()


#my_file = open("lucky_img/image.png", "wb")
#my_file.write(image)
#my_file.close()
#time.sleep(2)
#os.remove("lucky_img/image.png")


