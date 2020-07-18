from PIL import Image

logo = Image.open('assets/logo.png')

bg = Image.open('assets/yt_banner2.png')
bg.paste(logo,(10,500),logo)
bg.save('sv_yt.png')

# for i in range(1,3):
#     bg = Image.open(f'assests/yt_banner{i}.png')
#     bg.paste(logo,(10,500),logo)
#     bg.save(f'yt_banner{i}_logo.png')

