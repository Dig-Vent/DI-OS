# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from customtkinter import *
import psutil


class TaskManager(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.process_info = {}
        self.left_frame = Frame(self, width="40", bg="black")
        self.top_frame = Frame(self, height="35", bg="blue")
        self.under_top_frame = Frame(self, height="35", bg="red")
        self.frame = Frame(self, height=(self.winfo_screenheight() - (20 + 20)))
        self.search_bar = CTkEntry(self.top_frame, fg_color="white", placeholder_text="Search", placeholder_text_color="black", bg_color="blue", text_color="black")
        self.scrollbar = Scrollbar(self.frame)
        self.canvas = Canvas(self.frame, yscrollcommand=self.scrollbar.set)
        self.task_frame = Frame(self.canvas)
        self.bt_end_task = ttk.Button(self.under_top_frame, text="End task", command=self.kill_process, style="Red.TButton")
        self.la = []
        self.pid = ""

    def task_manager(self):
        self.geometry("400x450")
        self.title("Tasks manager")
        self.iconphoto(True, PhotoImage(file='imgs/icons/TM.ico'))
        style = ttk.Style()
        style.configure("Red.TButton", background="red")
        self.left_frame.pack(fill=Y, anchor="w", side="left")
        self.top_frame.pack(fill="x", anchor="n", side="top")
        self.under_top_frame.pack(fill="x", anchor="n", side="top")
        self.frame.pack(fill="y", side="left")
        self.search_bar.pack(anchor="center", side=TOP)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        def on_mousewheel(event):
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

        self.bind_all("<MouseWheel>", on_mousewheel)
        self.scrollbar.configure(command=self.canvas.yview)
        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.bt_end_task.pack(side=RIGHT)

        self.task_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.left_frame.bind("<Button-1>", self.declick)
        self.top_frame.bind("<Button-1>", self.declick)
        self.under_top_frame.bind("<Button-1>", self.declick)
        self.update_list()
        self.mainloop()

    def kill_process(self):
        try:
            pud = psutil.Process(int(self.pid))
            pud.terminate()
        except psutil.NoSuchProcess:
            pass

    def declick(self, event):
        event.widget.focus_set()
        for widget in self.la:
            widget.config(bg="#F0F0F0")
        self.pid = ""
        self.bt_end_task.configure(state='disabled')

    def on_label_click(self, widget, pid):
        self.declick
        self.la.append(widget)
        widget.configure(bg="gray")
        self.pid = pid
        self.bt_end_task.configure(state='normal')

    def update_list(self):
        new_process_info = {}
        row = 0
        search_term = self.search_bar.get().lower()

        for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
            PID = process.info['pid']
            name = process.info['name']
            cpu_percent = f"{process.info['cpu_percent']}%"

            if name != "System Idle Process":
                if search_term == "" or search_term in name.lower():
                    if PID in self.process_info:
                        if self.process_info[PID]['name'] != name:
                            task_name = self.process_info[PID]['name_label']
                            task_name.config(text=name)
                        if self.process_info[PID]['cpu_percent'] != cpu_percent:
                            task_percent = self.process_info[PID]['percent_label']
                            task_percent.config(text=cpu_percent)
                    else:
                        task_name = Label(self.task_frame, text=name)
                        task_name.grid(row=row, column=0, padx=10, pady=5, sticky="w")
                        task_name.bind("<Button-1>",
                                       lambda event, Name=task_name, pid=PID: self.on_label_click(Name, pid))

                        task_percent = Label(self.task_frame, text=cpu_percent)
                        task_percent.grid(row=row, column=1, padx=10, pady=5, sticky="e")

                        new_process_info[PID] = {'name': name, 'name_label': task_name, 'cpu_percent': cpu_percent,
                                                 'percent_label': task_percent}

                    row += 1
        self.process_info.update(new_process_info)
        self.after(10000, self.update_list)


if __name__ == "__main__":
    window = TaskManager()
    window.task_manager()
