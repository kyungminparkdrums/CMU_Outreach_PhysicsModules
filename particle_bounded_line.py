Web VPython 3.2
# from vpython import *  # If running on Python

'''
Particle on a bounded line

Particle (ball) moves on a line with boundary.
When the particle hits the boundary, velocity vector is flipped and its magnitude decreases by 20%.
Velocity vector is attached to the particle.

Change
1. Initial position of the particle
2. Initial velocity of the particle
3. Acceleration of the particle
'''

# Initialize parameters
x_xi = 0 # initial position in x
v_xi = 5 # initial velocity in x
a_xi = 3 # acceleration


xi = vector(x_xi, 0, 0)
vi = vector(v_xi, 0 ,0)
ai = vector(a_xi, 0, 0)


# Initialize time
t = 0; dt = 0.1; tMax = 100

# Draw a canvas
scene = canvas(width=500, height=300, autoscale = False)

# Make a boundary
boundary = box(pos = vector(0, 0, 0),
            length = 30,
            height = 1,
            width = 0.1,
            color = color.blue)

ball = sphere(pos=xi)
ball.vel = vi
ball.acc = ai

gd = graph(width=600, height=200, xmin=0, xmax=tMax, xtitle ="Time", ytitle = "Position")
block_line = gcurve(color=vector(0,1,0), label='block x position')
ball_line = gcurve(color = vector(1, 0, 0), label = 'ball x position')

# 'vel' and 'acc' are properties of 'block' (object-oriented programming).
attach_arrow(ball, "vel", scale = 1, color = color.cyan, shaftwidth=0.5)

# Let's count time
# The loop increments t by dt till it reaches t = tMax.
while t < tMax:
    sleep(dt)

    # If the ball is in contact with the blue boundary then pause
    if ball.pos.x > 0 and (ball.pos.x + ball.radius) > boundary.length/2:
        #ball.acc = ball.acc*(-.8)
        ball.vel = ball.vel*(-0.8)
        ball.pos.x = boundary.length/2 - ball.radius
    
    else if ball.pos.x < 0 and (ball.pos.x - ball.radius) < (-1)*boundary.length/2:
        ball.vel = ball.vel*(-0.8)
        ball.pos.x = -boundary.length/2 + ball.radius
    
        
    # Increment the position in infinitesimal time.
    ball.vel = ball.vel + ball.acc*dt
    ball.pos = ball.pos + ball.vel*dt

    ball_line.plot(t, ball.pos.x)

    t = t + dt # Update the current time.
