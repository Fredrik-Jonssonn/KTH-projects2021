from tkinter import *
from tkinter import messagebox
import random
import time


class Tile:
    """Describes a tile of a minefield. Stores information about how many mines
    are in proximity, if the tile has a mine planted on it, if it has been
    checked by a user and if it has been flagged by the user."""

    def __init__(self):
        """The constructor for a tile that creates an empty tile"""
        self.mines_in_proximity = 0
        self.is_mine = False
        self.is_checked = False
        self.is_flagged = False

    def __repr__(self):
        """Returns a string that gives the information about the tile that
         the user has access to."""
        if self.is_flagged is True:
            return "F"
        if self.is_checked is False:
            return " "
        if self.is_mine is True:
            return "M"
        return str(self.mines_in_proximity)

    def check_tile(self):
        """Method that tracks if a tile is checked during the game by
        making the attribute that stores if the tile has been checked True"""
        self.is_checked = True

    def plant_mine(self):
        """Method for planting a mine on a tile, by making
        the attribute that stores if the tile has a mine planted on it
        True"""
        self.is_mine = True

    def add_mine_in_proximity(self):
        """Method that increases the amount of mines in the proximity
        of the tile by 1."""
        self.mines_in_proximity += 1

    def flag_tile(self):
        """Method that tracks if a tile is flagged/unflagged during the game by
        making the attribute that stores if the tile is flagged True/False"""
        if self.is_flagged:
            self.is_flagged = False
        elif not self.is_flagged:
            self.is_flagged = True


class MinesweeperApp(Tk):
    """The base of the entire application, a master
     window with a set geometry and title."""

    def __init__(self):
        """The constructor that creates the master window with a
        set geometry and title."""
        Tk.__init__(self)
        self._frame = None
        self.geometry("1280x850")
        self.title("Minesweeper"
                   )
        self.resizable(False, False)
        self.switch_frame(MainMenu)

    def switch_frame(self, frame_class):
        """Destroys the current frame and replaces it with a new one that is placed
        in the master window, i.e moving from one page to another in the application"""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def start_game(self, rows, columns, mines):
        """Destroys the SettingsPage frame and replaces it with a GamePage
        frame with the format the user chose on the SettingsPage frame,
        i.e starts the game"""
        game = GamePage(self, rows, columns, mines)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = game
        self._frame.pack()


class MainMenu(Frame):
    """The Main Menu page frame"""

    def __init__(self, master):
        """Constructs the Main Menu page frame containing elements that allow the user to
        Play Minesweeper, view highscores and exit the application."""
        Frame.__init__(self, master)
        Label(self, text="MINESWEEPER", font=("courier", 44)).grid(row=0, column=0, pady=(100, 50), padx=290)
        Button(self, text="Play Minesweeper", height=5, width=25, command=lambda: master.switch_frame(SettingsPage)) \
            .grid(row=1, column=0)
        Button(self, text="High Scores", height=5, width=25, command=lambda: master.switch_frame(HighscorePage)) \
            .grid(row=2, column=0)
        Button(self, text="Exit Minesweeper", height=5, width=25, command=master.quit).grid(row=3, column=0)


