from ui.home_view import HomeView
from ui.add_string_view import AddStringView
from ui.search_string_view import SearchStringView


class UI:
    def __init__(self, root, string_service):
        self._root = root
        self._current_view = None
        self._string_service = string_service

    def start(self):
        self._show_view(HomeView)

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_view(self, view_class):
        self._hide_current_view()
        if view_class == HomeView:
            self._current_view = view_class(
                self._root, self._handle_add_string, self._handle_search_string
            )
        if view_class == AddStringView:
            self._current_view = view_class(
                self._root, self._handle_home, self._string_service
            )
        if view_class == SearchStringView:
            self._current_view = view_class(
                self._root, self._handle_home, self._string_service
            )
        self._current_view.pack()

    def _handle_home(self):
        self._show_view(HomeView)

    def _handle_add_string(self):
        self._show_view(AddStringView)

    def _handle_search_string(self):
        self._show_view(SearchStringView)
