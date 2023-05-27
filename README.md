# Image Encryption/Decryption

This Python program provides a graphical user interface (GUI) for encrypting and decrypting image files using the AES encryption algorithm. It uses the tkinter library for the GUI components and the PIL (Python Imaging Library) library for image manipulation.

## Features

- Encrypts image files with a password-based encryption algorithm.
- Decrypts encrypted image files using the same password.
- Supports PNG, JPG, and JPEG image file formats.

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- Pillow (Python Imaging Library)

## Installation

1. Clone the repository or download the source code files.
2. Install the required libraries by running the following command:
```
pip install tkinter
pip install pillow
pip install pycryptodome
```

## Usage

1. Run the program using the following command:
```
python En-De.py
```

2. The GUI window will appear with two buttons: "Encrypt Image" and "Decrypt Image".

3. **Encrypting an Image**:
- Click on the "Encrypt Image" button.
- Select an image file (PNG, JPG, or JPEG) that you want to encrypt.
- Enter a password in the password prompt dialog.
- The encrypted image will be saved with the extension `.enc`.

4. **Decrypting an Encrypted Image**:
- Click on the "Decrypt Image" button.
- Select an encrypted image file (`.enc`) that you want to decrypt.
- Enter the password used for encryption in the password prompt dialog.
- The decrypted image will be saved with the original file format (PNG, JPG, or JPEG).

## Note

- This program uses a simple password input dialog for demonstration purposes. For better security, consider using a more secure and robust password input mechanism in a real application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Feel free to customize `En-De.py` file based on your specific requirements and project details. You can provide additional information, instructions, and screenshots as needed.

Happy image encryption and decryption!
