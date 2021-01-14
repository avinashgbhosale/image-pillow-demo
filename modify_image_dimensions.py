from PIL import Image

file = "demo.jpg"
img = Image.open(file)
new_width = 160
new_height = 210
img = img.resize((new_width, new_height))
img.save('modified_{}'.format(file))