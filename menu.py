import maze_bfs as bfs
import maze_dfs as dfs
import maze_puzzle as mp
import time

print("-----------------------------------")
print("             MAZE GAME             ")
print("-----------------------------------")

while True:

    print("\n\nWYBIERZ OPCJE: ")
    print("0. EXIT")
    print("1. DZIALANIE PROGRAMU")

    wybor = int(input("Wybor: "))
    print("\n\n\n")
    if wybor == 0:
        exit(0)
    elif wybor == 1:
        x = int(input("Podaj wymiary Labiryntu - x: "))
        y = int(input("Podaj wymiary Labiryntu - y: "))
        print("")

        maze_game_main = mp.MazePuzzle(x, y)

        print("-------------------------BFS------------------------")
        start = time.time()
        bfs.start_bfs(maze_game_main, x, y)
        end = time.time()
        print("\nTIME:")
        print(end-start)
        print("\n-------------------------DFS------------------------")
        start2 = time.time()
        dfs.start_dfs(maze_game_main, x, y)
        end2 = time.time()
        print("\nTIME:")
        print(end2 - start2)
