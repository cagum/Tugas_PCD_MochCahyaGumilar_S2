import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt

def show_images_and_grayscale(image_paths):
    plt.figure(figsize=(12, 6))

    for i, img in enumerate(image_paths):
        image = imageio.imread(img['path'])
        plt.subplot(2, len(image_paths), i + 1)
        plt.imshow(image)
        plt.title(f'Warna Asli - {img["name"]}')
        plt.axis('off')
    for i, img in enumerate(image_paths):
        image = imageio.imread(img['path'])    
        
        grayscale = 0.289 * image[:, :, 0] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 2]

        plt.subplot(2, len(image_paths), len(image_paths) + i + 1)
        plt.imshow(grayscale, cmap='gray')
        plt.title(f'Grayscale - {img["name"]}')
        plt.axis('off')

    plt.tight_layout()
    plt.show()

image_paths = [
    {'path': 'D:\\Perkuliahan\\S5\\Pengolahan Citra Digital\\s2\\Tugas PCD s2\\daun_singkong.jpg', 'name': 'Daun Singkong'},
    {'path': 'D:\\Perkuliahan\\S5\\Pengolahan Citra Digital\\s2\\Tugas PCD s2\\daun_pepaya.jpg', 'name': 'Daun Pepaya'},
    {'path': 'D:\\Perkuliahan\\S5\\Pengolahan Citra Digital\\s2\\Tugas PCD s2\\daun_kenikir.jpg', 'name': 'Daun Kenikir'}
]

show_images_and_grayscale(image_paths)
