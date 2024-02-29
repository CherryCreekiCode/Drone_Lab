from easytello import tello
myDrone = tello.Tello()

''' 
    Makes the drone take 1 step forward and then turn left or right
    function input:
        'r' or 'l'
    function output none

    the function makes the turn and one step forward
'''


def makeTurn(turn):
    print("Drone is turning: " + turn)
    myDrone.forward(60)
    if turn == 'l':
        myDrone.ccw(90)
    elif turn == 'r':
        myDrone.cw(90)
    else:
        print("ERROR BAD INPUT. CANNOT TURN")

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
myDrone.takeoff()

bPower = myDrone.get_battery()
print("Batter Power: " + str(bPower))
for i in range(4):
    if bPower < 80:
        makeTurn('r')
    else:
        makeTurn('l')

myDrone.land()



