import os, time

from PIL import Image
from waveshare_epd import epd7in5_V2 

def isImage(input_list_item):
    if (".jpg" in input_list_item):
        return 1
    else:
        return 0

def getImage(input_list_item, maxwidth, maxheight):
    pil_im = Image.open(input_list_item)
    
    print(pil_im.size)
    
    ratio = min(maxwidth/pil_im.size[0], maxheight/pil_im.size[1])
    newWidth = int(pil_im.size[0] * ratio)
    newHeight = int(pil_im.size[1] * ratio)
    
    pil_im = pil_im.resize((newWidth, newHeight))
    pil_im_new = Image.new("RGB", (800, 480))
    pil_im_new.paste(pil_im, ((800-newWidth)//2, (480-newHeight)//2))
    
    
    print(pil_im_new.size)

    pil_im_new = pil_im_new.convert(mode='1', dither=Image.FLOYDSTEINBERG)
    return pil_im_new
    
os.chdir("/home/pi/Desktop/engagement")
os_list = os.listdir()
epd = epd7in5_V2.EPD()

epd.init()
epd.Clear()

width = 800
height = 480

print(os.getcwd())

while 1:
    
    for i in range(len(os_list)):
        
        if (isImage(os_list[i])):
            print(os_list[i])
            im = getImage(os_list[i], width, height)
            
            epd.display(epd.getbuffer(im))
            
            time.sleep(10)
            epd.init()
        else:
            continue
    
 