class SettingsPage(Frame):
    """The settings page frame"""

    def __init__(self, master):
        """Constructs the Settings page frame containing elements that allow the user to
         set the amount rows, columns and mines in the coming game and start that game. They also
         allow the user to return to the Main Menu page frame"""
        Frame.__init__(self, master)
        Label(self, text="Rows", font=("courier", 44)).grid(row=0, column=0, pady=(60, 0), columnspan=2)
        row_slider = Scale(self, length=250, from_=5, to=20, orient=HORIZONTAL,
                           command=lambda value: self.mine_slider_dependance(value, column_slider.get(), mine_slider))
        row_slider.grid(row=1, column=0, columnspan=2)
        Label(self, text="Columns", font=("courier", 44)).grid(row=2, column=0, pady=(20, 0), columnspan=2)
        column_slider = Scale(self, length=250, from_=5, to=30, orient=HORIZONTAL,
                              command=lambda value: self.mine_slider_dependance(row_slider.get(), value, mine_slider))
        column_slider.grid(row=3, column=0, columnspan=2)
        Label(self, text="Mines", font=("courier", 44)).grid(row=4, column=0, pady=(20, 0), columnspan=2)
        mine_slider = Scale(self, length=250, from_=(int(round((row_slider.get() * column_slider.get()) * 0.1))),
                            to=(int(round((row_slider.get() * column_slider.get()) * 0.9))), orient=HORIZONTAL)
        mine_slider.grid(row=5, column=0, columnspan=2)
        Button(self, text="Play", height=5, width=25, command=lambda: master.start_game(row_slider.get(),
                                                                                        column_slider.get(),
                                                                                        mine_slider.get())) \
            .grid(row=6, column=0, pady=(50, 0))
        Button(self, text="Difficulty suggestions", height=5, width=25, command=self.difficulty_suggestions) \
            .grid(row=6, column=1, pady=(50, 0))
        Button(self, text="Return", height=5, width=54, command=lambda: master.switch_frame(MainMenu)) \
            .grid(row=7, column=0, columnspan=2)

    @staticmethod
    def mine_slider_dependance(row_slider_value, column_slider_value, mine_slider):
        """Configures the upper and lower limits of the slider that sets the amount of mines
         in the coming game depending to how many rows and columns are set."""
        mine_slider.config(from_=(int(round((int(row_slider_value) * int(column_slider_value)) * 0.1))),
                           to=(int(round((int(row_slider_value) * int(column_slider_value)) * 0.9))))

    @staticmethod
    def difficulty_suggestions():
        """Displays a window containing difficulty suggestions"""
        messagebox.showinfo("Difficulty Suggestions", ("Easy: 9 x 9, 10 mines\n"
                                                       "Medium: 16 x 16, 40 mines\n"
                                                       "Expert: 16 x 30, 99 mines"))


class HighscorePage(Frame):
    """The highscore page frame"""

    def __init__(self, master):
        """Constructs the highscore page frame containing elements that display
        the current top ten Minesweeper scores and allow the user to
        return to the Main Menu page."""
        Frame.__init__(self, master)
        Label(self, text="Top 10:", font=("courier", 40)) \
            .grid(row=0, column=0, pady=(100, 50))
        highscore_list = read_highscores()
        counter = 0
        for element in highscore_list:
            counter += 1
            Label(self, text=(str(counter) + "." + str(element[0]) + ": " + str(element[1]) + " points"),
                  font=("courier", 22)).grid(row=(counter + 1), column=0)
        Button(self, text="Return", height=5, width=25, command=lambda: master.switch_frame(MainMenu)) \
            .grid(row=counter + 2, column=0)


