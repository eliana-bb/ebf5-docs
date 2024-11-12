from PIL import Image
import os
for file in os.listdir("in"):
    im = Image.open("in/" + file)
    im = im.crop(im.getbbox())
    target_size = max(im.width, im.height)
    out_im = Image.new("RGBA", (target_size,target_size))
    out_im.paste(im, ((target_size-im.width)//2,(target_size-im.height)//2))
    out_im = out_im.resize((128, 128))
    out_im.save("in/" + file)