from tkinter import ttk, constants


class HelloView:
    def __init__(self, root, handle_menu):
        self._root = root
        self._handle_menu = handle_menu
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        button_continue = ttk.Button(
            master=self._frame,
            text="Jatka kirjautumatta",
            command=self._handle_menu
        )
        # Lisätään toiminto myöhemmin
        button_sign_in = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=None
        )
        # Lisätään toiminto myöhemmin
        button_register = ttk.Button(
            master=self._frame,
            text="Rekisteröidy",
            command=None
        )

        button_continue.grid(row=1, column=0)
        button_sign_in.grid(row=2, column=0)
        button_register.grid(row=3, column=0)
