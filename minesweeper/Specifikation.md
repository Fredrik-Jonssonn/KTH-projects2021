# Specifikation

## Inledning
Jag har valt att programmera P-uppgift 168: Minröjning. En version
av programmet skall köras i en terminal och en version med ett
grafiskt användargränssnitt. Användaren presenteras först med en meny
där hen kan avsluta programmet, öppna en tio-i-topp-lista över bästa
spelare hitills och starta spelet. Väljer användaren att 
starta spelet presenteras hen med en inställningsmeny
där hen får bestämma spelets format, dvs antalet rader, kolumner och minor.
Sedan startas spelet, en matris med rutor presenteras och användaren  kan börja undersöka 
rutorna genom att öppna upp dem och flagga dem för minor. När en ruta öppnas upp
visar den hur många minor som finns i angränsande rutor. Öppnar användaren upp
ruta med 0 angränsande minor öppnas hela det sammanhängande område med rutor utan angränsande
minor samt kanten på detta område bestående av rutor med siffror upp. Användaren vinner när
antingen alla minor är flaggade eller om alla rutor utan minor har öppnats. Användaren förlorar
om hen öppnar upp en ruta med en mina. När spelet avslutas räknas användarens
poäng ut och om poängen platsar på tio-i-topp-listan får hen möjlighet att spara
sitt poäng i listan. 

En av de största utmaningarna är att hantera användarens inmatningar, eftersom ett
stort antal objekt påverkas av en enda inmatning. T.ex att alla angränsande rutor
öppnas upp när en ruta med 0 angränsande minor öppnas upp eller att skapa
ett spelfält enligt användarens specifikationer.
Även att skapa en klass som lagrar all nödvändig information om en ruta lär ta en hel del tid att utforma. 
Eftersom alla angränsande rutor påverkar varandra i någon utsträckning och det medför många
risker att något blir fel. 

## Användarscenario
Oskar skall spela Minesweeper. Oskar startar programmet och möts av en huvudmeny, han ser
att det finns en "highscore" lista och blir nyfiken på vilka som har platsat på listan. Han 
väljer därför "View Highscores" i menyn och möts av en tio-i-topp-lista. Han vill gärna
själv hamna på topplistan och noterar därför att han måste få mer än 5000 poäng i spelet för att slå
ut Olle som just nu ligger på plats tio. Han återgår till huvudmenyn och den här gången väljer han "Play Minesweeper" och
bes mata in hur många rader, kolumner och minor som skall finnas i hans spel. Det visas
även några förslag på olika svårighetsgrader, Oskar väljer "Medium" svårighetsgraden med
16 rader, 16 kolumner och 40 minor. Spelet startas och ett minfält ritas upp tillsammans med
instruktioner för spelet. Oskar bes undersöka en ruta genom att mata in rutans position
i fältet (rad, kolumn). Han väljer rutan på rad 1 kolumn 1. Tyvärr träffade Oskar en mina direkt
och förlorar utan att få några poäng alls. Hela minfältet visar sig och Oskar återvänder till
Huvudmenyn. Utan att ge upp startar Oskar ett nytt spel med samma inställningar. Återigen väljer han
rutan på rad 1 kolumn 1, men denna gång var rutan tom med 0 angränsande minor och
en stor del av fältet öppnar upp upp sig. Han undersöker fler rutor och flaggar de rutor
där han ser att det måste finnas minor genom att mata in ett F efter rutans position i matrisen
tills han tillslut har flaggat alla minor. Oskar vinner därmed
och får 5500 poäng. Eftersom det var mer än Olles 5000 poäng får Oskar en möjlighet att spara
sina poäng i tio-i-topp-listan innan han sedan återvänder till huvudmenyn. Han väljer återigen
"View Highscores" och ser han nu har tionde platsen. Nöjd med sin insats återvänder han
till huvudmenyn och väljer sedan "exit" vilket avslutar spelet.

