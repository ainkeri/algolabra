from tkinter import ttk, constants

class HomeView:
    def __init__(self, root, handle_add_string, handle_search_string):
        self._root = root
        self._handle_add_string = handle_add_string
        self._handle_search_string = handle_search_string
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Home")

        add_button = ttk.Button(
            master=self._frame,
            text="Add a new string",
            command=self._handle_add_string
        )

        search_button = ttk.Button(
            master=self._frame,
            text="Search string",
            command=self._handle_search_string
        )

        label.grid(row=0, column=0)
        add_button.grid(row=1, column=0)
        search_button.grid(row=1, column=1)
