from tkinter import ttk, constants

class Menu:
    def __init__(self, root, handle_hello):
        self._root = root
        self._handle_hello = handle_hello
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Aloitusvalikko")

        button_new_game = ttk.Button(
            master=self._frame,
            text="Aloita uusi peli",
            command=None
        )

        button_statistics = ttk.Button(
            master=self._frame,
            text="Pelitilastot",
            command=None
        )

        button_back = ttk.Button(
            master=self._frame,
            text="Takaisin alkuun",
            command=self._handle_hello
        )


        label.grid(row=0, column=0)
        button_new_game.grid(row=1, column=0)
        button_statistics.grid(row=2, column=0)
        button_back.grid(row=3, column=0)