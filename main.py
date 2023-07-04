import os
from PIL import Image

# 透過画像を読み込む
mask_img = Image.open('./mask_do.png').convert("RGBA")
back_img = Image.open('./back.png').convert("RGBA")

# ディレクトリ内のすべての画像ファイルに対してループを行う
dir_path = './images/'  # 画像が保存されているディレクトリのパス
for filename in os.listdir(dir_path):
    if filename.endswith('.png'):
        # 元の画像を読み込む
        base_img_path = os.path.join(dir_path, filename)
        base_img = Image.open(base_img_path).convert("RGBA")

        # 元の画像の上に透過画像を合成する
        combined_img = Image.alpha_composite(base_img, mask_img)
        masked_img = Image.alpha_composite(back_img, combined_img)

        # 合成した画像を保存する（元のファイルを上書き）
        # ファイル名は「./masked/元のファイル名_masked.png」
        #masked_img.save(base_img_path.replace('.png', '_masked.png'))
        masked_img.save('./masked/' + filename.replace('.png', '_masked.png'))
