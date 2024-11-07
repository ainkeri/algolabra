import customtkinter
from ui.ui import UI
from services.string_service import StringService

def main():
    window = customtkinter.CTk()
    window.title("Kirjoitusvirheiden korjaaja")
    window.geometry("400x150")

    string_service = StringService()
    string_service.add_file_words_to_trie()

    ui_view = UI(window, string_service)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()