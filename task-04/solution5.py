# Input the grid and words
grid = [list(input().strip()) for _ in range(10)]
words = input().strip().split(';')

# Initialize variables for recursion
stack = [(grid, 0)]  # Stack to hold the grid state and the current word index

while stack:
    current_grid, index = stack.pop()

    if index == len(words):  # If all words are placed, print the solution and exit
        for row in current_grid:
            print("".join(row))
        exit()

    word = words[index]  # Current word to place

    for row in range(10):
        for col in range(10):
            # Check if the word can be placed horizontally
            if col + len(word) <= 10:
                can_place = True
                for i in range(len(word)):
                    if current_grid[row][col + i] not in ('-', word[i]):
                        can_place = False
                        break

                if can_place:  # Place the word horizontally
                    temp_grid = [r[:] for r in current_grid]  # Create a copy of the grid
                    for i in range(len(word)):
                        temp_grid[row][col + i] = word[i]
                    stack.append((temp_grid, index + 1))  # Add the new state to the stack

            # Check if the word can be placed vertically
            if row + len(word) <= 10:
                can_place = True
                for i in range(len(word)):
                    if current_grid[row + i][col] not in ('-', word[i]):
                        can_place = False
                        break

                if can_place:  # Place the word vertically
                    temp_grid = [r[:] for r in current_grid]  # Create a copy of the grid
                    for i in range(len(word)):
                        temp_grid[row + i][col] = word[i]
                    stack.append((temp_grid, index + 1))  # Add the new state to the stack
