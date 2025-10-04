from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)
    img.save("encrypted_image.png")
    print(" Image encrypted successfully as 'encrypted_image.png'!")

def decrypt_image(encrypted_path, key):
    img = Image.open(encrypted_path)
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)
    img.save("decrypted_image.png")
    print(" Image decrypted successfully as 'decrypted_image.png'!")

def main():
    print("=== Simple Image Encryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
    image_path = input("Enter image path: ")
    key = int(input("Enter encryption key (integer): "))
    if choice == 'e':
        encrypt_image(image_path, key)
    elif choice == 'd':
        decrypt_image(image_path, key)
    else:
        print(" Invalid choice! Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()
