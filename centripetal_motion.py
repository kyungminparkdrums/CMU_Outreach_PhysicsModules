Web VPython 3.2

'''
Centripetal motion

Ball in a centripetal motion.
Displacement, velocity, acceleration vectors are shown.

Change
1. Radius of the centripetal motion
2. Initial velocity in x

'''

scene = canvas()
scene.center = vector(0,0,0)
    
vi = 4
rad = 10

xi=0
yi = -rad
    
si = vector(xi,yi,0)
ball = sphere(pos=si, color=color.magenta, opacity = 0.4, radius=1,
        make_trail = True, trail_type = "points", interval = 10)
        
dot = sphere(pos=si, color=color.black, radius=0.01)
    
ball.vel = vector(vi,0,0)
ball.cAcc = -(mag(ball.vel)**2)*norm(ball.pos)/rad
    
dot.disp = vector(0,0,0)

attach_arrow(dot, "disp", scale = 1, color = color.green, shaftwidth=0.1)
attach_arrow(ball, "vel", scale = 1, color = color.blue, shaftwidth=0.1)
attach_arrow(ball, "cAcc", scale = 5, color = color.orange, shaftwidth=0.1)
    
dt = 0.1
t = 0
tMax = 100

# CREATE A GRAPH
gd0 = graph(width=600, height=250, xmin=0, xmax=tMax, xtitle='Time')
dx = gcurve(color=color.green,label='displacement magnitude')
    
gd1 = graph(width=600, height=250, xmin=0, xmax=tMax, xtitle='Time')
pathL = gcurve(color=color.magenta, label='distance')
    
while t < tMax:
    sleep(dt)  # Animation Speed
        
    ball.cAcc = -(mag(ball.vel)**2)*norm(ball.pos)/rad
    
    ball.vel = ball.vel + ball.cAcc*dt
    ball.pos = ball.pos + ball.vel*dt
    dot.disp = ball.pos - si
    dx.plot(t, mag(ball.pos - si))
    pathL.plot(t, mag(ball.vel)*t)
        
    t = t + dt
