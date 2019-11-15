from PIL import Image
import os

directory_str = 'Output/skin_racks/'
out_dir = 'Output/skins/'
out_thumb_dir = 'Output/skins_thumb/'

directory = os.fsencode(directory_str)
skin_id = 0

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    rack = Image.open(directory_str + filename)

    for c in range(6):
        for r in range(5):
            skin = rack.crop(((c * 64), (r * 64), (c * 64) + 64, (r * 64) + 64))
            skin.save(out_dir + str(skin_id) + '.png')

            # Body parts
            left_arm = skin.crop((36, 52, 40, 64))
            right_arm = skin.crop((44, 20, 48, 32))
            left_leg = skin.crop((20, 52, 24, 64))
            right_leg = skin.crop((4, 20, 8, 32))
            torso = skin.crop((20, 20, 28, 32))
            head = skin.crop((8, 8, 16, 16))

            thumb = Image.new('RGBA', (16, 32))

            thumb.paste(head, (4, 0, 12, 8))
            thumb.paste(left_arm, (0, 8, 4, 20))
            thumb.paste(torso, (4, 8, 12, 20))
            thumb.paste(right_arm, (12, 8, 16, 20))
            thumb.paste(left_leg, (4, 20, 8, 32))
            thumb.paste(right_leg, (8, 20, 12, 32))

            thumb = thumb.resize((128, 256))

            thumb.save(out_thumb_dir + str(skin_id) + '.png')

            skin_id += 1
