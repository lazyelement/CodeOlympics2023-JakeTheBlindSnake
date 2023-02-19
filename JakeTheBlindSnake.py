def find_food(grid):
    rows = len(grid)
    cols = len(grid[0])
    snake_pos = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == '$'][0]
    path = []
    visited = set()
    
    def dfs(pos):
        if grid[pos[0]][pos[1]] == 'F':
            return True
        visited.add(pos)
        for move in ['up', 'down', 'left', 'right']:
            if move == 'up' and pos[0] > 0 and grid[pos[0]-1][pos[1]] not in ['+', '-', '|'] and (pos[0]-1, pos[1]) not in visited:
                path.append(move)
                if dfs((pos[0]-1, pos[1])):
                    return True
                path.pop()
            elif move == 'down' and pos[0] < rows-1 and grid[pos[0]+1][pos[1]] not in ['+', '-', '|'] and (pos[0]+1, pos[1]) not in visited:
                path.append(move)
                if dfs((pos[0]+1, pos[1])):
                    return True
                path.pop()
            elif move == 'left' and pos[1] > 0 and grid[pos[0]][pos[1]-1] not in ['+', '-', '|'] and (pos[0], pos[1]-1) not in visited:
                path.append(move)
                if dfs((pos[0], pos[1]-1)):
                    return True
                path.pop()
            elif move == 'right' and pos[1] < cols-1 and grid[pos[0]][pos[1]+1] not in ['+', '-', '|'] and (pos[0], pos[1]+1) not in visited:
                path.append(move)
                if dfs((pos[0], pos[1]+1)):
                    return True
                path.pop()
        return False
        
    dfs(snake_pos)
    return ', '.join(path)

grid = [
    ['+', '-', '+', '-', '+', '-', '+'],
    ['|', ' ', ' ', ' ', ' ', ' ', '|'],
    ['+', ' ', '+', '-', '+', ' ', '+'],
    ['|', '  ', ' ', 'F', '|', ' ', '|'],
    ['+', '-', '+', '-', '+', ' ', '+'],
    ['|', '$', ' ', ' ', ' ', ' ', '|'],
    ['+', '-', '+', '-', '+', '-', '+']
]

# Call the function and print the result
path = find_food(grid)
print(path)
