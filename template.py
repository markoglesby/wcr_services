import tkinter
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from server import Server
import socket


class Root(tkinter.Tk):
    """Creates root window."""

    def __init__(self, *args, **kwargs):

        self.machine = socket.gethostname()
        # setting window size
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.width = 300
        self.height = 400
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (
            self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.geometry(self.alignstr)
        self.resizable(width=False, height=False)
        self.title("WebCenter Services")
        self._menu = MainMenu(self)
        self._container = None

        self.show_main_frame()

    def show_main_frame(self):
        if self._container != None:
            self._container.destroy()
        self._container = MainFrame(self)

    def show_setting_frame(self):
        if self._container != None:
            self._container.destroy()
        self._container = Settings(self)

    def show_help_frame(self):
        if self._container:
            self._container.destroy()
        self._container = About(self)


class MainMenu(tkinter.Menu):
    """Creates Main menu."""

    @property
    def root(self):
        return self._root

    def __init__(self, root, *args, **kwargs):
        tkinter.Menu.__init__(self, root, *args, **kwargs)
        self._root = root

        window_menu = FramesMenu(self, tearoff=0)
        self.add_cascade(label="Options", menu=window_menu)

        root.config(menu=self)


class FramesMenu(tkinter.Menu):
    """Creates Window menu."""

    def __init__(self, parent, *args, **kwargs):
        tkinter.Menu.__init__(self, parent, *args, **kwargs)

        self.add_command(label="Main Window", command=parent.root.show_main_frame)
        self.add_command(label="Settings", command=parent.root.show_setting_frame)
        self.add_command(label="About", command=parent.root.show_help_frame)
        self.add_command(label="Exit", command=parent.root.quit)


class MainFrame(tkinter.Frame, Root):
    """Creates welcome frame."""

    def __init__(self, root, *args, **kwargs):
        self._root = root

        self.machine = socket.gethostname()

        tkinter.Frame.__init__(self, root, *args, **kwargs)
        self.pack(fill="both", expand=True)

        # Create Server Entry fields
        self.server_frame = Frame(self)
        self.server_frame.pack(padx=10, pady=10)

        self.app_label = tk.Label(self.server_frame, text='Server: ' + self.machine, font=("Helvetica", 12))
        self.app_label.grid(row=0, column=0, sticky=tk.W)

        # Create Button Frame and Buttons
        self.button_frame = Frame(self)
        self.button_frame.pack()
        # self.font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.font = tkFont.Font(family="Helvetica", size=12)

        self.start_button = Button(self.button_frame, text="Start WebCenter Services", font=self.font,
                                   command=self.start_services)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)
        self.stop_button = Button(self.button_frame, text="Stop WebCenter Services", font=self.font,
                                  command=self.stop_services)
        self.stop_button.grid(row=1, column=0, padx=10, pady=10)
        self.restart_button = Button(self.button_frame, text="Restart WebCenter Services", font=self.font,
                                     command=self.restart_services)
        self.restart_button.grid(row=2, column=0, padx=10, pady=10)

        # Create Status Frame and Label
        self.status_frame = Frame(self)
        self.status_frame.pack(padx=10, pady=10)
        self.status_label = tk.Label(self.status_frame, text="Status:", font=("Helvetica", 12, "bold"))
        self.status_label.grid(row=0, column=0, sticky=tk.W)

        # Create Status Frame and bottom
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(anchor=S, fill=BOTH, expand=True)
        self.quit_button = Button(self.bottom_frame, text="Quit", command=self.destroy, font=self.font)
        self.quit_button.pack(side=BOTTOM, padx=10, pady=10)

    @staticmethod
    def start_services(self):
        """Starts the services using a method in the server class"""
        for i in Server.wcr_services:
            print(i)
            self.start_service(i)

    @staticmethod
    def stop_services(self):
        """Stops the services using a method in the server class"""
        for i in Server.wcr_services:
            print(i)
            self.stop_service(i)

    @staticmethod
    def restart_services(self):
        """Restarts the services using a method in the server class"""
        for i in Server.wcr_services:
            print(i)
            self.restart_service(i)

    def goto_settings(self):
        self._root.show_setting_frame()

    def goto_about(self):
        self._root.show_help_frame()


class Settings(tkinter.Frame):
    """Creates Frame 2."""

    def __init__(self, root, *args, **kwargs):
        self._root = root

        tkinter.Frame.__init__(self, root, *args, **kwargs)
        self.pack(fill="both", expand=True)

        welcome_label = tkinter.Label(self, text="Welcome to Frame 2")
        welcome_label.grid(row=1, column=1)

        buttons_frame = tkinter.Frame(self)
        buttons_frame.grid(row=3, column=1)

        frame2_button = tkinter.Button(
            buttons_frame,
            text="Go To Frame 1",
            command=self.goto_main_frame)
        frame2_button.grid(row=1, column=1)

        frame3_button = tkinter.Button(
            buttons_frame,
            text="Go To Frame 3",
            command=self.goto_about_frame)
        frame3_button.grid(row=1, column=2)

        quit_button = tkinter.Button(
            buttons_frame,
            text="Quit",
            command=root.quit)
        quit_button.grid(row=1, column=3)

    def goto_main_frame(self):
        self._root.show_main_frame()

    def goto_about_frame(self):
        self._root.show_help_frame()


class About(tkinter.Frame):
    """Creates Frame 3."""

    def __init__(self, root, *args, **kwargs):
        self._root = root

        tkinter.Frame.__init__(self, root, *args, **kwargs)
        self.pack(fill="both", expand=True)

        welcome_label = tkinter.Label(self, text="About WebCenter Services")
        welcome_label.grid(row=1, column=1)

        '''make an info box usiong a tkinter label'''
        info_frame = tkinter.Frame(self)
        info_frame.grid(row=3, column=1)
        info_label = tkinter.Label(info_frame, text="WebCenter Services is a tool to manage the ").pack()

        buttons_frame = tkinter.Frame(self)
        buttons_frame.grid(row=4, column=1)

        frame1_button = tkinter.Button(
            buttons_frame,
            text="Main Window",
            command=self.goto_main_frame)
        frame1_button.grid(row=1, column=1)

        quit_button = tkinter.Button(
            buttons_frame,
            text="Quit",
            command=root.quit)
        quit_button.grid(row=1, column=3)

    def goto_main_frame(self):
        self._root.show_main_frame()

    def goto_settings_frame(self):
        self._root.show_setting_frame()


if __name__ == "__main__":
    wcr = Root()
    wcr.mainloop()
