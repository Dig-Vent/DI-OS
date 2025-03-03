from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import *
from DI_Configurations import CustomTitleBar


class DI_Files(Tk):
    def __init__(self):
        super().__init__()
        self.config(bg="#202020")
        self.overrideredirect(True)
        self.geometry("600x400+1100+400")
        self.wm_attributes("-transparentcolor", "#202020")
        img = Image.open("imgs/icons/config_icon.png")
        self.icon = ImageTk.PhotoImage(img)
        self.iconphoto(False, self.icon)

        img = Image.open("imgs/File.png").resize((24, 24))
        self.file_icon = ImageTk.PhotoImage(img)
        img = Image.open("imgs/Folder.png").resize((24, 24))
        self.folder_icon = ImageTk.PhotoImage(img)

        self.Titlebar = CustomTitleBar(self, "DI_Files", "imgs/icons/config_icon.png")
        self.update_idletasks()
        self.Titlebar.place(x=0, y=0, height=self.Titlebar.right_corner_icon.height(), width=self.winfo_width())

        self.search_entry = CTkEntry(self.Titlebar, bg_color="transparent", placeholder_text="Path",
                                placeholder_text_color="#B3B3B3", fg_color="#292929", border_width=0,
                                text_color="#B3B3B3", corner_radius=7, width=250)
        self.search_entry.pack(side="left", expand=True)
        self.search_entry.insert(0, string=r"MyFiles\ ")
        self.search_entry.delete(len(self.search_entry.get()) - 1, "end")

        self.tree = ttk.Treeview(self, columns=("Name",), show="tree")
        self.tree.place(x=0, y=50, width=self.winfo_width())
        self.last_adress = None

        self.tree.bind("<Double-Button-1>", self.on_item_double_click)
        self.search_entry.bind("<Return>", lambda event: self.load_files(self.search_entry.get()))

        self.load_files()

        self.mainloop()

    def on_item_double_click(self, event):
        selected_item = self.tree.focus()
        item_text = self.tree.item(selected_item, "text")
        if item_text == ".":
            item_text = os.path.dirname(os.path.normpath(self.search_entry.get()))
            self.search_entry.delete(0, "end")
            self.search_entry.insert("end", string=fr"{item_text}\ ")
            self.search_entry.delete(len(self.search_entry.get()) - 1, "end")
            self.load_files()
        elif item_text != "":
            if os.path.isdir(f"{self.search_entry.get()}/{item_text}"):
                self.search_entry.insert("end", string=fr"{item_text}\ ")
                self.search_entry.delete(len(self.search_entry.get()) - 1, "end")
                self.load_files()
            else:
                print("file")

    def load_files(self, path=None):
        if path and not os.path.exists(path):
            self.search_entry.delete(0, "end")
            self.search_entry.insert(0, string=self.last_adress)
        else:
            if path:
                if not path.endswith("\\"):
                    self.search_entry.insert("end", string=r"\ ")
                    self.search_entry.delete(len(self.search_entry.get()) - 1, "end")
            self.tree.delete(*self.tree.get_children())
            if len(self.search_entry.get()) != 8:
                img = self.folder_icon
                self.tree.insert("", "end", text=".", image=img if img else "")
            for item in os.listdir(f"{self.search_entry.get()}"):
                img = self.folder_icon if os.path.isdir(fr"{self.search_entry.get()}\{item}") else self.file_icon
                self.tree.insert("", "end", text=item, image=img if img else "")
            self.last_adress = self.search_entry.get()

if __name__ == "__main__":
    DI_Files_Window = DI_Files()
