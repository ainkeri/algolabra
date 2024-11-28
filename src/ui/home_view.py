from tkinter import constants
import customtkinter


class HomeView:
    def __init__(self, root, handle_add_string, handle_search_string):
        self._root = root
        self._handle_add_string = handle_add_string
        self._handle_search_string = handle_search_string
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = customtkinter.CTkFrame(master=self._root)
        label = customtkinter.CTkLabel(master=self._frame, text="Tervetuloa!")

        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)

        add_button = customtkinter.CTkButton(
            master=self._frame, text="Lisää uusi sana", command=self._handle_add_string
        )

        search_button = customtkinter.CTkButton(
            master=self._frame, text="Etsi sanaa", command=self._handle_search_string
        )

        label.grid(row=0, column=0, pady=(20, 10), sticky="ew")
        add_button.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        search_button.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="ew")
