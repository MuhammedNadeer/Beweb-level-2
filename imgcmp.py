from PIL import Image
import os

s = input("Enter the file path : ")
q = int(input("Enter compression quality(Range 0-100):"))
image = Image.open(s)

width, height = image.size
new_size = (width//2, height//2)
resized_image = image.resize(new_size)

resized_image.save('compressed_image.jpg', optimize=True, quality=q)

original_size = os.path.getsize(s)
compressed_size = os.path.getsize('compressed_image.jpg')

print("Original Size: ", original_size)
print("Compressed Size: ", compressed_size)