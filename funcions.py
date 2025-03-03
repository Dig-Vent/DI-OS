# -*- coding: utf-8 -*-
from DI_Calendar import *
import _tkinter
import csv
from PIL import Image, ImageTk, ImageFilter
from datetime import datetime
import windows
import os


class AnimatedGIFLabel:
    def __init__(self, root, label, width, height):
        self.root = root
        self.width = width
        self.height = height
        self.gif_image = Image.open("imgs/animations/loading.gif")
        self.current_frame = 0
        self.gif_frames = []
        self.load_gif_frames()
        self.label = label
        self.label.config(bg="#7E0CB9")
        self.update_label()

    def load_gif_frames(self):
        try:
            while True:
                frame = self.gif_image.copy().resize((self.width, self.height))
                self.gif_frames.append(ImageTk.PhotoImage(frame))
                self.gif_image.seek(len(self.gif_frames))
        except EOFError:
            pass

    def update_label(self):
        self.label.config(image=self.gif_frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        self.root.after(40, self.update_label)


class OperatingSystem:
    def __init__(self):
        self.monitors = None
        self.U_name = None
        self.atached_apps_path = []
        self.atached_apps_img = []
        self.activ_U_img = None
        self.activ_U_name = None
        self.U_home = 0
        self.U___ = []
        self.P___ = []
        self.activ_U_wp = None
        self.window = None
        self.screen_width = None
        self.rx = 0.5
        self.btn_list = []
        self.full_list = []
        self.labels = []
        self.btn_height = 0
        ###
        self.U_img_w = None
        self.U_img = None
        self.U_img_label = None
        self.Q_S_label = None
        self.Q_S_window = None
        self.Q_S_funcions_button = None
        self.opt_w_info = False
        self.opt_w = None
        self.opt_bt_image = None
        self.height____ = None
        self.square_size = None
        self.h_image_label = None
        self.pass_image = None
        self.pass_label = None
        self.main_clock = None
        self.monitor = None
        self.L_st = None
        self.L_nd = None
        self.L_rd = None
        self.L_th = None
        self.L_fth = None
        self.U_st = None
        self.U_nd = None
        self.U_rd = None
        self.U_th = None
        self.U_fth = None
        self.leave_label = None
        self.tk_img = None
        self.bg_label = None
        self.label_U = None
        self.sub_label = None
        self.pass_box = None
        self.submit_button = None
        self.show_hide = None
        self.L_U_S = None
        self.L_U_S_R = None
        self.bg_image = None
        self.painel_img = None
        self.label_U_name = None
        self.btn_img = None
        self.image_S = Image.open("imgs/L_U_S.png")
        self.image_S = self.image_S.resize((int(self.image_S.width * 1.5), int(self.image_S.height * 1.5)))
        self.image_S_R = Image.open("imgs/L_U_S_R.png")
        self.image_S_R = self.image_S_R.resize((int(self.image_S_R.width * 1.5), int(self.image_S_R.height * 1.5)))
        self.h_image = Image.open("imgs/hexagono_img.png")
        self.Q_S_image = None
        self.Ust_img = None
        self.Und_img = None
        self.Urd_img = None
        self.Uth_img = None
        self.Ufth_img = None

    def load_apps_name_and_img(self):
        with open('csv_info/quick_bar_img_path.csv', newline='') as csvfile_apps:
            reader_apps = csv.reader(csvfile_apps, delimiter=';', quotechar='"')
            for column, row in enumerate(reader_apps):
                if column == 0:
                    self.atached_apps_img.append(row[0])
                if column == 1:
                    self.atached_apps_img.append(row[0])
                if column == 2:
                    self.atached_apps_img.append(row[0])
                if column == 3:
                    self.atached_apps_img.append(row[0])
                if column == 4:
                    self.atached_apps_img.append(row[0])

        with open('csv_info/quick_bar_app_path.csv', newline='') as csvfile_apps:
            reader_apps = csv.reader(csvfile_apps, delimiter=';', quotechar='"')
            for column, row in enumerate(reader_apps):
                if column == 0:
                    self.atached_apps_path.append(row[0])
                if column == 1:
                    self.atached_apps_path.append(row[0])
                if column == 2:
                    self.atached_apps_path.append(row[0])
                if column == 3:
                    self.atached_apps_path.append(row[0])
                if column == 4:
                    self.atached_apps_path.append(row[0])

    def name_and_img(self):
        self.activ_U_name = self.U___[self.U_home]
        if os.path.isfile(f"imgs/U_info/U_{self.U_home + 1}/U_img.png"):
            self.activ_U_img = f"imgs/U_info/U_{self.U_home + 1}/U_img.png"
        else:
            self.activ_U_img = "imgs/U_info/default/U_img.png"
        if os.path.isfile(f"imgs/U_info/U_{self.U_home + 1}/wallpaper.png"):
            self.activ_U_wp = f"imgs/U_info/U_{self.U_home + 1}/wallpaper.png"
        else:
            self.activ_U_wp = "imgs/U_info/default/wallpaper.png"

    def verify(self, event):
        if self.P___[self.U_home] != '':
            password = self.pass_box.get()
        else:
            password = self.P___[self.U_home]
        if self.P___[self.U_home] == password:
            self.bg_label.unbind("<Button-1>")
            delete_widgets(self.full_list)
            self.U_img_w.destroy()
            self.full_list = []
            windows.home(self)
            return
        else:
            self.U_name.set("Wrong password")
            self.label_U.config(fg="red")
            self.label_U.place_forget()
            self.label_U.place(relx=0.5, rely=0.525, anchor=CENTER)
            self.label_U.after(2000, lambda: self.label_U.config(fg="white"))
            self.label_U.after(2000, lambda: self.U_name.set(f"#_{self.activ_U_name}_#"))

    def clock(self, clock_ID, digits, previous_time):
        try:
            current_time = datetime.now().strftime("%H:%M")
            if previous_time != current_time:
                width = clock_ID.winfo_reqwidth() / 14
                height = clock_ID.winfo_reqheight() / 3
                add_rx = width * 2 / clock_ID.winfo_reqwidth()
                try:
                    for digit in digits:
                        digit.destroy()
                        digits.remove(digit)
                except KeyboardInterrupt:
                    for digit in digits:
                        digit.close()
                        digits.remove(digit)

                leters = list(current_time)
                digits = []
                h = -2

                for leter in leters:
                    if leter == ":":
                        leter = "ç"
                    l_img = Image.open(f"imgs/l_and_n/{leter}.png")
                    l_img = l_img.resize((int(width), int(height)))
                    l_img = ImageTk.PhotoImage(l_img)
                    l_label = Label(clock_ID, image=l_img, bg="black")
                    l_label.place(relx=0.5 + h * add_rx, rely=0.5, anchor="center")
                    h += 1
                    digits.append(l_label)
                    digits.append(l_img)
            self.window.after(500, lambda: self.clock(clock_ID, digits, current_time))
        except _tkinter.TclError:
            pass

    def lock_creen(self):
        self.main_clock = Toplevel(self.window)
        self.main_clock.lift()
        self.main_clock.wm_attributes("-topmost", True)
        self.main_clock.wm_attributes("-transparentcolor", "white")
        self.main_clock.overrideredirect(True)
        self.h_image = ImageTk.PhotoImage(self.h_image)
        self.main_clock.geometry(f"{int(self.window.winfo_screenwidth() / 14)}x{int(self.window.winfo_screenheight() / 28)}+{int((self.window.winfo_screenwidth() - self.h_image.width())/2)}+{int(self.window.winfo_screenheight()/2.4)}")
        self.main_clock.bind("<Button-1>", lambda event: self.move(self.main_clock))
        self.window.bind("<Button-1>", lambda event: self.move(self.main_clock))
        self.window.bind("<Return>", lambda event: self.move(self.main_clock))

        self.h_image_label = Label(self.main_clock, image=self.h_image, width=int(self.window.winfo_screenwidth() / 14), height=int(self.window.winfo_screenheight() / 28), bg="white")
        self.h_image_label.pack()

        self.clock(self.h_image_label, [], "")
        self.window.focus_set()

    def new_position(self, id, final_y, times, time_break, final_command):
        if times != 0:
            new_y = id.winfo_y() - (id.winfo_y() - final_y) / times
            id.geometry(f"{int(id.winfo_width())}x{int(id.winfo_height())}+{int(id.winfo_x())}+{int(new_y)}")
            self.window.after(time_break, lambda: self.new_position(id, final_y, times - 1, time_break, final_command))
        else:
            if final_command:
                final_command()
            else:
                pass

    def move(self, clockID):
        self.window.unbind("<Button-1>")
        self.window.unbind("<Return>")
        self.main_clock.unbind("<Button-1>")

        self.new_position(clockID, 0, 20, 3, self.U_interface)

        self.name_and_img()
        self.U_name = StringVar()
        self.U_int_imgs()
        self.U_name.set(f"#_{self.activ_U_name}_#")
        self.label_U = Label(self.window, textvariable=self.U_name, font=("strong", 10), fg="white", bg="#002957")
        self.sub_label = Label(self.window, image=self.btn_img, bg="#002957")
        self.submit_button = Label(self.sub_label, text="Login", bg="black", fg="white")
        self.pass_label = Label(self.window, image=self.pass_image, bg="#002957", width=self.pass_image.width(), height=self.pass_image.height())
        self.pass_box = Entry(self.pass_label, show="*", bg="#FEBD00", width=int(self.pass_image.width() / 9), fg="blue")

    def New_U_int(self, U_number):
        self.U_home = U_number
        self.name_and_img()

        if self.P___[self.U_home] == '':
            for widget in self.full_list:
                widget.place_forget()
            self.label_U.place(relx=0.5, rely=0.525, anchor=CENTER)
            self.bg_label.unbind("<Button-1>")
            self.bg_label.bind("<Button-1>", self.verify)
            self.U_name.set("Click anywhere")
            self.full_list = []
            self.full_list.append(self.label_U)
        else:
            for widgets in self.btn_list:
                widgets.place_forget()
            self.place_bind()
            tk_img = Image.open(self.activ_U_img)
            tk_img = tk_img.resize((200, 200))
            self.tk_img = ImageTk.PhotoImage(tk_img)
            self.label_U.place_forget()
            self.label_U.place(relx=0.5, rely=0.525, anchor=CENTER)
            self.label_U.config(fg="white")
            self.U_name.set(f"#_{self.activ_U_name}_#")
            self.pass_box.delete(0, 'end')
            self.window.after(100, self.pass_box.focus)
        self.U_img = Image.open(self.activ_U_img)
        self.U_img = ImageTk.PhotoImage(self.U_img)
        self.U_img_label.config(image=self.U_img, bg="white")

    def place_bind(self):
        list_btn = []
        for btn in self.btn_list:
            list_btn.append(btn)
        activ_U = list_btn.pop(self.U_home * 2)
        activ_L = list_btn.pop(self.U_home * 2)
        i = 0
        for btn in list_btn:
            if int(list_btn.index(btn) % 2) == 0:
                btn.place(relx=0.2, rely=((1-4*self.btn_height/self.window.winfo_screenheight())/2.5 + (self.btn_height/self.window.winfo_screenheight()) * 1.16 * i), anchor='center')
                if int(list_btn.index(btn)) / 2 >= self.U_home:
                    btn.bind("<Button-1>", lambda event, idx=int(list_btn.index(btn) / 2 + 1): self.New_U_int(idx))
                else:
                    btn.bind("<Button-1>", lambda event, idx=int(list_btn.index(btn) / 2): self.New_U_int(idx))
                i += 1
            else:
                btn.place(relx=self.rx, rely=self.rx, anchor='center')
                if int(list_btn.index(btn)) / 2 >= self.U_home:
                    btn.bind("<Button-1>", lambda event, idx=int(list_btn.index(btn) / 2 + 1): self.New_U_int(idx))
                else:
                    btn.bind("<Button-1>", lambda event, idx=int(list_btn.index(btn) / 2): self.New_U_int(idx))

    def U_int_imgs(self):
        self.Ust_img = Image.open("imgs/Ust.png")
        self.Und_img = Image.open("imgs/Und.png")
        self.Urd_img = Image.open("imgs/Urd.png")
        self.Uth_img = Image.open("imgs/Uth.png")
        self.Ufth_img = Image.open("imgs/Ufth.png")
        self.bg_image = Image.open("imgs/lock_wallpaper.png")
        self.screen_width = int(self.bg_image.width * (self.window.winfo_screenheight() / self.bg_image.height))
        self.painel_img = Image.open("imgs/painel_U_int.png")
        self.painel_img = self.painel_img.resize((int(self.screen_width/1.7), int(self.window.winfo_screenheight()/1.7)))
        self.painel_img = ImageTk.PhotoImage(self.painel_img)
        self.tk_img = Image.open(self.activ_U_img)
        self.tk_img = self.tk_img.resize((200, 200))
        self.tk_img = ImageTk.PhotoImage(self.tk_img)
        self.label_U_name = Image.open("imgs/U_label_img.png")
        self.label_U_name = self.label_U_name.resize((int(self.screen_width/150*15), int(self.window.winfo_screenheight()/21)))
        self.label_U_name = ImageTk.PhotoImage(self.label_U_name)
        self.btn_img = Image.open("imgs/btn_normal.png")
        self.btn_img = self.btn_img.resize((int(self.btn_img.width * 1.2), int(self.btn_img.height * 1.2)))
        self.btn_img = ImageTk.PhotoImage(self.btn_img)
        self.pass_image = Image.open("imgs/pass_entry.png")
        self.pass_image = self.pass_image.resize((int(self.window.winfo_screenwidth() / 11), int((self.pass_image.height / self.pass_image.width) * self.window.winfo_screenwidth() / 16)))
        self.pass_image = ImageTk.PhotoImage(self.pass_image)
        self.L_U_S = ImageTk.PhotoImage(self.image_S)
        self.L_U_S_R = ImageTk.PhotoImage(self.image_S_R)
        num = 7
        self.Ust_img = self.Ust_img.resize((int(self.window.winfo_screenwidth()/num), int(((self.window.winfo_screenwidth()/num)/self.Ust_img.width)*self.Ust_img.height)))
        self.Ust_img = ImageTk.PhotoImage(self.Ust_img)
        self.Und_img = self.Und_img.resize((int(self.window.winfo_screenwidth()/num), int((self.window.winfo_screenwidth()/num)/self.Und_img.width*self.Und_img.height)))
        self.Und_img = ImageTk.PhotoImage(self.Und_img)
        self.Urd_img = self.Urd_img.resize((int(self.window.winfo_screenwidth()/num), int((self.window.winfo_screenwidth()/num)/self.Urd_img.width*self.Urd_img.height)))
        self.Urd_img = ImageTk.PhotoImage(self.Urd_img)
        self.Uth_img = self.Uth_img.resize((int(self.window.winfo_screenwidth()/num), int((self.window.winfo_screenwidth()/num)/self.Uth_img.width*self.Uth_img.height)))
        self.Uth_img = ImageTk.PhotoImage(self.Uth_img)
        self.Ufth_img = self.Ufth_img.resize((int(self.window.winfo_screenwidth()/num), int((self.window.winfo_screenwidth()/num)/self.Ufth_img.width*self.Ufth_img.height)))
        self.Ufth_img = ImageTk.PhotoImage(self.Ufth_img)
        self.btn_height = self.Ust_img.height()

    def display_U_img(self):
        self.U_img_w = Toplevel(self.window)
        self.U_img_w.lift()
        self.U_img_w.wm_attributes("-topmost", True)
        self.U_img_w.wm_attributes("-transparentcolor", "white")
        self.U_img_w.overrideredirect(True)
        self.U_img_w.config(bg="white")
        self.U_img = Image.open(self.activ_U_img)
        self.U_img = ImageTk.PhotoImage(self.U_img)
        self.U_img_label = Label(self.U_img_w, image=self.U_img, bg="white")
        self.U_img_label.pack()
        self.U_img_w.geometry(f"{self.U_img.width()}x{self.U_img.height()}+{int((self.window.winfo_screenwidth() - self.U_img.width()) / 2)}+{int((self.window.winfo_screenheight() - self.U_img.height()) / 3)}")

    def U_interface(self):
        self.display_U_img()
        if self.P___[self.U_home] == '':
            print("a")
            self.bg_label.unbind("<Button-1>")
            self.bg_label.bind("<Button-1>", self.verify)
            self.U_name.set("Click anywhere")
            self.label_U.place(relx=0.5, rely=0.525, anchor=CENTER)
            self.full_list.append(self.label_U)
        else:
            self.window.after(100, self.pass_box.focus)
            self.bg_image = Image.open("imgs/lock_wallpaper.png")
            self.bg_image = self.bg_image.filter(ImageFilter.GaussianBlur(radius=20))
            self.bg_image = self.bg_image.resize((self.screen_width, self.window.winfo_screenheight()))
            self.bg_image = ImageTk.PhotoImage(self.bg_image)
            self.bg_label.config(image=self.bg_image)
            self.label_U.place(relx=0.5, rely=0.525, anchor=CENTER)
            self.sub_label.place(relx=0.5, rely=0.65, anchor=CENTER)
            self.submit_button.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.pass_label.place(relx=0.5, rely=0.58, anchor=CENTER)
            self.pass_box.place(relx=0.5, rely=0.5, anchor=CENTER)

            def focusin(label, bt):
                label.config(image=self.L_U_S_R)
                label.image = self.L_U_S_R
                bt.config(bg="#880015")

            def focusout(label, bt):
                label.config(image=self.L_U_S)
                bt.config(bg="#002957")

            self.U_st = Label(self.window, image=self.Ust_img, width=self.Ust_img.width(), height=self.Ust_img.height(), bg="#002957")
            self.L_st = Label(self.U_st, text=f">>{self.U___[0]}<<", bg="#0F0D25", fg="red")
            self.btn_list = [self.U_st, self.L_st]

            if len(self.U___) > 1:
                self.U_nd = Label(self.window, image=self.Und_img, width=self.Und_img.width(), height=self.Und_img.height(), bg="#002957")
                self.L_nd = Label(self.U_nd, text=f">>{self.U___[1]}<<", bg="#0F0D25", fg="red")
                self.btn_list.append(self.U_nd)
                self.btn_list.append(self.L_nd)

            if len(self.U___) > 2:
                self.U_rd = Label(self.window, image=self.Urd_img, width=self.Urd_img.width(), height=self.Urd_img.height(), bg="#002957")
                self.L_rd = Label(self.U_rd, text=f">>{self.U___[2]}<<", bg="#0F0D25", fg="red")
                self.btn_list.append(self.U_rd)
                self.btn_list.append(self.L_rd)

            if len(self.U___) > 3:
                self.U_th = Label(self.window, image=self.Uth_img, width=self.Uth_img.width(), height=self.Uth_img.height(), bg="#002957")
                self.L_th = Label(self.U_th, text=f">>{self.U___[3]}<<", bg="#0F0D25", fg="red")
                self.btn_list.append(self.U_th)
                self.btn_list.append(self.L_th)

            if len(self.U___) > 4:
                self.U_fth = Label(self.window, image=self.Ufth_img, width=self.Ufth_img.width(), height=self.Ufth_img.height(), bg="#002957")
                self.L_fth = Label(self.U_fth, text=f">>{self.U___[4]}<<", bg="#0F0D25", fg="red")
                self.btn_list.append(self.U_fth)
                self.btn_list.append(self.L_fth)

            self.place_bind()

            show_img = Image.open("imgs/show_img.png")
            show_img = show_img.resize((int(self.window.winfo_screenwidth() / 35), int(self.window.winfo_screenheight() / 35)))
            show_img = ImageTk.PhotoImage(show_img)
            hide_img = Image.open("imgs/hide_img.png")
            hide_img = hide_img.resize((int(self.window.winfo_screenwidth() / 35), int(self.window.winfo_screenheight() / 35)))
            hide_img = ImageTk.PhotoImage(hide_img)

            def show_hide_f(event):
                if self.show_hide.image == hide_img:
                    self.show_hide.config(image=show_img)
                    self.show_hide.image = show_img
                    self.pass_box.configure(show="")
                else:
                    self.show_hide.configure(image=hide_img)
                    self.show_hide.image = hide_img
                    self.pass_box.configure(show="*")

            self.show_hide = Label(self.window, image=hide_img, width=hide_img.width(), height=hide_img.height(), bg="#002957")
            self.show_hide.image = hide_img
            self.show_hide.place(relx=0.57, rely=0.58, anchor="center")
            self.full_list = [self.pass_box, self.pass_label, self.label_U, self.show_hide, self.sub_label] + self.btn_list
            self.pass_box.bind("<Return>", self.verify)
            self.submit_button.bind("<Button-1>", self.verify)
            self.sub_label.bind("<Button-1>", self.verify)
            self.show_hide.bind("<Button-1>", show_hide_f)
            self.bg_label.bind("<Button-1>", lambda event: self.pass_label.focus_force())
            self.label_U.bind("<Button-1>", lambda event: self.pass_label.focus_force())
            self.window.mainloop()

    def create_new_user(self, x, y, Win, w):
        if all(char == ' ' for char in x) or x == "":
            w_p = Label(Win, text=f"No user name detected!", font="normal 12", fg="red")
            w_p.grid(columnspan=2, row=2, sticky=W, padx=5, pady=5)
            Win.after(2000, w_p.destroy)
        elif len(x) > 11:
            w_p = Label(Win, text="Tha maximus caracters for a name is 11!", font="normal 12", fg="red")
            w_p.grid(columnspan=2, row=2, sticky=W, padx=5, pady=5)
            Win.after(2000, w_p.destroy)
        elif all(char == ' ' for char in y) or y == "":
            w_p = Label(Win, text=f"No password detected!!", font="normal 12", fg="red")
            w_p.grid(columnspan=2, row=2, sticky=W, padx=5, pady=5)
            Win.after(2000, w_p.destroy)
        elif ";" in y:
            w_p = Label(Win, text=f"You can't use ';' in the password!", font="normal 12", fg="red")
            w_p.grid(columnspan=2, row=2, sticky=W, padx=5, pady=5)
            Win.after(2000, w_p.destroy)
        else:
            with open('csv_info/login.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=';')
                csv_writer.writerow([x, y])

            windows_list = [Win, w]
            delete_widgets(windows_list)
            self.U_home = 0

    def done(self):
        print("done")

    def Q_S(self, monitor):
        self.monitor = monitor
        self.Q_S_window = Toplevel(self.window)
        self.Q_S_window.lift()
        self.Q_S_window.wm_attributes("-topmost", True)
        self.Q_S_window.wm_attributes("-transparentcolor", "white")
        self.Q_S_window.overrideredirect(True)
        self.Q_S_image = Image.open("imgs/Q_S.png")
        self.height____ = int((self.Q_S_image.height * int(monitor.width / 5)) / self.Q_S_image.width)
        self.Q_S_image = self.Q_S_image.resize((int(monitor.width / 5), self.height____))
        self.Q_S_image = ImageTk.PhotoImage(self.Q_S_image)
        self.Q_S_window.geometry(f"{int(monitor.width / 5)}x{self.height____}+{int(monitor.x + ((monitor.width - monitor.width / 5) / 2))}+{int(monitor.y - monitor.height / 3)}")
        self.Q_S_window.config(bg="black")
        self.Q_S_label = Label(self.Q_S_window, image=self.Q_S_image, width=int(monitor.width / 5), height=self.height____, bg="white")
        self.Q_S_label.pack()

        def options(event):
            if self.opt_w_info is False:
                self.opt_w_info = True
                self.opt_w = windows.on_off_options(self.window, self, Q_S_close)
            elif self.opt_w_info is True:
                self.opt_w_info = False
                self.opt_w.destroy()
            else:
                exit(print("error on options (self.opt_w_info nor true nor false)"))

        self.square_size = int(self.height____ / 5)
        self.opt_bt_image = Image.open("imgs/power_button.png")
        self.opt_bt_image = self.opt_bt_image.resize((self.square_size, self.square_size))
        self.opt_bt_image = ImageTk.PhotoImage(self.opt_bt_image)
        self.Q_S_funcions_button = Label(self.Q_S_label, bg="white", width=self.square_size, height=self.square_size, image=self.opt_bt_image)
        self.Q_S_funcions_button.place(x=int(self.Q_S_label.winfo_reqwidth() - (self.square_size/2)), y=self.square_size/2, anchor="ne", width=self.square_size, height=self.square_size)
        self.Q_S_funcions_button.bind("<Button-1>", options)

        def Q_S_open(event):
            self.Q_S_window.focus_set()
            self.new_position(self.main_clock, int(self.monitor.y - self.main_clock.winfo_height()), 60, 8, self.Q_S_open)

        def Q_S_close(event=None):
            self.new_position(self.Q_S_window, int(self.monitor.y - self.Q_S_window.winfo_height()), 62, 4, self.Q_S_close)

        self.main_clock.bind("<Button-1>", Q_S_open)
        self.Q_S_window.bind("<FocusOut>", Q_S_close)

    def Q_S_open(self):
        self.new_position(self.Q_S_window, self.monitor.y, 62, 4, None)

    def Q_S_close(self):
        self.new_position(self.main_clock, self.monitor.y, 60, 8, None)



###


def set_sized_bg_img(master, img_path, width, height):
    image = PhotoImage(file=img_path)
    image.configure(height=height, width=width)
    bg_label = Label(master, image=image)
    bg_label.pack()


def deselect(event):
    try:
        event.widget.focus_set()
    except AttributeError:
        pass


def delete_widgets(widgets_list):
    for objects in widgets_list:
        objects.destroy()


def see_rows():
    with open('csv_info/login.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        return rows


def nevoa(img):
    img.putalpha(int(255 * 0.5))
    return img
