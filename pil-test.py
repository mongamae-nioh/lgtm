from PIL import Image, ImageDraw

file_path = './output.png'

image = Image.open(file_path)
draw = ImageDraw.Draw(image)

draw.text((0,0), 'TEST')
image.save('output2.png', 'PNG')