def board_func(player, locations):

    while(True):
        player["move"] = input(player["name"] + ", where would you like to place your move?")
        if(player["move"] in locations): 
            locations[player["move"]] = player["symbol"]
            break
        else:
            print("Sorry " + player["move"] + " is not a vaild location, try again.")
        
    board_print(locations)

    board_check(player, locations)


    

def board_check(player, locations):
        
    if(locations["tl"] == locations["tc"] == locations["tr"] or
       locations["ml"] == locations["mc"] == locations["mr"] or
       locations["bl"] == locations["bc"] == locations["br"] or
       locations["tl"] == locations["ml"] == locations["bl"] or
       locations["tc"] == locations["mc"] == locations["bc"] or
       locations["tr"] == locations["mr"] == locations["br"] or
       locations["tl"] == locations["mc"] == locations["br"] or
       locations["tr"] == locations["mc"] == locations["bl"]):

        print("Congratulations " + player["name"] + "! You won the game! :)")
        player["winner"] = "yes"


def board_print(locations):
    
    print( f"""
    {locations["tl"]} | {locations["tc"]} | {locations["tr"]}
    ------------
    {locations["ml"]} | {locations["mc"]} | {locations["mr"]}
    ------------
    {locations["bl"]} | {locations["bc"]} | {locations["br"]}\n""")
    

board_locations = {"tl" : "tl", "tc" : "tc", "tr" : "tr",
                   "ml" : "ml", "mc" : "mc", "mr" : "mr",
                   "bl" : "bl", "bc" : "bc", "br" : "br"}

player1 = {"name": "", "symbol": "", "move": "", "player_no": "1", "winner": "no"}
player2 = {"name": "", "symbol": "", "move": "", "player_no": "2", "winner": "no"}


print("Hello! Welcome to this simple tic tac toe game!\n")

player1["name"] = input("Player1 enter your name: ")

while(True):
    player1["symbol"] = input("Hey " + player1["name"] + ", what symbol would you like to play with?(Enter o or x): " )

    if(player1["symbol"] == "X" or player1["symbol"] == "x" or player1["symbol"] == "O" or player1["symbol"] == "o"):
        break
    else:
        print(player1["symbol"] + " is not a valid symbol, please enter a valid symbol.")

player2["name"] = input("\nPlayer2 enter your name: ")

if(player1["symbol"] == "x" or player1["symbol"] == "X"):
    player2["symbol"] = "O"

else:
    player2["symbol"] = "X"

players_turn = 1

board_print(board_locations)

while(player1["winner"] == "no" and player2["winner"] == "no"):
    if(players_turn == 1):
        board_func(player1, board_locations)
        players_turn = 2
    else:
        board_func(player2, board_locations)
        players_turn = 1
        
        











