from tkinter import ttk, constants
import tkinter as tk
import customtkinter


class AddStringView:
    def __init__(self, root, handle_home, string_service):
        self._root = root
        self._handle_home = handle_home
        self._string_service = string_service
        self._frame = None
        self._create_string_entry = None
        self._input_string = ""

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_create_string(self):
        string = self._create_string_entry.get()

        if string:
            if self._string_service.search_word_from_trie(string):
                self._input_string = customtkinter.CTkLabel(
                    master=self._frame, text=f"Sana '{string}' on jo lisätty.")
                self._input_string.grid(row=3, column=0)
                self._input_string.after(
                    3000, lambda:  self._input_string.configure(text=""))
            else:
                self._string_service.create_string(string)
                self._input_string = customtkinter.CTkLabel(
                    master=self._frame, text=f"Uusi sana '{string}' lisätty!")
                self._input_string.grid(row=3, column=0)
                self._input_string.after(
                    3000, lambda:  self._input_string.configure(text=""))

        self._create_string_entry.delete(0, tk.END)

    def _initialize_footer(self):
        self._create_string_entry = customtkinter.CTkEntry(master=self._frame)

        create_string_button = customtkinter.CTkButton(
            master=self._frame,
            text="Lisää",
            command=self._handle_create_string
        )

        self._create_string_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        create_string_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = customtkinter.CTkFrame(master=self._root)
        label = customtkinter.CTkLabel(master=self._frame, text="Lisää sana:")

        self._initialize_footer()

        button = customtkinter.CTkButton(
            master=self._frame,
            text="Takaisin",
            command=self._handle_home
        )

        label.grid(row=1, column=0)
        button.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="ew")
