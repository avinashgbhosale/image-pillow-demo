from PIL import Image

file = "demo.jpg"
image = Image.open(file)
MAX_SIZE = (100, 100)

image.thumbnail(MAX_SIZE)

# creating thumbnail
image.save('thumbnail.png')
image.show()
