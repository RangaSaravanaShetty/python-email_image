from PIL import Image, ImageFont, ImageDraw

# Using a banner image
base = Image.open('assets/yt_banner1.png')

# creating a text layer with transparent data
txt = Image.new('RGBA',base.size,'#ffffff00')

# importing fonts
fnt = ImageFont.truetype("assets/fonts/FreeMono.ttf",20)
fnt1 = ImageFont.truetype("assets/fonts/DejaVuSans.ttf",80)

#data to add on the image
title = "Skill Disk"
tag_line = "Friend for your skill development"
social_media = "Facebook\nTwitter\nTelegram\nYoutube"

#drawinging text over image
d = ImageDraw.Draw(txt)
d.text((20,100),title,font=fnt1, fill="#ffaa00",align="center", stroke_width=2, stroke_fill='#2a2a2a' )
d.text((20,200),tag_line,font=fnt, fill="#000000",align="center" )
d.multiline_text((20,600),social_media,font=fnt, fill="#ffffff",align="left" )

#draw a line
d.line([(20,190),(400,190)],fill="#ffffff",width=5)

#Add text over the base image
out = Image.alpha_composite(base,txt)


out.save('text_banner.png')