class GamePage(Frame):
    """The game page frame"""

    def __init__(self, master, rows, columns, mines):
        """Constructs the game page frame containing a matrix of tile buttons
        that represent the mine field. Also contains buttons allows the user
        to view game instructions and return to the settings page frame"""
        Frame.__init__(self, master)
        mine_field = create_mine_field_matrix(rows, columns)
        mine_placement(mine_field, mines)
        set_proximity(mine_field)
        tile_buttons = []
        start_time = time.time()
        self.rowconfigure(0, minsize=110)
        for row in range(rows):
            tile_buttons.append([])
            for column in range(columns):
                new_tile_button = Button(self, text=str(mine_field[row][column]), width=1, height=1,
                                         command=lambda row=row, column=column:
                                         self.check_tile_button(master, tile_buttons, row, column, mine_field, mines,
                                                                start_time))
                new_tile_button.grid(row=row, column=column, sticky=S)
                tile_buttons[row].append([])
                tile_buttons[row][column] = new_tile_button
                new_tile_button.grid(row=row, column=column)
                new_tile_button.bind('<Button-3>', lambda event, row=row, column=column:
                self.flag_tile_button(event, master, tile_buttons, row, column, mine_field, mines, start_time))
        Button(self, text="Return", width=9, command=lambda: master.switch_frame(SettingsPage)) \
            .grid(row=rows + 1, column=0, columnspan=columns, sticky=S)
        Button(self, text="Instructions", width=9, command=self.instructions) \
            .grid(row=rows, column=0, pady=(10, 0), columnspan=columns)

    @staticmethod
    def instructions():
        """Displays a window containing game instructions"""
        messagebox.showinfo("Instructions", ("Left click a tile to\n check it for mines\n\n"
                                             "Right click a tile to\n flag/unflag it"))

    def check_tile_button(self, master, tile_buttons, row, column, field, mines, start_time):
        """Represents the user action of checking tiles by disabling tile buttons, altering
        tile button text and calling the Tile.check_tile method on those tiles.
        Also checks if a win/lose condition is met by that action, if so the game ends"""
        flag_win_counter, correctly_flagged_mines = check_win(field, mines)[1:3]
        if field[row][column].is_flagged:
            return
        elif field[row][column].is_mine:
            self.reveal_field(field, tile_buttons)
            self.end_screen(False, correctly_flagged_mines, mines, 0, start_time, master)
        elif field[row][column].mines_in_proximity == 0:
            self.check_neighbours(row, column, field, tile_buttons)
        else:
            Tile.check_tile(field[row][column])
            tile_buttons[row][column].config(text=str(field[row][column]), state=DISABLED)
        if check_win(field, mines)[0]:
            self.reveal_field(field, tile_buttons)
            self.end_screen(True, mines, mines, len(field) * len(field[0]), start_time, master)

    def flag_tile_button(self, event, master, tile_buttons, row, column, field, mines, start_time):
        """Represents the user action of flagging/unflagging tiles by altering the tile button
        text and calling the Tile.flag_tile method on those tiles. Also checks if a win
        condition is met by that action, if so the game ends"""
        if field[row][column].is_checked:
            return
        Tile.flag_tile(field[row][column])
        tile_buttons[row][column].config(text=str(field[row][column]))
        if check_win(field, mines)[0]:
            self.reveal_field(field, tile_buttons)
            self.end_screen(True, mines, mines, len(field) * len(field[0]), start_time, master)

    def check_neighbours(self, row, column, field, tile_buttons):
        """Recursively checks the entire continuous part of the minefield consisting
        of all neighboring tiles to tiles with with zero mines in
        proximity by altering tile button text, disabling tile buttons and
        calling the Tile.check_tile method on those tiles."""
        if row < 0 or row > len(field) - 1 or column < 0 or column > len(field[0]) - 1:
            return
        if field[row][column].is_flagged:
            return
        if not field[row][column].is_checked:
            Tile.check_tile(field[row][column])
            tile_buttons[row][column].config(text=str(field[row][column]), state=DISABLED)
            if field[row][column].mines_in_proximity == 0:
                for adjacent_row in range(row - 1, row + 2):
                    for adjacent_column in range(column - 1, column + 2):
                        if adjacent_row == row and adjacent_column == column:
                            continue
                        else:
                            self.check_neighbours(adjacent_row, adjacent_column, field, tile_buttons)

    @staticmethod
    def reveal_field(field, tile_buttons):
        """Reveals the entire mine field by checking all of the tiles by
        disabling tile buttons, altering tile button text and
        calling the Tile.check_tile method on those tiles.
        """
        for row in range(len(field)):
            for column in range(len(field[0])):
                if field[row][column].is_flagged:
                    Tile.flag_tile(field[row][column])
                Tile.check_tile(field[row][column])
                tile_buttons[row][column].config(text=str(field[row][column]), state=DISABLED)

    def end_screen(self, win, cleared_mines, mines, field_size_score_bonus, start_time, master):
        """Creates a top level end screen window containing elements that display
        if the user lost or won the game and their score. If the users score is among
        the top ten they are able to save their score. The user may also
        return to the Main Menu page from here."""
        end_screen = Toplevel(self)
        end_screen.resizable(False, False)
        end_screen.geometry("500x500")
        end_screen.columnconfigure(0, weight=1)
        total_time = time.time() - start_time
        highscore_list = read_highscores()
        if win is False:
            Label(end_screen, text=("BOOOOOM!\nGAME OVER!\nYou found " + str(cleared_mines) + " out of " +
                                    str(mines) + " mines")).grid(row=0, column=0, pady=20)
        if win is True:
            Label(end_screen, text=("You win\nYou found all of the " +
                                    str(mines) + " mines")).grid(row=0, column=0, pady=20)
        score = round(60000 * (cleared_mines / total_time) + field_size_score_bonus)
        Label(end_screen, text=("Your score was " + str(score) + " points")).grid(row=1, column=0, pady=20)
        try:
            if score < highscore_list[9][1]:
                Button(end_screen, text="Main Menu", command=lambda: master.switch_frame(MainMenu)) \
                    .grid(row=2, column=0)
                highscore = False
            else:
                highscore = True
        except IndexError:
            highscore = True
        if highscore is True:
            player_name_entry = Entry(end_screen)
            player_name_entry.grid(row=2, column=0)
            player_name_entry.insert(0, "Player Name")
            Button(end_screen, text="Save score and return to Main Menu",
                   command=lambda: self.save_highscore(master, highscore_list, player_name_entry.get(), score)) \
                .grid(row=3, column=0)
        end_screen.mainloop()

    @staticmethod
    def save_highscore(master, highscore_list, highscore_holder, score):
        """Saves the users highscore by adding the score to the accompanying
        highscore.txt file and then sorting the file according to score.
        Scores below the 10th place are discarded.
        Also returns the user to the Main Menu page"""
        highscore_list.append([highscore_holder, score])
        highscore_list.sort(reverse=True, key=lambda x: x[1])
        counter = 0
        with open('highscore.txt', "w+") as highscore_file:
            for element in highscore_list:
                if counter >= 10:
                    break
                counter += 1
                highscore_file.write(str(element[0]) + "\n" + str(element[1]) + "\n")
        master.switch_frame(MainMenu)


