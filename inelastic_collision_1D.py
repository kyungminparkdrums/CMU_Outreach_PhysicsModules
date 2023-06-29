Web VPython 3.2

'''
1D Inelastic Collision with target at rest

Ball moves toward a target at rest, perfectly inelastic collision takes place.
Velocity is calculated using the conservation of momentum.

Change
1. initial velocity of the ball
2. mass of the ball
3. mass of the target
'''


# Input on initial position, velocity, and the mass of the ball and the target
ball_xi = -3 # place it on the left of the target, so any negative value
ball_m = .3  # ball mass
ball_vxi = 2 # make it move towards the target, so positive value

target_m = .6 # target mass

# Create a ball that is moving
ball=sphere(pos=vec(ball_xi,0,0), radius=0.1, color=color.red)
ball.m= ball_m # mass
ball.vel=vec(ball_vxi,0,0) # momentum

# Create a target at rest
target=sphere(pos=vec(0,0,0), radius=0.2, color=color.cyan)
target.m = target_m # mass
target.vel=vec(0,0,0) # momentum, at rest

# Time steps and max time
t=0
tMax = 10
dt=0.1

# CREATE A GRAPH
gd_pos = graph(width=600, height=200, xmin=0, xmax=tMax, xtitle='Time', ytitle='Position')
ball_pos = gcurve(color=color.red,label='Ball')
target_pos = gcurve(color=color.cyan,label='Target')
    
gd_vel = graph(width=600, height=200, xmin=0, xmax=tMax, xtitle='Time', ytitle='Velocity')
ball_vel = gcurve(color=color.red,label='Ball')
target_vel = gcurve(color=color.cyan,label='Target')

isTogether = False # whether the target and ball are stuck to each other

while t<tMax:
    sleep(dt)
    
    # Update the velocities of the ball and the target
    # The moment that the elastic collision happens, change the velocities
    # Velocities are derived based on the conservation of energy & momentum
    if isTogether == False and (mag(target.pos - ball.pos) <= (ball.radius + target.radius)):
        target.vel = ball.m*ball.vel/(target.m + ball.m)
        ball.vel = ball.m*ball.vel/(target.m + ball.m)
        isTogether = True
    
    # Update position of the ball and the target based on their velocities
    ball.pos = ball.pos + ball.vel*dt
    target.pos = target.pos + target.vel*dt
    
    t=t+dt
    
    ball_pos.plot(t, ball.pos.x)
    target_pos.plot(t, target.pos.x)
    
    ball_vel.plot(t, ball.vel.x)
    target_vel.plot(t, target.vel.x)
