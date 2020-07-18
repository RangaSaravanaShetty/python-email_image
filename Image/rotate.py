from PIL import Image

logo = Image.open('assets/sigma.png')

# Rotate 90 deg Counterclockwise
logo_90 = logo.rotate(90)
logo_90.save('logo_90.png')

# Rotate 45 deg Counterclockwise
logo_45 = logo.rotate(45)
logo_45.save('logo_45.png')

# Rotate 180 deg Counterclockwise
logo_180 = logo.rotate(180)
logo_180.save('logo_180.png')

# Rotate 270 deg Counterclockwise
logo_270 = logo.rotate(270)
logo_270.save('logo_270.png')

# Flip Image Left Rigt
logo_flip_right = logo.transpose(Image.FLIP_LEFT_RIGHT)
logo_flip_right.save('logo_flip_right.png')

# Flip Image Top Bottom
logo_flip_top = logo.transpose(Image.FLIP_TOP_BOTTOM)
logo_flip_top.save('logo_flip_top.png')