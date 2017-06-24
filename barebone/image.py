from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def image(url):
	img = Image.open("url")

	draw = ImageDraw.Draw(img)

	font = ImageFont.truetype('sans-serif.ttf', 16)

	draw.text((0,0), "Sample Text", (255,255,0), font=font)
	draw = ImageDraw.Draw(img)
	img.save('sample-out.jpg')


