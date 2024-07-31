from PIL import Image
import random

def encrypt_image(image_path, output_path, key):
    
    img = Image.open(image_path)
    pixels = img.load()

    
    width, height = img.size

    
    random.seed(key)

    
    for i in range(width):
        for j in range(height):
           
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            
            
            pixels[i, j], pixels[x, y] = pixels[x, y], pixels[i, j]

   
    img.save(output_path)

def decrypt_image(image_path, output_path, key):
    
    img = Image.open(image_path)
    pixels = img.load()

    
    width, height = img.size

   
    random.seed(key)

    
    swaps = []
    for i in range(width):
        for j in range(height):
           
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            
          
            swaps.append(((i, j), (x, y)))

    
    for swap in reversed(swaps):
        (i, j), (x, y) = swap
        pixels[i, j], pixels[x, y] = pixels[x, y], pixels[i, j]

    
    img.save(output_path)


encrypt_image('input_image.png', 'encrypted_image.png', key=12345)
decrypt_image('encrypted_image.png', 'decrypted_image.png', key=12345)