import os
from PIL import Image

yourpath = 'folder_path'
for root, dirs, files in os.walk(yourpath, topdown=False):
    outpath = os.path.join(root,'jpg_image')
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    for name in files:
        print(os.path.join(root, name))
        if os.path.splitext(os.path.join(root, name))[1].lower() in ['.tif','.tiff']:
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                print(f"A jpeg file already exists for {name}")
            else:
                outfile = os.path.splitext(os.path.join(outpath, name))[0] + ".jpg"
                try:
                    print(f"Generating jpeg for {name}")
                    Image.open(os.path.join(root, name)).convert('RGB').save(outfile, "JPEG", quality=100)
                except Exception as e:
                    print(str(e))