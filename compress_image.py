from PIL import Image

file_name = "demo.jpg"
picture = Image.open(file_name)
n_file_name = file_name.split(".")[0] + ".jpeg"
picture.save("Compressed_"+n_file_name, optimize=True, quality=30)
