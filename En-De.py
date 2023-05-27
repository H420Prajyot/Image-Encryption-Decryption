from tkinter import filedialog
from PIL import Image
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt
import tkinter as tk

# Encryption parameters
salt = b'\x9a\xf2\x9d\xcbWu\xeb,\xad\x94\xb6\x0f\x88\x92C'

def derive_key(password):
    # Derive a 256-bit key from the password using scrypt key derivation function
    key = scrypt(password, salt, key_len=32, N=2**14, r=8, p=1)
    return key

def encrypt_image():
    # Select an image file to encrypt
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])

    if file_path:
        # Load the image
        image = Image.open(file_path)
        image_data = image.tobytes()

        # Prompt the user for a password
        password = tk.simpledialog.askstring("Password", "Enter a password", show='*')

        if not password:
            status_label["text"] = "Password not entered."
            return

        # Derive the encryption key from the password
        key = derive_key(password)

        # Create an AES cipher object with the encryption key
        cipher = AES.new(key, AES.MODE_ECB)

        # Perform encryption on the image data
        encrypted_data = cipher.encrypt(image_data)

        # Save the encrypted image
        save_path = filedialog.asksaveasfilename(defaultextension=".enc",
                                                 filetypes=[("Encrypted image files", "*.enc")])
        if save_path:
            encrypted_image = Image.frombytes(image.mode, image.size, encrypted_data)
            encrypted_image.save(save_path, format="PNG")  # Specify the file format explicitly
            status_label["text"] = "Image encrypted and saved successfully!"

def decrypt_image():
    # Select an encrypted image file to decrypt
    file_path = filedialog.askopenfilename(filetypes=[("Encrypted image files", "*.enc")])

    if file_path:
        # Prompt the user for the password
        password = tk.simpledialog.askstring("Password", "Enter the password", show='*')

        if not password:
            status_label["text"] = "Password not entered."
            return

        try:
            # Load the encrypted image
            encrypted_image = Image.open(file_path)
            encrypted_data = encrypted_image.tobytes()

            # Derive the decryption key from the password
            key = derive_key(password)

            # Create an AES cipher object with the decryption key
            cipher = AES.new(key, AES.MODE_ECB)

            # Decrypt the image data
            decrypted_data = cipher.decrypt(encrypted_data)

            # Create a new PIL image from the decrypted data
            decrypted_image = Image.frombytes(encrypted_image.mode, encrypted_image.size, decrypted_data)

            # Save the decrypted image
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                decrypted_image.save(save_path)
                status_label["text"] = "Image decrypted and saved successfully!"
        except ValueError as e:
            status_label["text"] = f"Decryption error: {str(e)}"
        except Exception as e:
            status_label["text"] = f"An error occurred during decryption: {str(e)}"

# Create the main window
window = tk.Tk()
window.title("Image Encryption/Decryption")
window.geometry("300x150")

# Create buttons for encryption and decryption
encrypt_button = tk.Button(window, text="Encrypt Image", command=encrypt_image)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(window, text="Decrypt Image", command=decrypt_image)
decrypt_button.pack(pady=10)

# Create a label for status messages
status_label = tk.Label(window, text="")
status_label.pack()

# Start the GUI event loop
window.mainloop()
