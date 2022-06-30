from collections import deque

import maze_puzzle as mp


# Function to find a route using the Depth-first Search algorithm.

# Depth-first search is an algorithm used to traverse a tree or generate nodes and paths in a tree. This algorithm
# starts at a specific node and explores paths of connected nodes of the first child and does this recursively until
# it reaches the furthest leaf node before backtracking and exploring other paths to leaf nodes via other child nodes
# that have been visited.

# Although the Depth-first search algorithm van be implemented with a recursive function. This implementation is
# achieved using a stack to better represent the order of operations as to which nodes get visited and processed.
# It is important to keep track of the visited points so that the same nodes do not get visited unnecessarily and
# create cyclic loops.
def run_dfs(maze_game, root_point, visited_points):
    # TODO: Dla podstawowej postaci labiryntu wynik powinien być identyczny jak w BFS.
    stack = deque()
    stack.append(root_point)
    while stack:
        current_point = stack.popleft()
        if not is_in_visited_points(current_point, visited_points):
            visited_points.append(current_point)
            if maze_game.get_current_point_value(current_point) == '*':
                    return current_point
            else:
                neighbors = maze_game.get_neighbors(current_point)
                for neighbor in neighbors:
                    neighbor.set_parent(current_point)
                    stack.appendleft(neighbor)

    return False


# Function to determine if the point has already been visited
def is_in_visited_points(current_point, visited_points):
    for visited_point in visited_points:
        if current_point.x == visited_point.x and current_point.y == visited_point.y:
            return True
    return False


def start_dfs(maze_game_main, x, y):
    print('---Depth-first Search---')

    # Initialize a MazePuzzle
    # Run the depth first search algorithm with the initialized maze
    starting_point = mp.Point(x-1, y-1)
    outcome = run_dfs(maze_game_main, starting_point, [])

    # Get the path found by the depth first search algorithm
    if not run_dfs(maze_game_main, starting_point, []):
        print("\n-----No path to the goal found.-----\n")

    else:
        print("\n-----WYNIK-----\n")
        dfs_path = mp.get_path(outcome)

        # Print the results of the path found
        print('Path Length: ', len(dfs_path))
        maze_game_main.overlay_points_on_map(dfs_path)
        print('Path Cost: ', mp.get_path_cost(outcome))
        for point in dfs_path:
            print('Point: ', point.x, ',', point.y)