def create_mine_field_matrix(rows, columns):
    """Creates and returns a 2d list of tile objects, i.e the matrix
    that will act as the mine field"""
    mine_field = []
    for row in range(rows):
        mine_field.append([])
        for column in range(columns):
            mine_field[row].append([])
            mine_field[row][column] = Tile()
    return mine_field


def mine_placement(field, mines):
    """Randomly places the chosen amount of mines in a matrix of tile objects"""
    counter = 0
    while counter < mines:
        row = random.choice(range(len(field)))
        column = random.choice(range(len(field[0])))
        if not field[row][column].is_mine:
            Tile.plant_mine(field[row][column])
            counter += 1


def set_proximity(field):
    """Calculates and stores the amount of mines in that are in adjacent tiles
    for every tile in a matrix of tile objects"""
    for row in range(len(field)):
        for column in range(len(field[0])):
            if field[row][column].is_mine:
                for adjacent_row in range(row - 1, row + 2):
                    for adjacent_column in range(column - 1, column + 2):
                        if (adjacent_row == row and adjacent_column == column) or \
                                (adjacent_row < 0 or adjacent_row > len(field) - 1 or
                                 adjacent_column < 0 or adjacent_column > len(field[0]) - 1):
                            continue
                        else:
                            Tile.add_mine_in_proximity(field[adjacent_row][adjacent_column])


def check_win(field, mines):
    """Returns the amount of correctly flagged mines, the sum
    correctly flagged mines - incorrectly flagged mines (flag_win_counter)
    and a boolean: True if the minefield satisfies one of two
    win conditions, either having all non-mine tiles checked
    or having all mine-tiles flagged. False otherwise."""
    flag_win_counter = 0
    reveal_win_counter = 0
    correctly_flagged_mines_counter = 0
    for row in range(len(field)):
        for column in range(len(field[0])):
            if field[row][column].is_mine and field[row][column].is_flagged:
                flag_win_counter += 1
                correctly_flagged_mines_counter += 1
            if (not field[row][column].is_mine) and field[row][column].is_flagged:
                flag_win_counter -= 1
            if field[row][column].is_checked:
                reveal_win_counter += 1
    if flag_win_counter == mines:
        return True, flag_win_counter, correctly_flagged_mines_counter
    elif reveal_win_counter == len(field) * len(field[0]) - mines:
        return True, flag_win_counter, correctly_flagged_mines_counter
    else:
        return False, flag_win_counter, correctly_flagged_mines_counter


def read_highscores():
    """Reads the accompanying highscore.txt file and
     returns a 2d list where each element consists of the
     highscore holder and the score"""
    with open('highscore.txt', "r") as highscore_file:
        highscore_list = []
        highscore_holder = highscore_file.readline().strip()
        while highscore_holder != "":
            score = int(highscore_file.readline().strip())
            highscore_list.append([highscore_holder, score])
            highscore_holder = highscore_file.readline().strip()
        return highscore_list


if __name__ == "__main__":
    """Starts the program"""
    app = MinesweeperApp()
    app.mainloop()
