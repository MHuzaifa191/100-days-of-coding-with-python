import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")
        
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=10)
        
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack(pady=10)
        
        self.watermark_text = tk.StringVar(value="Your Watermark")
        self.entry = tk.Entry(root, textvariable=self.watermark_text, width=30)
        self.entry.pack(pady=10)
        
        self.add_watermark_btn = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.add_watermark_btn.pack(pady=10)
        
        self.save_btn = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_btn.pack(pady=10)
        
        self.image = None
        self.watermarked_image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def display_image(self, image):
        image.thumbnail((600, 400))
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(300, 200, image=self.tk_image)

    def add_watermark(self):
        if self.image:
            draw = ImageDraw.Draw(self.image)
            text = self.watermark_text.get()
            font = ImageFont.load_default()

            bbox = draw.textbbox((0, 0), text, font=font)
            textwidth, textheight = bbox[2] - bbox[0], bbox[3] - bbox[1]
            
            width, height = self.image.size
            margin = 10
            x = width - textwidth - margin
            y = height - textheight - margin

            draw.text((x, y), text, font=font)
            self.watermarked_image = self.image.copy()
            self.display_image(self.watermarked_image)
        else:
            messagebox.showwarning("Warning", "Please upload an image first.")


    def save_image(self):
        if self.watermarked_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg *.jpeg")])
            if file_path:
                self.watermarked_image.save(file_path)
                messagebox.showinfo("Info", "Image saved successfully!")
        else:
            messagebox.showwarning("Warning", "Please add a watermark first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
