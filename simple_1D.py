Web VPython 3.2

# from vpython import *  # If running on Python

# Initialize your vectors
xi = vector(-15,0,0)
vi = vector(5,0,0)
ai = vector(1,0,0)

# Initialize time
t = 0; dt = 0.1; tMax = 5

# Draw a canvas
scene = canvas(width=600, height=300, autoscale = False)

# Make a box at position xi and name it 'block'
#block = box(pos=xi, vel=vi, acc=ai)
block = box(pos=xi)
block.vel = vi  # Give a velocity to 'block'. 
block.acc = ai
block.color = color.green
# 'vel' and 'acc' are properties of 'block' (object-oriented programming).

# Create a graph
gd = graph(width=600, height=200, xmin=0, xmax=tMax, xtitle='Time', ytitle='Position')
line = gcurve(color=color.green,label='x position')

# Let's count time
# The loop increments t by dt till it reaches t = tMax.
while t < tMax:
    sleep(dt)
    
    # Increment the velocity in infinitesimal time.
    block.vel = block.vel + block.acc*dt
    # Increment the position in infinitesimal time.
    block.pos = block.pos + block.vel*dt
    # Update the plot
    line.plot(t, block.pos.x)
    
    t = t + dt # Update the current time.
    
