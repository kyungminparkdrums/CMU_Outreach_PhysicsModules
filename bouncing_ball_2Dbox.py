Web VPython 3.2

'''
Ball bouncing off the wall in a 2D box

Ball is moving under acceleration from gravity.
When it touches the boundary of the box, it bounces off.
When bouncing off, the speed decreases by 20% and the velocity sign is flipped.

Change
1. Initial position of the ball
2. Initial velocity of the ball
3. Gravitational constant

'''


# Initialize your vectors

xi = vector(0, 0, 0)
vi = vector(-5, 10, 0)


g = 9.8
ai = vector(0, -g, 0)

# Initialize time
t = 0; dt = 0.1; tMax = 10


# Draw a canvas
scene = canvas(width=500, height=300, autoscale = False)

# Make a boundary
boundary = box(pos = vector(0, 0, 0),
            length = 30,
            height = 15,
            width = 0,
            color = color.red)

yoffset = boundary.height/2

ball = sphere(pos=xi)
ball.vel = vi
ball.acc = ai
ball.radius = 1

gd = graph(width=600, height=300, xmin=0, xmax=tMax, xtitle ="Time", ytitle = "Position")
ball_pos_x = gcurve(color = vector(1, 0, 0), label = 'ball x position')

gd_vel = graph(width=600, height=200, xmin=0, xmax=tMax, xtitle ="Time", ytitle = "Velocity")
ball_pos_y = gcurve(color = vector(1, 0, 0), label = 'ball y position')


attach_arrow(ball, "vel", scale = 1, color = color.cyan, shaftwidth=0.5)


# The loop increments t by dt till it reaches t = tMax.
while t < tMax:
    sleep(dt)
    
    # Increment the position in infinitesimal time.
    ball.vel = ball.vel + ball.acc*dt
    ball.pos = ball.pos + ball.vel*dt

    # If the ball is in contact with the boundary then
    # Decrease the speed by 20%
    # Flip the velocity sign
    if ball.pos.x > 0 and (ball.pos.x + ball.radius) >= boundary.length/2:
      ball.vel = ball.vel*(-0.8)
      ball.pos.x = boundary.length/2 - ball.radius
    
    else if ball.pos.x < 0 and (ball.pos.x - ball.radius) <= (-1)*boundary.length/2:
      ball.vel = ball.vel*(-0.8)
      ball.pos.x = -boundary.length/2 + ball.radius
      
    if ball.pos.y > 0 and (ball.pos.y + ball.radius) > boundary.height/2:
        ball.vel = ball.vel*(-0.8)
        ball.pos.y = boundary.height/2 - ball.radius
    
    else if ball.pos.y < 0 and (ball.pos.y - ball.radius) < (-1)*boundary.height/2:
        ball.vel = ball.vel*(-0.8)
        ball.pos.y = -boundary.height/2 + ball.radius
        

    ball_pos_x.plot(t, ball.pos.y)
    ball_pos_y.plot(t, ball.pos.y)

    t = t + dt # Update the current time.
