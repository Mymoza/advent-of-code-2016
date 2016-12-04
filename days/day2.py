import os
os.chdir("../resources") # Change the current directory
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

file_day2 = open("day2", "r")

class bathroomDoor:

    keys = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
            ]
    x = y = 1
    numbers = []

    def find_number(self, line):
        for letter in line: # Explore Letter by Letter until the end

            if letter == "U":
                self.y = max(0, self.y - 1)
            elif letter == "D":
                self.y = min(2, self.y + 1)
            elif letter == "L":
                self.x = max(0, self.x - 1)
            elif letter == "R":
                self.x = min(2, self.x + 1)


    def readfile(self, file):
        for line in file: # Explore line by line
            self.find_number(line)
            (self.numbers).append(str(self.keys[self.y][self.x]))



pee = bathroomDoor()

pee.readfile(file_day2)
print(''.join(pee.numbers))




