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
            return "*"
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
    for every tile in a matrix of Tile objects"""
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


def check_neighbours(row, column, field):
    """Recursively checks the entire continuous part of the minefield consisting
    of all neighboring tiles to tiles with with zero mines in
    proximity"""
    if row < 0 or row > len(field) - 1 or column < 0 or column > len(field[0]) - 1:
        return
    if field[row][column].is_flagged:
        return
    if not field[row][column].is_checked:
        Tile.check_tile(field[row][column])
        if field[row][column].mines_in_proximity == 0:
            for adjacent_row in range(row - 1, row + 2):
                for adjacent_column in range(column - 1, column + 2):
                    if adjacent_row == row and adjacent_column == column:
                        continue
                    else:
                        check_neighbours(adjacent_row, adjacent_column, field)


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


def reveal_field(field):
    """Reveals the entire mine field by checking all of the tiles"""
    for row in range(len(field)):
        for column in range(len(field[0])):
            if field[row][column].is_flagged:
                Tile.flag_tile(field[row][column])
            Tile.check_tile(field[row][column])


def print_mine_field(field):
    """Prints a minefield matrix with row and column indices along with borders"""
    print()
    print("\t\tMINESWEEPER")
    string = "    "
    for column in range(len(field[0])):
        if column < 10:
            string = string + "   " + str(column + 1)
        else:
            string = string + "  " + str(column + 1)
    print(string)
    for row in range(len(field)):
        string = "      "
        if row == 0:
            for column in range(len(field[0])):
                string = string + 4 * "\u0332"
            print(string)
        if row < 9:
            string = "  " + str(row + 1) + "  "
        else:
            string = "  " + str(row + 1) + " "
        for column in range(len(field[0])):
            string = string + "| " + str(field[row][column]) + " "
        print(string + "|")
        string = "      "
        if row == len(field) - 1:
            for column in range(len(field[0])):
                string = string + 4 * "\u203E"
            print(string)


def instructions():
    """Prints game instructions"""
    print("1. Enter row and column number to check a tile, (E.g. 3 2) \n"
          "2. Flag/Unflag a tile by entering row and column number followed by F, (E.g. 3 2 F)\n"
          "3. Type Exit at any time to exit the game session")


def game_settings():
    """Lets the user decide the settings for the the coming game session. Returns
    a mine field and the amount of planted mines according to user inputs"""
    print("Decide the format of your game:\n"
          "Choose between 5 to 20 rows, 5 to 30 columns and\n"
          "an amount of mines between 10% and 90% of the total amount of tiles\n"
          "Suggestions:\n"
          "Easy: 9 x 9, 10 mines\n"
          "Medium: 16 x 16, 40 mines\n"
          "Expert: 16 x 30, 99 mines")
    while True:
        try:
            rows = int(input("How many rows? "))
            if rows < 5 or rows > 20:
                print("The number of rows has to be between 5 and 20")
                continue
            columns = int(input("How many columns? "))
            if columns < 5 or columns > 30:
                print("The number of columns has to be between 5 and 30")
                continue
            mines = int(input("How many mines (between " + str(int(round((rows * columns) * 0.1)))
                              + " and " + str(int(round((rows * columns) * 0.9))) + ")? "))
            if mines <= 0:
                print("The number of mines has to be a positive integer")
                continue
            if mines > round((rows * columns) * 0.9):
                print("The number of mines can't exceed 90% of the amount of tiles in the field (rows*columns)")
                continue
            if mines < round((rows * columns) * 0.1):
                print("The number of mines can't be below 10% of the amount of tiles in the field(rows*columns)")
                continue
            mine_field = create_mine_field_matrix(rows, columns)
            mine_placement(mine_field, mines)
            set_proximity(mine_field)
            return mine_field, mines
        except ValueError:
            print("Invalid input, please enter a positive integer")


def end_screen(win, field, mines, start_time, flag_win_counter, correctly_flagged_mines):
    """
    Calculates the time spent on the game and the users score,
    also prints the game ending screen for the user and
    allows saving scores through the save_highscore function.
    """
    end_time = time.time()
    total_time = end_time - start_time
    reveal_field(field)
    print_mine_field(field)
    if win is True:
        print("Congratulations, you cleared all the mines. You win!")
        score = round(60000 * (mines / total_time) + len(field) * len(field[0]))
        print("Your score was:", score, "points")
        save_highscore(score, read_highscores())
        input("press enter to return to the main menu")
    if win is False:
        print("BOOOOOM!\nGAME OVER!\nYou found " + str(correctly_flagged_mines) + " out of",
              mines, "mines")
        score = round(60000 * (flag_win_counter / total_time))
        print("Your score was:", score, "points")
        save_highscore(score, read_highscores())
        input("press enter to return to the main menu")


def game_loop():
    """The game loop that tracks user inputs and continuously prints
     updated versions of the mine field according to said inputs. Also
     tracks win/lose conditions and sets the start point for time tracking"""
    mine_field, mines = game_settings()
    start_time = time.time()
    while True:
        win, flag_win_counter, correctly_flagged_mines = check_win(mine_field, mines)
        if win is True:
            end_screen(True, mine_field, mines, start_time, flag_win_counter, correctly_flagged_mines)
            return
        print_mine_field(mine_field)
        instructions()
        while True:
            choice = input("Check a tile: ").split()
            try:
                if int(choice[0]) <= 0 or int(choice[1]) <= 0:
                    print("Rows and columns cannot be negative or 0")
                    continue
                if len(choice) == 2:
                    if (mine_field[int(choice[0]) - 1][int(choice[1]) - 1].is_checked or
                            mine_field[int(choice[0]) - 1][int(choice[1]) - 1].is_flagged):
                        print("That tile is already checked/flagged, try again")
                    elif mine_field[int(choice[0]) - 1][int(choice[1]) - 1].is_mine:
                        end_screen(False, mine_field, mines, start_time, flag_win_counter, correctly_flagged_mines)
                        return
                    elif mine_field[int(choice[0]) - 1][int(choice[1]) - 1].mines_in_proximity == 0:
                        check_neighbours(int(choice[0]) - 1, int(choice[1]) - 1, mine_field)
                        break
                    else:
                        Tile.check_tile(mine_field[int(choice[0]) - 1][int(choice[1]) - 1])
                        break
                elif len(choice) == 3 and choice[2] == "F":
                    if mine_field[int(choice[0]) - 1][int(choice[1]) - 1].is_checked:
                        print("That tile is already flagged, try again")
                        break
                    else:
                        Tile.flag_tile(mine_field[int(choice[0]) - 1][int(choice[1]) - 1])
                        break
                else:
                    print("That is not a valid tile, try again")
            except ValueError:
                if choice[0] == "Exit" or choice[0] == "exit":
                    return
                else:
                    print("That is not a valid tile, try again")
            except IndexError:
                print("That is not a valid tile, try again")
                continue


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


def print_highscores(highscore_list):
    """Displays the current highscores to the user"""
    print("These are the current highscores, try to beat them!")
    counter = 0
    for element in highscore_list:
        counter += 1
        print(str(counter) + "." + str(element[0]) + ": " + str(element[1]) + " points")
    input("press enter to return to the main menu")


def save_highscore(score, highscore_list):
    """Saves the users score if the score is among the top ten by
    adding score to the accompanying highscore.txt file and then sorting the
    file according to score. Scores below the 10th place are discarded."""
    try:
        if score < highscore_list[9][1]:
            return
    except IndexError:
        pass
    highscore_holder = input("Save your score\nWhats your name?\n")
    highscore_list.append([highscore_holder, score])
    highscore_list.sort(reverse=True, key=lambda x: x[1])
    counter = 0
    with open('highscore.txt', "w+") as highscore_file:
        for element in highscore_list:
            if counter >= 10:
                break
            counter += 1
            highscore_file.write(str(element[0]) + "\n" + str(element[1]) + "\n")


def main_menu():
    """The game's main menu, from here the user can play the game, view highscores
    or exit"""
    menu = {"1": (lambda: game_loop()),
            "2": (lambda: print_highscores(read_highscores()))}
    while True:
        print("Welcome to Minesweeper!")
        print("1. Play Minesweeper \n"
              "2. View High-Scores \n"
              "3. Exit")
        choice = input()
        if choice in menu.keys():
            menu[choice]()
        elif choice == "3":
            print("Good Bye!")
            break
        else:
            print("Invalid input, try again")


if __name__ == '__main__':
    """Starts the program"""
    main_menu()
