# -*- coding: utf-8 -*-
from PIL import Image, ImageTk, ImageDraw
from tkinter import *
from funcions import CustomTitleBar


class HomePage(Tk):
    def __init__(self):
        super().__init__()
        self.title_bar = None
        self.config(bg="#202020")
        self.wm_attributes("-transparentcolor", "#202020")
        self.screen_width = int((self.winfo_screenwidth() / 8) * 5)
        self.screen_height = int((self.winfo_screenheight() / 8) * 6)
        self.x = (self.winfo_screenwidth() - self.screen_width) / 2
        self.y = (self.winfo_screenheight() - self.screen_height) / 2
        self.geometry(f"{self.screen_width}x{self.screen_height}+{int(self.x)}+{int(self.y)}")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def New_U_img(self, input_image_path):
        border_size = 3
        img = Image.open(input_image_path).convert("RGBA")
        root = Tk()
        screen_width = root.winfo_screenwidth()
        root.destroy()
        new_size = screen_width // 8
        img = img.resize((new_size, new_size))
        mask = Image.new('L', (new_size, new_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, new_size, new_size), fill=255)
        output = Image.new('RGBA', (new_size, new_size))
        output.paste(img, (0, 0), mask=mask)
        border_color = (0, 0, 0, 255)
        bordered_img = Image.new('RGBA', (new_size + 2 * border_size, new_size + 2 * border_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(bordered_img)
        draw.ellipse((0, 0, new_size + 2 * border_size, new_size + 2 * border_size), fill=border_color)
        bordered_img.paste(output, (border_size, border_size), mask=mask)
        bordered_img.save(f"imgs/U_info/U_{0+1}/U_img.png")

    def Start(self):
        self.overrideredirect(True)
        self.title_bar = CustomTitleBar(self, "DI_Configurations", "imgs/icons/config_icon.png")
        self.update_idletasks()
        self.title_bar.place(x=0, y=0, height=self.title_bar.right_corner_icon.height(), width=self.winfo_width())
        self.mainloop()


if __name__ == "__main__":
    Configurer = HomePage()
    Configurer.Start()
