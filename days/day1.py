import os
os.chdir("../resources") # Change the current directory
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

file_day1 = open("day1", "r")

where_is_santa = 0

class walker:

    direction = 90;

    pos_list = []

    x = 0;
    y = 0;

    part2_foundit = False
    part2 = 0

    # Change the currect direction of the walker
    def turn(self, heading):
        if heading == "L":
            self.direction += 90
        elif heading == "R":
            self.direction -= 90
        self.direction = self.direction % 360
        return self.direction

    def walk(self, distance):
        for i in range(distance):
            if self.direction == 0:
                self.x += 1
            elif self.direction == 90:
                self.y += 1
            elif self.direction == 180:
                self.x -= 1
            elif self.direction == 270:
                self.y -= 1

            if {self.x, self.y} not in self.pos_list:  #If the coords are not already in the list
                self.pos_list.append({self.x, self.y})

            elif self.part2_foundit is False:
                # If I had more time this should be made cleaner lol ...
                part2 = self.shortest_path()
                self.part2_foundit = True
                print "part2 answer is ",part2
                break;



    def shortest_path(self):
        return abs(0-self.x) + abs(0-self.y);


    def readfile(self, file):
        data = file_day1.read()
        for i in data.split(", "):
            dist = int(i[1:])
            dir = i[0]
            human.turn(dir)
            human.walk(dist)

        return human.shortest_path()



human = walker()
where_is_bunny = human.readfile(file_day1)






file_day1.close()