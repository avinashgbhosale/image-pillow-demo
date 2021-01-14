from PIL import Image
file_name = "demo.jpg"
im = Image.open(file_name)
im.save('new_ext.jpeg')
