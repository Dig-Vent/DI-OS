# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
from tkinter import *


class CustomTitleBar(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="black")
        self.parent = parent
        self.icon = PhotoImage(file="imgs/icons/DI.ico")
        self.close_image = PhotoImage(file="imgs/Config/close_button.png")
        self.close_image2 = PhotoImage(file="imgs/Config/close_button - 2.png")
        self.maximize_image1 = PhotoImage(file="imgs/Config/maximize_button.png")
        self.maximize_image2 = PhotoImage(file="imgs/Config/maximize_button2.png")
        self.maximize_image3 = PhotoImage(file="imgs/Config/maximize_button - 3.png")
        self.maximize_image4 = PhotoImage(file="imgs/Config/maximize_button - 4.png")
        self.minimize_image = PhotoImage(file="imgs/Config/minimize_button.png")
        self.minimize_image2 = PhotoImage(file="imgs/Config/minimize_button - 2.png")
        self.size = 35
        self.x = 0
        self.y = 0

        self.bind("<B1-Motion>", self.drag_window)
        self.bind("<Button-1>", self.start_draging_deselect)
        self.bind('<Button-3>', self.right_touch)
        self.bind("<Double-Button-1>", lambda event: self.maximize_restore_window(self.maximize_image1, self.maximize_image2))

        self.icon_l = Label(self, image=self.icon, height=self.size, width=self.size, bg="black")
        self.icon_l.pack(side="left")

        self.close_button = Label(self, image=self.close_image, height=self.size, width=self.size, bg="black")
        self.close_button.pack(side="right")
        self.close_button.bind("<Button-1>", self.close_window)
        self.close_button.bind("<Enter>", lambda _: self.L_enter1(self.close_image2))
        self.close_button.bind("<Leave>", lambda _: self.L_leave1(self.close_image))

        self.maximize_button = Label(self, image=self.maximize_image1, height=self.size, width=self.size, bg="black")
        self.maximize_button.pack(side="right")
        self.maximize_button.bind("<Button-1>", lambda event: self.maximize_restore_window(self.maximize_image1,
                                                                                           self.maximize_image2))
        self.maximize_button.bind("<Enter>", lambda _: self.L_enter2(self.maximize_image4, self.maximize_image3))
        self.maximize_button.bind("<Leave>", lambda _: self.L_leave2(self.maximize_image1, self.maximize_image2))

        self.minimize_button = Label(self, image=self.minimize_image, height=self.size, width=self.size, bg="black")
        self.minimize_button.pack(side="right")
        self.minimize_button.bind("<Button-1>", self.minimize_window)
        self.minimize_button.bind("<Enter>", lambda _: self.L_enter3(self.minimize_image2))
        self.minimize_button.bind("<Leave>", lambda _: self.L_leave3(self.minimize_image))

    def right_touch(self, event):
        def close_window(event):
            window.destroy()
        window = Tk()
        window.overrideredirect(True)
        x = window.winfo_pointerx()
        y = window.winfo_pointery()
        window.geometry(f"+{x + 10}+{y + 10}")
        window.bind("<FocusOut>", close_window)
        window.mainloop()

    def start_draging_deselect(self, event):
        event.widget.focus_set()
        self.x = event.x
        self.y = event.y

    def drag_window(self, event):
        if self.parent.state() == "zoomed":
            self.parent.state("normal")
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.parent.winfo_x() + deltax
        y = self.parent.winfo_y() + deltay
        self.parent.geometry(f"+{x}+{y}")

    def close_window(self, _):
        self.parent.quit()

    def maximize_restore_window(self, maximize_image1, maximize_image2):
        if self.parent.state() == "zoomed":
            self.parent.state("normal")
            self.maximize_button.configure(image=maximize_image1)
        else:
            self.parent.state("zoomed")
            self.maximize_button.configure(image=maximize_image2)

    def minimize_window(self, _):
        self.parent.withdraw()

    def L_enter1(self, close_image2):
        self.close_button.configure(image=close_image2)

    def L_enter2(self, maximize_image4, maximize_image3):
        if self.parent.state() == "zoomed":
            self.maximize_button.configure(image=maximize_image4)
        else:
            self.maximize_button.configure(image=maximize_image3)

    def L_enter3(self, minimize_image2):
        self.minimize_button.configure(image=minimize_image2)

    def L_leave1(self, close_image):
        self.close_button.configure(image=close_image)

    def L_leave2(self, maximize_image1, maximize_image2):
        if self.parent.state() == "zoomed":
            self.maximize_button.configure(image=maximize_image2)
        else:
            self.maximize_button.configure(image=maximize_image1)

    def L_leave3(self, minimize_image):
        self.minimize_button.configure(image=minimize_image)


def deselect(event):
    event.widget.focus_set()


class HomePage(Tk):
    def __init__(self):
        super().__init__()
        self.title_bar = None
        self.screen_width = int((self.winfo_screenwidth() / 8) * 7)
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
        bordered_img.save(f"imgs/Temp/U_{0+1}/U_img.png")

    def Start(self):
        self.overrideredirect(True)
        self.title_bar = CustomTitleBar(parent=self)
        self.title_bar.grid(row=0, columnspan=2, sticky="ew")
        self.mainloop()


if __name__ == "__main__":
    Configurer = HomePage()
    Configurer.Start()
