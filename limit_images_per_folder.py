
import os
import random

base_folder = 'F:\AI_Mango_Propagation\data_mog'

image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')

for folder_name in os.listdir(base_folder):
    folder_path = os.path.join(base_folder, folder_name)

    if not os.path.isdir(folder_path):
        continue 

    all_images = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(image_extensions)
    ]

    if len(all_images) <= 48:
        print(f'✅ "{folder_name}" มี {len(all_images)} รูป ไม่ต้องลบ')
        continue

    images_to_delete = random.sample(all_images, len(all_images) - 48)

    for img in images_to_delete:
        img_path = os.path.join(folder_path, img)
        os.remove(img_path)

    print(f'🗑️ "{folder_name}" → ลบ {len(images_to_delete)} รูป เหลือ 48 รูป')

print('✅ เสร็จสิ้นแล้ว')