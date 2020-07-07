def board_func(player, locations): #uses the player and location dictionary as inputs

    while(True): #asks the player where they want to place their move. If the move is valid then then store it in location dictionary with the same name and break the loop. Else loop.
        player["move"] = input(player["name"] + ", where would you like to place your move?")
        if(player["move"] in locations):
            locations[player["move"]] = player["symbol"]
            break
        else:
            print("Sorry " + player["move"] + " is not a vaild location, try again.")

    board_print(locations) #use the function to print out the board

    board_check(player, locations) #use the function to check weather there is a winning pattern




def board_check(player, locations): #uses the player and location dictionary as inputs

    if(locations["tl"] == locations["tc"] == locations["tr"] or #checks horizontal, vertical and diagonal patterns of symbols respectively.
       locations["ml"] == locations["mc"] == locations["mr"] or
       locations["bl"] == locations["bc"] == locations["br"] or
       locations["tl"] == locations["ml"] == locations["bl"] or
       locations["tc"] == locations["mc"] == locations["bc"] or
       locations["tr"] == locations["mr"] == locations["br"] or
       locations["tl"] == locations["mc"] == locations["br"] or
       locations["tr"] == locations["mc"] == locations["bl"]):

        print("Congratulations " + player["name"] + "! You won the game! :)") #if any of the patterns match then a print statement congrtulates the winning player
        player["winner"] = "yes" #change winner in player dictionary to yes which helps stop a loop


def board_print(locations): #takes in location dictionary as input and prints each location in a presentable way

    print( f"""
    {locations["tl"]} | {locations["tc"]} | {locations["tr"]}
    ------------
    {locations["ml"]} | {locations["mc"]} | {locations["mr"]}
    ------------
    {locations["bl"]} | {locations["bc"]} | {locations["br"]}\n""")


board_locations = {"tl" : "tl", "tc" : "tc", "tr" : "tr", #dictionary for storing the locations of the tic tac toe board
                   "ml" : "ml", "mc" : "mc", "mr" : "mr",
                   "bl" : "bl", "bc" : "bc", "br" : "br"}

player1 = {"name": "", "symbol": "", "move": "", "player_no": "1", "winner": "no"} #dictionary for each of the two players storing various information
player2 = {"name": "", "symbol": "", "move": "", "player_no": "2", "winner": "no"}


print("Hello! Welcome to this simple tic tac toe game!\n") #greeting message

player1["name"] = input("Player1 enter your name: ") #player name

while(True): #ask player1 what symbol they would like to use, if its valid break the loop, else print a message and loop.
    player1["symbol"] = input("Hey " + player1["name"] + ", what symbol would you like to play with?(Enter o or x): " )

    if(player1["symbol"] == "X" or player1["symbol"] == "x" or player1["symbol"] == "O" or player1["symbol"] == "o"):
        break
    else:
        print(player1["symbol"] + " is not a valid symbol, please enter a valid symbol.")

player2["name"] = input("\nPlayer2 enter your name: ") #ask player2 for their name

if(player1["symbol"] == "x" or player1["symbol"] == "X"): #store the opposite of player1's symbol for player2
    player2["symbol"] = "O"

else:
    player2["symbol"] = "X"

turns = 0 #variable to keep track of turns

board_print(board_locations)#print board using function

while(player1["winner"] == "no" and player2["winner"] == "no"): #loop stops when either player's winner key changes or satisfies first if condition

    if(turns == 9): #if condition to print out a message stating its a draw when the board fills up and then breaks from the loop
        print("Tough luck! Its a draw. :(")
        break

    elif(turns % 2 == 0): #Player1 and player2 switch between turns depending on weather turns variable is positive or negative.
        board_func(player1, board_locations)#calls the board_func function and then adds to the turns variables.
        turns += 1
    else:
        board_func(player2, board_locations)
        turns += 1
