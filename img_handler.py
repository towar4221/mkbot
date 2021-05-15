import os, requests, glob
from PIL import Image

imgs = {
    "vs_bg": "./img/vs_bg.png",
    "vs_bg_animated":"./img/vs_bg_animated/frame_*.jpg"
}

async def vs_create(url1:str, url2:str):
    vs_bg = Image.open(os.path.join(imgs["vs_bg"]))
    
    size = (150, 150)

    f1 = Image.open(requests.get(url1, stream = True).raw).resize(size)
    f2 = Image.open(requests.get(url2, stream = True).raw).resize(size)

    pos1 = (vs_bg.width//2 - f1.width*2, vs_bg.height//2 - f1.height//2)
    pos2 = (vs_bg.width//2 + f2.width, vs_bg.height//2 - f1.height//2)

    vs_bg.paste(f1, pos1)
    vs_bg.paste(f2, pos2)

    vs_bg.save(os.path.join("./img", "result.png"))


# async def vs_create_animated(url1:str, url2:str):
#     vs_bg, *img - [Image.open(path) for path in glob.glob(imgs["vs_bg_animated"])]
#     size = (150, 150)
#     f1 = Image.open(requests.get(url1, stream=True).raw).resize(size)
#     f2 = Image.open(requests.get(url2, stream=True).raw).resize(size)

#     pos1 = (vs_bg.width//2 - f1.width*2,  vs_bg.hieght//2 - f1.height//2)
#     pos2 = (vs_bg.width//2 + f2.width,  vs_bg.hieght//2 - f2.height//2)

#     vs_bg.paste(f1, pos1)
#     vs_bg.paste(f2, pos2)

#     for im in img:
#         im.paste(f1, pos1)
#         im.paste(f2, pos2)

#     vs_bg.save(fp=ps.path.join("./img/result.git"), apped_images=img, save_all=True, duration=20, loop=0)