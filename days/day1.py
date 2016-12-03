import os
os.chdir("../resources") # Change the current directory
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

file_day1 = open("day1", "r")

where_is_santa = 0

class walker:

    direction = 90;

    x = 0;
    y = 0;

    # Change the currect direction of the walker
    def turn(self, heading):
        if heading == "L":
            self.direction += 90;
        elif heading == "R":
            self.direction -= 90;
        self.direction = self.direction % 360
        return self.direction

    def walk(self, distance):
        if self.direction == 0:
            self.x += distance
            print("Heading East", self.x)
        elif self.direction == 90:
            self.y += distance
            print("Heading North", self.y)
        elif self.direction == 180:
            self.x -= distance
            print("Heading West", self.x)
        elif self.direction == 270:
            self.y -= distance
            print("Heading South", self.y)

    def shortest_path(self):
        return abs(0-self.x) + abs(0-self.y);


    def readfile(self, file):
        data = file_day1.read()
        for i in data.split(", "):
            dist = int(i[1:])
            dir = i[0]
            human.turn(dir);
            human.walk(dist);

        return human.shortest_path()



human = walker()
where_is_bunny = human.readfile(file_day1)

print "Im at", human.x, human.y, "the shortest path is", where_is_bunny



file_day1.close()