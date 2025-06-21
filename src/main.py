"""
main.py
~~~~~~~

A bare-bones GUI wrapper for the Hangman bot.
"""

# pylint: disable=line-too-long

from __future__ import annotations
import tkinter as tk
import bot

WIN_W = 550
WIN_H = 450
TITLE = "HangStopper"

class App(tk.Tk):
    """
    Class for containing the attributes of the
    application.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set window geometry
        scr_w = self.winfo_screenwidth()
        scr_h = self.winfo_screenheight()
        x_pos = (scr_w - WIN_W) // 2
        y_pos = (scr_h - WIN_H) // 2
        self.geometry(f"{WIN_W}x{WIN_H}+{x_pos}+{y_pos}")

        self.title(TITLE)
        self.lift()
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, "-topmost", False)

        # Initialize attributes
        self.secret_word = tk.StringVar()
        self.incorrect_letters = tk.StringVar()
        self.common_only = tk.BooleanVar() # selected when user only wants 10000 most common english words
        self.guess = ""

        self.initialize_subwidgets()


    def initialize_subwidgets(self):
        """
        Creates all subwidgets for this app.
        """
        input_frm = tk.Frame(self)
        input_frm.pack(side="top")

        title_lbl = tk.Label(input_frm, text="HangStopper",
                             font=("TkDefaultFont", 20, "underline"))
        title_lbl.pack(side="top")

        instruction_lbl1 = tk.Label(input_frm,
                                    text="Enter the current state of the game, using '?' for unknown letters.")
        instruction_lbl1.pack(side="top")

        self.secret_word_entry = tk.Entry(input_frm, font=("TkDefaultFont", 12),
                                          textvariable=self.secret_word)
        self.secret_word_entry.pack(side="top", pady=5)
        self.secret_word_entry.bind_all("<Key>", self.remove_invalid_characters)

        instruction_lbl2 = tk.Label(input_frm,
                                    text="Enter any incorrectly guessed letters.")
        instruction_lbl2.pack(side="top")

        self.incorrect_entry = tk.Entry(input_frm, font=("TkDefaultFont", 12),
                                        textvariable=self.incorrect_letters)
        self.incorrect_entry.pack(side="top", pady=5)
        self.incorrect_entry.bind_all("<Key>", self.remove_invalid_characters)

        submit_frm = tk.Frame(input_frm)
        submit_frm.pack(side="top")

        submit_btn = tk.Button(submit_frm, text="Submit", command=self.submit)
        submit_btn.pack(side="right")

        self.common_words_only_btn = tk.Checkbutton(submit_frm,
                                                    text="Only Check 10000 Most Common English Words",
                                                    font=("TkDefaultFont", 8), variable=self.common_only)
        self.common_words_only_btn.pack(side="left", padx=5)

        self.output_frm = tk.Frame(self, relief="solid", bd=1)
        self.output_frm.pack(side="top", pady=10, padx=10, fill="both")


    def remove_invalid_characters(self, e=None):
        """
        Removes invalid characters from the entry widgets
        """
        temp_str = ""
        for let in self.secret_word.get():
            if let.lower() in "abcdefghijklmnopqrstuvwxyz?":
                temp_str += let.lower()

        self.secret_word.set(temp_str)

        temp_str = ""
        for let in self.incorrect_letters.get():
            if let.lower() in "abcdefghijklmnopqrstuvwxyz":
                temp_str += let.lower()

        self.incorrect_letters.set(temp_str)


    def submit(self):
        """
        Create extra widgets and display the results
        when the form is submitted.
        """
        for widget in self.output_frm.winfo_children():
            widget.destroy()

        title_lbl = tk.Label(self.output_frm, text="Loading...",
                             font=("TkDefaultFont", 15, "italic"))
        title_lbl.pack(side="top", pady=5)

        if self.common_only.get():
            # when selected, only top 10000 words will be searched.
            self.guess = bot.LetterGuess(self.secret_word.get(), self.incorrect_letters.get(),
                                         wordlist_file=bot._10000_WORDLIST)
        else:
            self.guess = bot.LetterGuess(self.secret_word.get(), self.incorrect_letters.get())

        title_lbl.config(text="Results:")

        # Output most important result
        guess_lbl = tk.Label(self.output_frm,
                               font=("TkDefaultFont", 15))
        guess_lbl.pack(side="top", pady=5)

        wordlist_needed = False
        if len(self.guess.valid_words) == 1:
            guess_lbl.config(text=f"The word is '{self.guess.valid_words[0]}.'")
        elif len(self.guess.valid_words) == 0:
            guess_lbl.config(text="There are no valid solutions.")
        else:
            guess_lbl.config(text=f"Best Guess: {self.guess.best_guess}")
            wordlist_needed = True

        valid_words_lbl = tk.Label(self.output_frm, text=f"Possible Words: {len(self.guess.valid_words)}")
        valid_words_lbl.pack(side="top")

        reduction_lbl = tk.Label(self.output_frm,
                                 text=f"Occurences of guess in possible words: {self.guess.best_guess_score}")
        reduction_lbl.pack(side="top")

        if wordlist_needed:
            wordlist_btn = tk.Button(self.output_frm,
                                     text="See All Possible Words", command=self.all_words)
            wordlist_btn.pack(side="top")

    def all_words(self, e=None):
        """
        Displays all valid possibilities
        """
        pop_up = tk.Toplevel(self, width=300, height=300)
        pop_up.geometry("300x300")
        pop_up.lift()
        pop_up.attributes("-topmost", True)
        pop_up.after_idle(pop_up.attributes, "-topmost", False)

        title = tk.Label(pop_up, text="All Valid Words")
        title.pack()

        content_frm = tk.Frame(pop_up, bd=1, relief="solid")
        content_frm.pack(fill="both", padx=10, pady=10)

        scroll = tk.Scrollbar(content_frm)
        scroll.pack(side="right", fill="y")

        listbox = tk.Listbox(content_frm, height=10, yscrollcommand=scroll.set)

        for word in self.guess.valid_words:
            listbox.insert("end", word)

        listbox.pack()

        scroll.config(command=listbox.yview)

        pop_up.mainloop()


if __name__ == "__main__":
    root = App()
    root.mainloop()
