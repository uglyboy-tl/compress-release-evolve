from PIL import Image
import os

out_dir = os.path.join(os.getcwd(), 'output')
img_21x9 = Image.open(os.path.join(out_dir, 'wechat-21x9-cover.png'))
img_1x1  = Image.open(os.path.join(out_dir, 'wechat-1x1-cover.png'))

target_h = img_1x1.height
w21 = int(img_21x9.width * target_h / img_21x9.height)
img_21x9_resized = img_21x9.resize((w21, target_h), Image.LANCZOS)

total_w = w21 + img_1x1.width
canvas = Image.new('RGB', (total_w, target_h), (242, 244, 245))
canvas.paste(img_21x9_resized, (0, 0))
canvas.paste(img_1x1, (w21, 0))

out_path = os.path.join(out_dir, 'wechat-cover-pair-preview.png')
canvas.save(out_path, 'PNG')
print(f'拼接完成: {total_w}x{target_h} -> {out_path}')
