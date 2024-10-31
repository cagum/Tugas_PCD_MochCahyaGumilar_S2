import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt

def show_images_and_threshold(image_paths, threshold_value=128):

    fig, axes = plt.subplots(2, len(image_paths), figsize=(12, 8))

    for i, img in enumerate(image_paths):
        image = imageio.imread(img['path'])
        
        axes[0, i].imshow(image)
        axes[0, i].set_title(f'Original - {img["name"]}')
        axes[0, i].axis('off')
        
        grayscale = 0.289 * image[:, :, 0] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 2]
        
        binary_image = np.where(grayscale > threshold_value, 1, 0)
        
        axes[1, i].imshow(binary_image, cmap='gray')
        axes[1, i].set_title(f'Threshold - {img["name"]}')
        axes[1, i].axis('off')
    
    plt.tight_layout()
    plt.show()

image_paths = [
    {'path': 'D:\\Perkuliahan\\S5\\Pengolahan Citra Digital\\s2\\Tugas PCD s2\\daun_singkong.jpg', 'name': 'Daun Singkong'},
    {'path': 'D:\\Perkuliahan\\S5\\Pengolahan Citra Digital\\s2\\Tugas PCD s2\\daun_pepaya.jpg', 'name': 'Daun Pepaya'},
    {'path': 'D:\\Perkuliahan\\S5\\Pengolahan Citra Digital\\s2\\Tugas PCD s2\\daun_kenikir.jpg', 'name': 'Daun Kenikir'}
]

show_images_and_threshold(image_paths, threshold_value=128)
