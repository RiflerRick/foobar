def answer(maze):
    # calculate height and width
    height = len(maze)
    width = len(maze[0])
    # dimensions tuple, (h, w) aka (width, height)
    dimensions = (height, width)

    # calculate removable walls
    removeable_walls = get_removeable_walls(maze, dimensions)

    print('removable walls: '+str(removeable_walls))
    print('count: '+str(len(removeable_walls)))

    shortest_path = 100000  # make it a very big int

    # Build a list of all possible mazes including one without removing
    # any walls, i am using list comprehensions to make a copy of list of list
    maze_list = []  # list of all possible mazes
    maze_list.append([x[:] for x in maze])  # add provided maze in list

    temp_maze = [x[:] for x in maze]

    # make all possible mazes with possible wall removed
    for wall in removeable_walls:
        h, w = wall
        new_maze = [x[:] for x in temp_maze]
        new_maze[h][w] = 0  # remove a wall
        # add it to list of mazes
        maze_list.append([x[:] for x in new_maze])

    # calculate the shortest distance in each maze we have in maze list
    for maze_item in maze_list:
        # make a graph from maze
        graph = make_graph(maze_item, dimensions)
        # calculate shortest path for a maze
        path = bfs(graph, 1, width*height)
        # if path is shorter then existing path, it is shortest path
        if path is not None:
            path_len = len(path)
            if path_len < shortest_path:
                shortest_path = path_len

    return shortest_path


def make_graph(maze, dimensions):
    """
    Makes a graph from given maze
    """
    height, width = dimensions
    graph = {}
    count = 0
    # h, w are the pos of items in maze
    h = -1
    w = -1
    for row in maze:
        w = -1
        h = h + 1
        for item in row:
            w = w + 1
            item_pos = (h, w)
            count = count + 1
            if item is 0:
                N, E, S, W = get_adj_items(maze, dimensions, item_pos)
                # if we can go to an item from current position, 
                # find count of that position
                # N -> count - width, E -> count + 1
                # S -> count + width, W -> count - 1
                graph[count] = []
                if N is 0:
                    graph[count].append(count - width)
                if E is 0:
                    graph[count].append(count + 1)
                if S is 0:
                    graph[count].append(count + width)
                if W is 0:
                    graph[count].append(count - 1)
    return graph


def get_removeable_walls(maze, dimensions):
    """
    get walls that can be removed and used as path
    if a "1" have two "0" adjacent to It
    we can remove and walk from there
    """
    walls = []
    removeable_walls = []
    # iterate over items and get walls
    h = -1
    w = -1
    for row in maze:
        w = -1
        h = h + 1
        # print row
        for item in row:
            w = w + 1
            item_pos = (h, w)
            if item:
                walls.append(item_pos)

    for wall in walls:
        if is_removable(maze, dimensions, wall):
            removeable_walls.append(wall)

    return removeable_walls


def is_removable(maze, dimensions, wall):
    """
    given a wall on maze it finds if it is removable or not
    """
    # if we have more then two "1's" wall is not breakable
    N, E, S, W = get_adj_items(maze, dimensions, wall)
    if (N+E+S+W) <= 2:
        return True

    return False


def get_adj_items(maze, dimensions, pos):
    """
    finds the adjacent items of a position
       N
    W pos E
       S
    N -> North; E-> East; S-> South; W-> West
    """
    height, width = dimensions
    h, w = pos

    # Variables to find adjacent items
    N_h = h-1
    E_w = w+1
    S_h = h+1
    W_w = w-1

    # N_h = h-1 & check if h-1 < 0 if yes pos is not walkable
    # E_w = w+1 & check if w+1 >= width of Maze if yes pos is not walkable
    # S_h = h+1 & check if h+1 >= height of Maze if yes pos is not walkable
    # W_w = w-1 & check if w-1 < 0 if yes pos is not not walkable

    # check for North side
    if N_h < 0:
        # print "North wall is hit"
        N = 1
    else:
        N = maze[N_h][w]

    # check the East side
    if E_w >= width:
        # print "East wall is hit"
        E = 1
    else:
        E = maze[h][E_w]

    # check for South side
    if S_h >= height:
        # print "South wall is hit"
        S = 1
    else:
        S = maze[S_h][w]

    # check the West side
    if W_w < 0:
        # print "West wall is hit"
        W = 1
    else:
        W = maze[h][W_w]

    return N, E, S, W


def bfs(graph_to_search, start, end):
    """
    Breadth-first search with visited node remembered
    """
    queue = [[start]]
    visited = set()

    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)
        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # We check if the current node is already in the visited nodes set in
        # order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it
            # into the queue
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

                # No need to visit other neighbour. Return at once
                if current_neighbour == end:
                    return new_path

            # Mark the vertex as visited
            visited.add(vertex)


# Ans = 11
# maze = [[0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0]]

# Ans = 6
# maze = [[0, 1, 1, 0],
#         [0, 0, 1, 0],
#         [1, 0, 1, 0]]

# Ans = 7
# maze = [[0, 1, 1, 0],
#         [0, 0, 0, 1],
#         [1, 1, 0, 0],
#         [1, 1, 1, 0]]

# Ans = 27
maze = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Ans = 33
# maze = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# maze = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print (answer(maze))
# print(answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))