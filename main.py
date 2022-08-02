#!/usr/bin/python3
# Mark Oglesby
"""Application that allows for the starting, stopping or restarting of services
on a Windows machine for Esko WebCenter"""

from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import server
import socket


class App:
    """Creates the GUI"""
    def __init__(self, root):
        root.title("WebCenter Services")

        self.machine = socket.gethostname()
        # setting window size
        width = 300
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Create Server Entry fields
        self.server_frame = Frame(root)
        self.server_frame.pack(padx=10, pady=10)

        self.app_label = tk.Label(self.server_frame, text='Server: ' + self.machine, font=("Helvetica", 12))
        self.app_label.grid(row=0, column=0, sticky=tk.W)

        # Create Button Frame and Buttons
        self.button_frame = Frame(root)
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
        self.status_frame = Frame(root)
        self.status_frame.pack(padx=10, pady=10)
        self.status_label = tk.Label(self.status_frame, text="Status:", font=("Helvetica", 12, "bold"))
        self.status_label.grid(row=0, column=0, sticky=tk.W)

        # Create Status Frame and bottom
        self.bottom_frame = Frame(root)
        self.bottom_frame.pack(anchor=S, fill=BOTH, expand=True)
        self.quit_button = Button(self.bottom_frame, text="Quit", command=root.destroy, font=self.font)
        self.quit_button.pack(side=BOTTOM, padx=10, pady=10)

    @staticmethod
    def start_services():
        """Starts the services using a method in the server class"""
        for i in wcr.wcr_services:
            print(i)
            wcr.start_service(i)

    @staticmethod
    def stop_services():
        """Stops the services using a method in the server class"""
        for i in wcr.wcr_services:
            print(i)
            wcr.stop_service(i)

    @staticmethod
    def restart_services():
        """Restarts the services using a method in the server class"""
        for i in wcr.wcr_services:
            print(i)
            wcr.restart_service(i)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    wcr = server.Server()
    root.mainloop()
