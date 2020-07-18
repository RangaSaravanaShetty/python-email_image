from PIL import Image

# Create a red image with width and height of 100 px
img1 = Image.new('RGB',(100,100),'red')

img1.save('red_image.png')