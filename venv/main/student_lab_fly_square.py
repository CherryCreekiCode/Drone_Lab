from easytello import tello

myDrone = tello.Tello()

''' 
    Makes the drone take 1 step forward and then turn left or right
    function input:
        'r' or 'l'
    function output none

    the function takes 1 step forward and then makes the turn
'''
def makeTurn(turn):
    print("Drone is turning: " + turn)



''' 
    1. Take off
    2. implement the makeTurn() function
    3. Use a loop to call the makeTurn() function to fly the square
        in the correct direction. 
        Direction is based on this calculation.

        Have a conditional checks battery life
        if battery < 70% fly clockwise square first
        else battery >= 70% fly square counter-clockwise first
    4. Fly square in opposite direction
    5. Land
'''

# START PROGRAM CODE HERE
#myDrone.takeoff()

#print("Batter Power: " + str(bPower))
#for i in range(4):

