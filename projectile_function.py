Web VPython 3.2

'''
Projectile motion using function

Box goes through a projectile motion under gravity
Velocity vectors (x and y) are attached to the box.

Change
1. Initial position in x and y of the box
2. Initial velocity in x and y of the box

'''


def projectile(xi = -12., yi =0., vxi = 15., vyi = 12., g = 9.8, attachArrow = True):
    
    # Create a box that will move
    boxA = box(pos=vector(xi,yi,0), color=color.magenta, opacity = 0.4,
              length=1.5, height=1.5, width=1.5,
              make_trail = True, trail_type = "points", interval = 10)
    
    boxA.vx = vector(vxi,0,0)
    boxA.vy = vector(0,vyi,0)
    
    boxA.vel = boxA.vx + boxA.vy
    
    boxA.acc = vector(0,-g,0)
        
    
    # Time steps and end time
    t = 0
    dt = 0.1
    tMax = 3.0
        
    # Create arrows for the velocity vectors
    if attachArrow:
      attach_arrow(boxA, "vx", scale = 0.3, color = color.green, shaftwidth=0.1)
      attach_arrow(boxA, "vy", scale = 0.3, color = color.orange, shaftwidth=0.1)
    
    # Create a graph
    gd = graph(width=600, height=200, xmin=0, xmax=tMax, xtitle='Time (s)', ytitle='Velocity (m/s)')
    vel_x = gcurve(color=color.green,label='v_x')
    vel_y = gcurve(color=color.orange, label='v_y')
    
    # Loop, update the velocity and position every timestep in dt
    while t < tMax:
        sleep(dt)
        
        # Update position and velocity
        boxA.vy = boxA.vy + boxA.acc*dt
        boxA.vel = boxA.vx + boxA.vy
        boxA.pos = boxA.pos + boxA.vel*dt
        
        # Update the plot
        if attachArrow:
            vel_x.plot(t, boxA.vel.x )
            vel_y.plot(t, boxA.vel.y )
         
        # Update time
        t = t + dt

    
projectile(xi = -12.0, yi = 0.0, vxi = 15.0, vyi = 12.0, g = 9.8)
