from tkinter import ttk, constants
from services.string_service import string_service

class AddStringView:
    def __init__(self, root, handle_home):
        self._root = root
        self._handle_home = handle_home
        self._frame = None
        self._create_string_entry = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _handle_create_string(self):
        string = self._create_string_entry.get()

        if string:
            string_service.create_string(string)
    
    def _initialize_footer(self):
        self._create_string_entry = ttk.Entry(master=self._frame)

        create_string_button = ttk.Button(
            master=self._frame,
            text="Add",
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
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Add string")

        self._initialize_footer()

        button = ttk.Button(
            master=self._frame,
            text="Back",
            command=self._handle_home
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)