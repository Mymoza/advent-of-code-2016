import os
os.chdir("../resources") # Change the current directory
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

file_day2 = open("day2", "r")

class bathroomDoor:

    keys = [
            ['X', 'X', 1, 'X', 'X'],
            [   'X', 2, 3, 4, 'X'],
                [5, 6, 7, 8, 9],
            ['X', 'A', 'B', 'C', 'X'],
            ['X', 'X', 'D', 'X', 'X']
            ]
    x = 2
    y = 0
    numbers = []

    def find_number(self, line):
        for letter in line: # Explore Letter by Letter until the end

            if letter == "U":
                self.y = max(0, self.y - 1) if self.keys[max(0, self.y - 1)][self.x] != 'X' else self.y
            elif letter == "D":
                self.y = min(4, self.y + 1) if self.keys[min(4, self.y + 1)][self.x] != 'X' else self.y
            elif letter == "L":
                self.x = max(0, self.x - 1) if self.keys[self.y][max(0, self.x - 1)] != 'X' else self.x
            elif letter == "R":
                self.x = min(4, self.x + 1) if self.keys[self.y][min(4, self.x + 1)] != 'X' else self.x


    def readfile(self, file):
        for line in file: # Explore line by line
            self.find_number(line)
            (self.numbers).append(str(self.keys[self.y][self.x]))



pee = bathroomDoor()

pee.readfile(file_day2)
print(''.join(pee.numbers))




