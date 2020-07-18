from PIL import Image, ImageFilter, ImageOps

base = Image.open('assets/test.jpg')

# Crop image all sides equal
img_crop = ImageOps.crop(base, border=50)
img_crop.save('crop_image.jpg')

# Crop image with (left,upper,right,lower) pixels
img_crop1 = base.crop((0,380,600,510))
img_crop1.save('crop1_image.jpg')

# Scale Image
img_scale = ImageOps.scale(base, 0.5)
img_scale.save('scale_image.jpg')

# Convert Image to grey scale
img_grey = ImageOps.grayscale(base)
img_grey.save('grey_image.jpg')

# Invert image
img_inv = ImageOps.invert(base)
img_inv.save('invert_image.jpg')

# Solarize image
img_solarize = ImageOps.solarize(base, threshold=100)
img_solarize.save('solarize_image.jpg')

# Applying BOX BLUR
img_blur = base.filter(filter=ImageFilter.BoxBlur(2))
img_blur.save('blur_image.jpg')

# GaussianBlur
img_gau = base.filter(filter=ImageFilter.GaussianBlur(2))
img_gau.save('gaussianblur_image.jpg')

# Min filter
img_minfilter = base.filter(filter=ImageFilter.MinFilter(3))
img_minfilter.save('minfilter_image.jpg')
