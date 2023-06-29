Web VPython 3.2

'''
Ball bouncing off the ground, projected horizontally

Ball is projected horizontally, from a height.
It is accelerated towards the ground due to gravity.
When it touches the ground, it bounces off.
When bouncing off, its magnitude of y velocity decreases by 20% and the y velocity sign flips.

Change
1. Initial speed of the horizontal projectile motion
2. Initial height of the ball
3. Gravitational constant

'''

vi = 4         #(m/s), initial speed (magnitude of velocity in x)
yi = 5         #(m), initial height

g = 9.8

tube = cylinder(pos = vector(-15, yi, 0),
                axis = vector(1,
                        0,
                        0),
                radius = 0.5,
                color = color.blue)

ball = sphere(pos = tube.pos + tube.axis,
              radius = 0.5,
              color = color.red,
              vel = vector(vi, 0, 0),
              acc = vector(0, -g, 0),
              make_trail = True, trail_type='points', interval=8
              )

floor = box(pos = vector(0, 0, 0),
            width = 0.01,
            length = 30.,
            height = 0.05,
            color = vector(1,1,1))

t = 0           #(s), initial time
dt = 0.01       #(s), time step
tMax = 20

while t < tMax:
    sleep(dt)
    ball.vel = ball.vel + ball.acc * dt
    ball.pos = ball.pos + ball.vel * dt

    # When the ball hits the floor (ball's y position is less than or equal to the radius of the ball)
    if ball.pos.y <= ball.radius:
        ball.vel.y =  - 0.8*ball.vel.y
        ball.pos.y = ball.radius
    
    # If the ball hits the right end of the floor, stop the ball
    if ball.pos.x >= floor.length/2:
        break

    t = t + dt
