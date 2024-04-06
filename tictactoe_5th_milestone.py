import random
grid = ["A1", "A2", "A3",
        "B1", "B2", "B3",
        "C1", "C2", "C3"]
state = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


winning_condition = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
def winning_conditions():
    w = 0
    
    while w < 8:
        if state[winning_condition[w][0]] == state[winning_condition[w][1]] == state[winning_condition[w][2]]:
            return state[winning_condition[w][0]]
        else:
            w = w+1

            



i = 0
rows = ("A","B","C")
column = ("1","2","3")
symbol_choice = input("What do you want to play as? X or O? ")
if symbol_choice == "X":
    while i < 5:
        
        symbol = "X"
        move = input("What's your move? ")
        loc = grid.index(move)
        if state[loc] != " ":
            while state[loc] != " ":
                print("Spot already taken. Pick a new spot.")
                move = input("What's your move? ")
                loc = grid.index(move)
        state[loc] = symbol
        print(state[0], "|", state[1], "|", state[2])
        print("---------")
        print(state[3], "|", state[4], "|", state[5])
        print("---------")
        print(state[6], "|", state[7], "|", state[8])
        if winning_conditions() is "X" or "O":
            print("Winner is", winning_conditions())
            if winning_conditions() == "X":
                i=6
            if winning_conditions() == "O":
                i=6
        if i < 4:
            npc_symbol = "O"
            npc_move = f'{random.choice(rows)}{random.choice(column)}'
            loc = grid.index(npc_move)
            if state[loc] != " ":
                while state[loc] != " ":
                    npc_move = f'{random.choice(rows)}{random.choice(column)}'
                    loc = grid.index(npc_move)

            state[loc] = npc_symbol
            print(f"Computer chose {grid[loc]} for {state[loc]}")
        i = i+1
        print(state[0], "|", state[1], "|", state[2])
        print("---------")
        print(state[3], "|", state[4], "|", state[5])
        print("---------")
        print(state[6], "|", state[7], "|", state[8])
        if winning_conditions() is "X" or "O":
            print("Winner is", winning_conditions())
            if winning_conditions() == "X":
                i=6
            if winning_conditions() == "O":
                i=6
if symbol_choice == "O":
    while i < 6:
        i = i+1
        npc_symbol = "X"
        npc_move = f'{random.choice(rows)}{random.choice(column)}'
        loc = grid.index(npc_move)
        if state[loc] != " ":
             while state[loc] != " ":
                npc_move = f'{random.choice(rows)}{random.choice(column)}'
                loc = grid.index(npc_move)

        state[loc] = npc_symbol
        print(f"Computer chose {grid[loc]} for {state[loc]}")

        print(state[0], "|", state[1], "|", state[2])
        print("---------")
        print(state[3], "|", state[4], "|", state[5])
        print("---------")
        print(state[6], "|", state[7], "|", state[8])
        if winning_conditions() is "X" or "O":
            print("Winner is", winning_conditions())
            if winning_conditions() == "X":
                i=6
            if winning_conditions() == "O":
                i=6
        symbol = "O"
        move = input("What's your move? ")
        loc = grid.index(move)
        if state[loc] != " ":
             while state[loc] != " ":
                print("Spot already taken. Pick a new spot.")
                move = input("What's your move? ")
                loc = grid.index(move)
        state[loc] = symbol
        print(state[0], "|", state[1], "|", state[2])
        print("---------")
        print(state[3], "|", state[4], "|", state[5])
        print("---------")
        print(state[6], "|", state[7], "|", state[8])
        if winning_conditions() is "X" or "O":
            print("Winner is", winning_conditions())
            if winning_conditions() == "X":
                i=6
            if winning_conditions() == "O":
                i=6
if " " not in state:
    print("It's a draw")       
if i == 6:
    print("Game is over")
        
else: print("Symbol does not match please try again.")

    

