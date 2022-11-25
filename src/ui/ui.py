from tkinter import Tk
from hello_view import HelloView
from menu import Menu


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_hello_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_menu(self):
        self._show_menu()

    def _handle_hello(self):
        self._show_hello_view()

    def _show_hello_view(self):
        self._hide_current_view()

        self._current_view = HelloView(
            self._root,
            self._handle_menu
        )

        self._current_view.pack()

    def _show_menu(self):
        self._hide_current_view()

        self._current_view = Menu(
            self._root,
            self._handle_hello
        )

        self._current_view.pack()


window = Tk()
window.title("Sudoku")

ui = UI(window)
ui.start()

window.mainloop()
