from tkinter import ttk, constants
import customtkinter

class SearchStringView:
    def __init__(self, root, handle_home, string_service):
        self._root = root
        self._handle_home = handle_home
        self._string_service = string_service
        self._frame = None
        self._search_string = None
        self._closest_word= None
        self._input_word = ""

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _handle_search_string(self):
        string = self._search_string.get()

        if string:
            self._string_service.search_word_from_trie(string)

            if self._string_service.search_word_from_trie(string):
                self._input_word = customtkinter.CTkLabel(master=self._frame, text="Word found in trie!")
                self._input_word.grid(row=3, column=0)
                self._input_word.after(3000, lambda:  self._input_word.configure(text=""))
            else:
                self._closest_word = self._string_service.__str__()
                self._input_word = customtkinter.CTkLabel(master=self._frame, text=self._closest_word)
                self._input_word.grid(row=3, column=0)
                self._input_word.after(3000, lambda:  self._input_word.configure(text=""))


    def _initialize_footer(self):
        self._search_string = customtkinter.CTkEntry(master=self._frame)

        create_string_button = customtkinter.CTkButton(
            master=self._frame,
            text="Search",
            command=self._handle_search_string
        )

        self._search_string.grid(
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
        label = customtkinter.CTkLabel(master=self._frame, text="Search string")

        self._initialize_footer()

        button = customtkinter.CTkButton(
            master=self._frame,
            text="Back",
            command=self._handle_home
        )

        label.grid(row=1, column=0)
        button.grid(row=0, column=0)

