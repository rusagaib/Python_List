import os, sys
from PIL import Image

print('Image Resizer ~~(UwU)~')
try:
    arg1 = sys.argv[1]
    new_width = 200
    new_height = 320
    img = Image.open(arg1) # image *.png,*.jpg
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    name = input('Input name of file: ')
    img.save('/home/rusagaib/Pictures/resize_'+name+'.png')
    print('Finish~~')
    print('Press ENTER to exit')
except:
    for x in sys.argv:
        print(x)
    print('\nUsage :\n ~$ python3 resize_image.py <path or name your file using *.png or *.jpeg> <new_width> <new_height>\n\nOr please install pillow library using pip..\n\n pip3 install pillow\n')
