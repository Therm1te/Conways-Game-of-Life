import random
import os
import time

class game:

    grid = []
    file_name = ""

    def main(self):
        self.file_open()

        generations = int(input("Enter the number of generations to simulate: "))

        for generation in range(0, generations):
            population = sum(sum(row) for row in self.grid)
            self.convert_grid(self.grid, generation, population)
            time.sleep(0.5)
            self.grid, _ = self.compute_generation(self.grid)
        
        self.file_save(self.grid)

    def rand_matrix_gen(self, grid_rows, grid_columns):
        
        for f in range(grid_rows):
            row = " "
            for i in range(grid_columns):
                r = random.randint(0, 10)
                
                if r == 0:
                    row += ". " 
                elif r == 1:
                    row += "O "

                else:
                    row += ". "

            print(row)

    # This function handles the file operations.

    def file_open(self):
        
        # Saving the file name as a character array, instead of storing it as a string object, to fulfil the project requirement.

        file_name_array = list(input("Enter file name with extension to parse as source file."))

        for i in file_name_array:
            self.file_name = self.file_name + i
        
        if len(self.file_name) < 20:
            try:
                with open(self.file_name, 'r') as f:
                    for line in f:
                        self.grid.append(list(map(int, line.split())))

            except FileNotFoundError as e:
                print(print("The file you entered doesn't exist. :("))
        else:
            print("Invalid File Name, Please check input criteria.")

    # This function converts from binary to matrix.

    def convert_grid(self, grid, generation, population):

        os.system('cls')
        print(f"Generation: {generation + 1}, Population: {population}\n")
        for row in grid:
            print(" ".join(['O' if cell else '.' for cell in row]))


    def count_live_neighbors(self, grid, x, y):

        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        ]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                count += grid[nx][ny]
        return count


    def compute_generation(self, grid):

        new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.population = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                live_neighbors = self.count_live_neighbors(grid, x, y)
                if grid[x][y] == 1:
                    if live_neighbors in [2, 3]:
                        new_grid[x][y] = 1
                        self.population += 1
                else:
                    if live_neighbors == 3:
                        new_grid[x][y] = 1
                        self.population += 1
        return new_grid, self.population
    
    def file_save(self, grid):
        with open(self.file_name, 'w') as f:
            for row in grid:
                f.write(" ".join(map(str, row)) + "\n")

game().main()


