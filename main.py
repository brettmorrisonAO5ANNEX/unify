import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class ImageUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Uploader")

        self.image_label = tk.Label(self.root)
        self.image_label.pack(padx=20, pady=20)

        self.upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(padx=20, pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        
        if file_path:
            image = cv2.imread(file_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            height, width, channel = image.shape
            image = cv2.resize(image, (width//10, height//10))

            self.photo = ImageTk.PhotoImage(image=Image.fromarray(image))
            self.image_label.config(image=self.photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageUploaderApp(root)
    root.mainloop()
