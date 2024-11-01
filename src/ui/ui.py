from ui.home_view import HomeView
from ui.add_string_view import AddStringView
from ui.search_string_view import SearchStringView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._show_home_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        
        self._current_view = None
    
    def _handle_home(self):
        self._show_home_view()
    
    def _handle_add_string(self):
        self._show_add_string_view()
    
    def _handle_search_string(self):
        self._show_search_string_view()
    
    def _show_home_view(self):
        self._hide_current_view()

        self._current_view = HomeView(
            self._root,
            self._handle_add_string,
            self._handle_search_string
        )

        self._current_view.pack()
    
    def _show_add_string_view(self):
        self._hide_current_view()

        self._current_view = AddStringView(
            self._root,
            self._handle_home
        )

        self._current_view.pack()
    
    def _show_search_string_view(self):
        self._hide_current_view()

        self._current_view = SearchStringView(
            self._root,
            self._handle_home
        )

        self._current_view.pack()

