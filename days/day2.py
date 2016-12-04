import os
os.chdir("../resources") # Change the current directory
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

file_day2 = open("day2", "r")

class bathroomDoor:

    keys = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    x = y = 1

    def find_number(self, line):
        action = 0
        for letter in str(line): # Explore Letter by Letter until the end
            if letter == "U":
                action = -3
            elif letter == "D":
                action = 3
            elif letter == "L":
                action = -1
            elif letter == "R":
                action = 1

            if (self.current_pos + action) > 0 and (self.current_pos + action) < 10:
                self.current_pos += action

        print "current pos", self.current_pos
        return self.current_pos


    def readfile(self, file):
        c = file.readlines() #Read lines
        result = ""
        for line in c: # Explore line by line
            result += str(self.find_number(c))
        return result



pee = bathroomDoor()

result = pee.readfile(file_day2)
print result




