from tkinter import constants
import customtkinter


class SearchStringView:
    def __init__(self, root, handle_home, string_service):
        self._root = root
        self._handle_home = handle_home
        self._string_service = string_service
        self._frame = None
        self._search_string = None
        self._closest_word = None
        self._input_word = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_search_string(self):
        string = self._search_string.get()

        if self._input_word is not None:
            self._input_word.destroy()

        if string:
            try:
                if self._string_service.word_exists_in_trie(string):
                    self._input_word = customtkinter.CTkLabel(
                        master=self._frame, text="Sana löytyi!"
                    )
                else:
                    self._closest_word = " ".join(
                        self._string_service.returns_closest_list(string)
                    )
                    if self._closest_word == string:
                        self._input_word = customtkinter.CTkLabel(
                            master=self._frame,
                            text="Lause löytyi!",
                        )

                    elif len(self._closest_word) <= 1:
                        self._input_word = customtkinter.CTkLabel(
                            master=self._frame,
                            text="Sanaa/lausetta ei löytynyt",
                        )
                    else:
                        self._input_word = customtkinter.CTkLabel(
                            master=self._frame,
                            text=f"Tarkoititko: '{self._closest_word}'?",
                        )
                self._input_word.grid(row=3, column=0)
                self._input_word.after(
                    6000, lambda: self._input_word.configure(text="")
                )
            except TimeoutError as e:
                self._input_word = customtkinter.CTkLabel(
                    master=self._frame, text=f"Virhe {str(e)}"
                )
                self._input_word.grid(row=3, column=0)
                self._input_word.after(
                    6000, lambda: self._input_word.configure(text="")
                )

    def _initialize_footer(self):
        self._search_string = customtkinter.CTkEntry(master=self._frame)

        create_string_button = customtkinter.CTkButton(
            master=self._frame, text="Etsi", command=self._handle_search_string
        )

        self._search_string.grid(row=2, column=0, padx=5, pady=5, sticky=constants.EW)

        create_string_button.grid(row=2, column=1, padx=5, pady=5, sticky=constants.EW)

        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=0)

    def _initialize(self):
        self._frame = customtkinter.CTkFrame(master=self._root)
        label = customtkinter.CTkLabel(
            master=self._frame, text="Etsi sanaa tai lausetta:"
        )

        button = customtkinter.CTkButton(
            master=self._frame, text="Takaisin", command=self._handle_home
        )

        label.grid(row=1, column=0, padx=10, pady=10)
        button.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        self._initialize_footer()
