# -*- coding: utf-8 -*-

from screeninfo import get_monitors
from tkinter import ttk
from time import sleep
from funcions import *
import pyautogui


def U_create(OS, w, btn):
    window = Tk()
    window.title("")
    window.geometry(f"{int(window.winfo_screenwidth()/4)}x{int(window.winfo_screenheight()/7)}")
    window.bind('<Button-1>', deselect)
    window.attributes("-toolwindow", True)
    window.attributes("-topmost", True)

    def on_close():
        btn.put()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.columnconfigure(0)
    window.columnconfigure(1)

    def h(event):
        E_p.focus()

    def x(event):
        OS.create_new_user(E_u.get(), E_p.get(), window, w)

    login_button = ttk.Button(window, text="Create user", command=lambda: OS.create_new_user(E_u.get(), E_p.get(), window, w))
    login_button.place(anchor=SE, relx=(window.winfo_width()-window.winfo_width()/40), rely=(window.winfo_height()-window.winfo_height()/15))
    password_label = ttk.Label(window, text="New password:", font=0.009765625*window.winfo_screenwidth())
    password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)
    E_p = ttk.Entry(window, font=0.009765625*window.winfo_screenwidth())
    E_p.grid(column=1, row=1, sticky=E, padx=5, pady=5)
    E_p.bind("<Return>", x)
    username_label = ttk.Label(window, text="New username:", font=0.009765625*window.winfo_screenwidth())
    username_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)
    E_u = ttk.Entry(window, font=0.009765625*window.winfo_screenwidth())
    E_u.grid(column=1, row=0, sticky=E, padx=5, pady=5)
    E_u.bind("<Return>", h)
    window.mainloop()


def welcome(OS):
    window = Tk()
    window.title("")
    window.attributes("-fullscreen", True)
    window.protocol("WM_DELETE_WINDOW")
    btn_hello = ttk.Button(window, text="Hello")
    btn_hello.place(relx=0.5, rely=0.5, anchor=CENTER)
    btn_hello.config(command=lambda: (btn_hello.place_forget(), U_create(OS, window, btn_hello)))
    window.mainloop()


def login(OS):
    window = Tk()
    window.title("")
    window.config(bg="#0D2131")
    window.overrideredirect(True)
    window.bind('<Button-1>', deselect)
    window.protocol("WM_DELETE_WINDOW")
    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}+0+0")
    image = Image.open("imgs/lock_wallpaper.png")
    image_width = int(image.width * (window.winfo_screenheight() / image.height))
    image = image.resize((image_width, window.winfo_screenheight()))
    image = ImageTk.PhotoImage(image)
    OS.bg_label = Label(window, image=image, bg="#0D2131", width=window.winfo_screenwidth(), height=window.winfo_screenheight())
    OS.bg_label.place(rely=0.5, relx=0.5, anchor=CENTER)
    OS.window = window
    OS.lock_screen()
    window.mainloop()


def home(OS):
    OS.P___ = []
    created_windows = []
    OS.monitors = get_monitors()

    monitor = OS.monitors[0]
    main_window = OS.window
    OS.bg_image = Image.open(OS.activ_U_wp)
    OS.bg_image = OS.bg_image.resize((monitor.width, monitor.height))
    OS.bg_image = ImageTk.PhotoImage(OS.bg_image)
    OS.bg_label.config(image=OS.bg_image, width=monitor.width, height=monitor.height)
    main_window.geometry(f"{monitor.width}x{monitor.height}+{monitor.x}+{monitor.y}")
    OS.main_clock.geometry(
        f"{int(main_window.winfo_screenwidth() / 14)}x{int(main_window.winfo_screenheight() / 28)}+{int(monitor.x + ((monitor.width - OS.main_clock.winfo_width()) / 2))}+{monitor.y}")
    OS.Q_S(monitor)
    created_windows.append(monitor)
    for monitor in OS.monitors:
        if monitor not in created_windows:
            window = Toplevel(main_window)
            window.title("")
            window.overrideredirect(True)
            window.protocol("WM_DELETE_WINDOW")
            bg_image = Image.open(OS.activ_U_wp)
            bg_image = bg_image.resize((monitor.width, monitor.height))
            bg_image = ImageTk.PhotoImage(bg_image)
            bg_label = Label(window, image=bg_image, width=bg_image.width(), height=bg_image.height())
            bg_label.pack()
            window.geometry(f"{monitor.width}x{monitor.height}+{monitor.x}+{monitor.y}")
            created_windows.append(monitor)
    mainloop()


def on_off_options(root, self):
    options_w = Toplevel(root, bg="white")
    options_w.overrideredirect(True)
    width = int(root.winfo_width() * 0.075)
    options_w.lift()
    options_w.wm_attributes("-topmost", True)
    options_w.wm_attributes("-transparentcolor", "white")
    x, y = pyautogui.position()
    options_w.geometry(f"{width}x{width}+{x}+{y}")
    options_image = Image.open("imgs/options.png")
    options_image = options_image.resize((width, width))
    options_w.options_image = ImageTk.PhotoImage(options_image)
    background = Label(options_w, bg="white", width=width, height=width, image=options_w.options_image)
    background.pack()

    st_dwn_btn = Label(background, text="Shutdown", width=int(width*0.8), height=int(width/4), bg="#212121", fg="white")
    st_dwn_btn.place(anchor="nw", width=int(width*0.8), height=int(width/4), x=int(width*0.1), y=int(width/16))
    st_dwn_btn.bind("<Button-1>", lambda event: (shutdown(root), options_w.destroy()))

    rst_btn = Label(background, text="Restart", width=int(width*0.8), height=int(width/4), bg="#212121", fg="white")
    rst_btn.place(anchor="nw", width=int(width*0.8), height=int(width/4), x=int(width*0.1), y=int(3*width/8))
    rst_btn.bind("<Button-1>", lambda event: restart(root, self))

    slp_btn = Label(background, text="Sleep", width=int(width * 0.8), height=int(width / 4), bg="#212121", fg="white")
    slp_btn.place(anchor="nw", width=int(width * 0.8), height=int(width / 4), x=int(width * 0.1), y=int(11*width/16))
    slp_btn.bind("<Button-1>", lambda event: (go_sleep(self), options_w.destroy()))

    def close(event):
        self.opt_w_info = False
        options_w.destroy()

    options_w.bind("<FocusOut>", close)
    return options_w


def shutdown(root):
    exit_w = Toplevel(root)
    exit_w.overrideredirect(True)
    width = int(root.winfo_width() / 2)
    height = int(root.winfo_height() / 2)
    exit_w.geometry(f"{width}x{height}+{int((root.winfo_screenwidth() - width) / 2)}+{int((root.winfo_screenheight() - height) / 2)}")
    exit_w.lift()
    exit_w.wm_attributes("-topmost", True)
    exit_id = exit_w.after(2000, root.destroy)
    cancel_btn = Button(exit_w, command=lambda: (exit_w.after_cancel(exit_id), exit_w.destroy()))
    cancel_btn.pack()


def restart(root, self):
    self.U_home = -1
    root.destroy()


def wake_up(self):
    self.bg_label.config(image=self.bg_image)
    self.window.unbind("<Button-1>")


def go_sleep(self):
    self.bg_label.config(image="", bg="black")
    self.window.bind("<Button-1>", lambda event: wake_up(self))
