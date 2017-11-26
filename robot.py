
#Let the user input the command sequence
comm = raw_input("Enter commands: ")

#I gave the directions numerical values so I can use modulo 4 to turn 90 deg
directions = {
	0: "EAST",
	1: "NORTH",
	2: "WEST",
	3: "SOUTH"
}

#set the table dimensions
table_width = 5
table_length = 5

class Robot:
    def __init__(self):
        self.x_pos = None
        self.y_pos = None
        self.orientation = None
        self.placed = False

    def report(self):
        print "My current position is {0},{1},{2}".format(self.x_pos, self.y_pos, directions[self.orientation])

    def move(self):
    	#python doesn't have swith-case, so I use if-elif
    	if self.orientation == 0 and self.x_pos < table_width-1:
    		self.x_pos += 1
    	elif self.orientation == 1 and self.y_pos < table_length-1:
    		self.y_pos += 1
    	elif self.orientation == 2 and self.x_pos > 0:
    		self.x_pos -= 1
    	elif self.orientation == 3 and self.y_pos > 0:
    		self.y_pos -= 1
    	else:
    		print "Cannot move there, ignoring 'MOVE'command"

    def place(self, x_pos, y_pos, orientation):
        if x_pos < table_width and y_pos < table_length:
            self.x_pos = x_pos
            self.y_pos = y_pos
            self.orientation = orientation
            self.placed = True
        else:
            print "Cannot place the robot there, ignoring 'PLACE' command"

    def right(self):
    	self.orientation = (self.orientation - 1) % 4

    def left(self):
    	self.orientation = (self.orientation + 1) % 4

#parse the commande sequence
command_list = comm.split()

#Merge the PLACE command with its arguments, so
# PLACE 0,0,NORTH REPORT becomes PLACE0,0,NORTH REPORT
for command in command_list:
	if command == "PLACE":
		current_index = command_list.index(command)
		command_list[current_index] = command + command_list[current_index + 1]
		del command_list[current_index + 1]

def parse_place_command(command):
    x,y,initial_direction = command.split(",")
    x_pos = int(x[5:])
    y_pos = int(y)
    for dir_index, d in directions.iteritems():
    	if d==initial_direction:
    		orientation = dir_index
    return x_pos, y_pos, orientation

r = Robot()

for command in command_list:
    if command[:5]=="PLACE":
        try:
            x_pos, y_pos, orientation = parse_place_command(command)
            r.place(x_pos, y_pos, orientation)
        except:
            print command + " is not a valid 'PLACE' command, please check the parameters"
    elif r.placed:
    	if command=="MOVE":
    		r.move()
    	elif command=="REPORT":
    		r.report()
    	elif command=="RIGHT":
    		r.right()
    	elif command=="LEFT":
    		r.left()
    	else:
    		print command + " is not a valid command"
    else:
        print "The robot is not yet placed, ignoring the '" + command + "' command"
