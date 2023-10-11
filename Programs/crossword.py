import random

# List of words for the crossword puzzle
word_list = ["python", "challenge", "coding", "puzzle", "algorithm", "developer", "learn", "fun"]

def create_crossword_grid(words):
    # Create a grid with the words intersecting
    grid = [[' ' for _ in range(10)] for _ in range(10)]
    
    for word in words:
        # Try to place each word horizontally or vertically
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row = random.randint(0, 9)
            col = random.randint(0, 10 - len(word))
        else:
            row = random.randint(0, 10 - len(word))
            col = random.randint(0, 9)
        
        for i in range(len(word)):
            grid[row + (i if direction == 'vertical' else 0)][col + (i if direction == 'horizontal' else 0)] = word[i]
    
    return grid

def display_crossword(grid):
    # Display the crossword grid
    for row in grid:
        print(" | ".join(row))
        print("-" * 33)

# Main function
if __name__ == "__main__":
    puzzle_grid = create_crossword_grid(word_list)
    print("Here's your crossword puzzle:")
    display_crossword(puzzle_grid)