## Kodskelett
Detta är ett skelett för den terminalbaserade versionen av spelet, den grafiska versionen
kommer utgå ifrån samma funktioner, men då såklart anpassade för tkinter.
```
class Tile:
    """Describes a tile of a minefield. Stores information about how many mines
    are in proximity, if the tile has a mine planted on it, if it has been
    checked by a user and if it has been flagged by the user."""

    def __init__(self):
        """The constructor for a tile that creates an empty tile"""
    
    def __repr__(self):
        """Returns a string that gives the information about the tile that
         the user has access to."""

    def check_tile(self):
        """Method that tracks if a tile is checked during the game"""

    def plant_mine(self):
        """Method for planting a mine on a tile"""

    def add_mine_in_proximity(self):
        """Method that increases the amount of mines in the proximity
        of the tile by 1."""
    
    def flag_tile(self):
        """Method that tracks if a tile is flagged/unflagged during the game"""

def create_mine_field_matrix(rows, columns):
    rows = amount of rows in the matrix. Columns = amount of columns in the matrix
    """Creates and returns a 2d list of tile objects, i.e the matrix
    that will act as the mine field"""

def mine_placement(field, mines):
    field = a matrix of tile objects, i.e the field where the mines are placed
    mines = chosen amount of mines to be placed
    """Randomly places the chosen amount of mines in a matrix of tile objects"""

def set_proximity(field):
    field = a matrix of tile objects, i.e the the mine field
    """Calculates and stores the amount of mines that are in adjacent tiles
    for every tile in a matrix of Tile objects"""

def check_neighbours(row, column, field):
    row = The tile row in the mine field. Column = the tile column in the mine field
    field = a  matrix of tile objects, i.e the the mine field
    """Recursively checks the entire continuous part of them minefield consisting
    of all neighboring tiles to tiles with with zero mines in
    proximity"""

def check_win(field, mines):
    field = a matrix of tile objects, i.e the the mine field
    mines = the amount of mines in the field
    """Returns the amount of correctly flagged mines, the sum
    correctly flagged mines - incorrectly flagged mines (flag_win_counter)
    and a boolean: True if the minefield satisfies one of two
    win conditions, either having all non-mine tiles checked
    or having all mine-tiles flagged. False otherwise."""

def reveal_field(field):
    field = a matrix of tile objects, i.e the the mine field
    """Reveals the entire mine field by checking all of the tiles"""

def print_mine_field(field):
    field = a matrix of tile objects, i.e the the mine field
    """Prints a minefield matrix with row and column indices along with borders"""

def instructions():
    """Prints game instructions"""

def game_settings():
    """Lets the user decide the settings for the the coming game session. Returns
    a mine field and the amount of planted mines according to user inputs"""

def end_screen(win, field, mines, start_time, flag_win_counter, correctly_flagged_mines):
    win = True or False whether or not the user won or lost
    field = a matrix of tile objects, i.e the the mine field
    mines = the amount of mines in the field
    start_time = the time when the game session started
    flag_win_counter = the sum correctly flagged tiles - incorrectly flagged tiles (used for score
    calculations).
    correctly_flagged_tiles = the amount of correctly flagged tiles
    """
    Calculates the time spent on the game and the users score,
    also prints the game ending screen for the user and
    allows saving scores through the save_highscore function.
    """

def game_loop():
    """The game loop that tracks user inputs and continuously prints
     updated versions of the mine field according to said inputs. Also
     tracks win/lose conditions and sets the start point for time tracking"""

def read_highscores():
    """Reads the accompanying highscore.txt file and
     returns a 2d list where each element consists of the
     highscore holder and the score"""

def print_highscores(highscore_list):
    highscore_list = The 2d list created in read_highscores()
    """Displays the current highscores to the user"""

def save_highscore(score, highscore_list):
    score = the score calculated in end_screen()
    highscore_list = The 2d list created in read_highscores()
    """Saves the users score if the score is among the top ten by
    adding score to the accompanying highscore.txt file and then sorting the
    file according to score. Scores below the 10th place are discarded."""

def main_menu():
    """The game's main menu, from here the user can play the game, view highscores
    or exit"""

main_menu()
```
## Programflöde och dataflöde
Programmet börjar med att presentera huvudmenyn för användaren. Från huvudmenyn kan
användaren välja:
1. "Play Minesweeper". Vilket startar game_loop funktionen som i sin tur skapar 
ett minfält genom ett anrop till game_settings() där användaren bes mata in spelets format
(rader, kolumner, antal minor). game_settings() anropar sedan create_mine_field_matrix() med
argument som användaren matade in. Detta minfält är en 2d matris bestående av tomma tileobjekt.
Alltså rutor (tileobjekt) utan minor, som inte är flaggade, som inte är undersökta och som inte har några
angränsande minor. Sedan körs mine_placement() och set_proximity() med minfältet som argument.
Dessa funktioner som placerar slumpmässig ut antalet minor i fältet som användaren valde samt sedan räknar ut
hur många angränsande minor varje ruta har och lagrar den informationen genom att köra
metoderna plant_mine(self) och add_mine_in_proximity(self). Åter i game_loop() startas nu en loop
som för varje iteration: kollar om användaren vunnit via check_win(), kör instructions(),
kör print_mine_field() samt ber användaren att antingen öppna/flagga en ruta. Att användaren öppnar/flaggar
en ruta innebär att metoderna check_tile respektive flag_tile körs. Öppnar användaren en ruta utan angränsande minor
körs reveal_neighbours() vilket öppnar upp hela det sammanhängande område med rutor utan angränsande
minor samt kanten på detta område bestående av rutor med siffror. Om nu användaren vinner
eller förlorar körs reveal_field() och print_mine_field() vilket visar hela fältet för användaren samt end_screen()
som berättar för användaren om hen har vunnit/förlorat samt räknar ut och visar hens poäng. Sedan körs save_highscore()
med read_highscore och användarens poäng
som argument. Är poängen tillräckligt bra för att platsa på tio-i-topp-listan bes
användaren att mata in sitt namn, vilket sparas tillsammans med poängen i en textfil.
Sedan kan användaren återvända till huvudmenyn.


2. "View Highscores". Vilket kör funktionen print_highscore med funktionen read_highscores som argument
vilket visar en tio-i-topp-lista för användaren. Sedan kan användaren återvända till huvudmenyn

3. "Exit". Vilket avslutar programmet