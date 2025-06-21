HangStopper - A Free, Open-Source Bot That Dominates at Hangman
===============================================================

About
-----
**HangStopper** is a simple yet powerful application that can solve almost any Hangman game you throw at it. Simply give the bot information about the current game state and it will parse through nearly **200,000 words** and determine which letter is the best guess. Hangstopper uses a regular expressions to filter out the words that can't be solutions and then counts the occurrences of each of the remaining letters. It will guess whichever letter occurs the most in the possible solutions; if there is only one possible solution, it will guess the full word. While this method of guessing is extremely simple, it produces impressive results:

- `punctuation`: HangStopper found the word in 4 guesses, with 1 incorrect guess: `e, i, n, o -> PUNCTUATION`
- `comprehensive`: HangStopper found the word in 1 guess, after finding the position of the E's: `e -> COMPREHENSIVE`
- `bookshelf`: HangStopper found the word in 4 guesses, with 0 incorrect guesses: `e, s, l, o -> BOOKSHELF`

However, HangStopper does have some limitations. It usually does better with longer words than shorter words.

- `pen`: HangStopper found the word in 17 guesses, with 14 incorrect guesses: `a, o, e, t, d, r, l, n, k, w, m, y, h, s, g, f, p -> PEN`
- `jazz`: HangStopper found the word in 16 guesses, with 14 incorrect guesses: `a, s, r, l, n, t, e, k, d, g, f, p, m, y, b, j -> JAZZ`

Nevertheless, it is still an extremely powerful tool, which, combined with human intuition, can help you **crush your friends** at this children's game.

Features
--------
- A bland but **intuitive GUI**
- **Two wordlist options** for maximizing guess precision
- The ability to know **when to guess letters** and **when to guess the word**
- **Important statistics**, such as how many possible solutions are left and which words are solutions

Running and Installation
------------------------
This project does not use any dependencies other than TKinter, which may have already been installed with Python on your system. If you do not have TKinter pre-installed, you can install it using `sudo apt-get install python3-tkinter` or similar. You should also have a fairly recent version of Python on your computer, ideally 3.10 or higher.

Currently, this project is not properly packaged, so you should download it as a zip file or by using `git clone`. Once you have it saved on your computer, you can start the application by running `python3 ./src/main.py` in the project's root directory, called `HangStopper`.

Basic Use
---------
Enter the blanks and correctly guessed letters in the first text box and enter the incorrectly guessed letters in the second text box. Once you click **"Submit,"** HangStopper will quickly and efficiently parse through the wordlist to determine which letter appears the most often in the possible solution and would make the safest guess. To see all of the valid solutions for a given game state, click **"See All Possible Words."** If you know that the secret word is a very common English word, you can select the **"Only Check 10000 Most Common English Words"** checkbox to make your guesses even more efficient.

Credits
-------
This project makes use of two wordlists, the larger list from [this GitHub repo](https://github.com/wordnik/wordlist/blob/main/previous_list/wordlist-20200727.txt) and the 10,000 word list from [this website](https://www.top10000words.com/english/top-10000-english-words). These word lists are redistributed using the licenses under which their creators originally published them and are not relicensed under the MIT license used for the source code of this project. For more information, please consult the `LICENSE/` folder.

License
-------
HangStopper is licensed under the MIT license, which means that you are allowed to use, modify, and redistribute the source code for free, as long as you include a copy of the license in any derivatives you make. For more information, please consult the `LICENSE/` folder.

IMPORTANT NOTE
--------------
While this software is intended for use by general audiences, it is also designed to be able to guess any word that a user prompts it with. Thus, if the hints you give it point to an offensive word, it may output that offensive word as a suggested guess. bad-indentation does not support the use of these words to intentionally insult or offend other people and simply includes them in the wordlist to make the bot more rigorous.
