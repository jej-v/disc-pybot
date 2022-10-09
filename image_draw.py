from PIL import Image,ImageDraw, ImageChops
import io
from urllib.request import urlopen, Request


def pinkuwu(image):
    with Image.open(image).convert("RGBA") as base:
        # make a blank image for the uwu, initialized to transparent text color
        ov = Image.new("RGBA", base.size, (255, 255, 255, 0))

        draw = ImageDraw.Draw(ov)
        draw.rectangle([(0,0), base.size], (242,202,244))

        out = ImageChops.overlay(base, ov)
        out.save('uwout.png')

def pinkuwu_member(image):
    with Image.open(urlopen(Request(image, headers={'User-Agent': 'Mozilla'}))).convert("RGBA") as base:
        # make a blank image for the uwu, initialized to transparent text color
        ov = Image.new("RGBA", base.size, (255, 255, 255, 0))

        draw = ImageDraw.Draw(ov)
        draw.rectangle([(0,0), base.size], (242,202,244))

        out = ImageChops.overlay(base, ov)
        out.save('uwout.png')

def senti(url):
    bg = Image.open('senti.png')
    img = Image.open(urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))).resize((170,170))

    img1 = Image.new("RGB", bg.size, (255, 255, 255))

    img1.paste(img, (230,90))
    mask_im = Image.open('mask.png').resize(bg.size).convert('1')

    final = Image.composite(bg, img1, mask_im)
    final.save("senti_result.png")
