GlowScript 2.7 VPython

#SINCE F_GR = -G Mm/r**2 * r_hat
def gforce(p1, p2):
    G = 1
    r_vec = p1.pos - p2.pos
    r_mag = mag(r_vec)
    r_hat = r_vec/r_mag
    force_magnitude = (G*p1.mass*p2.mass)/r_mag**2
    force_vec = -force_magnitude*r_hat
    
    return force_vec
    
    
#CREATING OUR OBJECTS
star = sphere(pos = vector(0,0,0), radius = 0.2, color=color.yellow, mass = 1000, momentum = vector(0,0,0), make_trail = True)
planet1 = sphere(pos = vector(1,0,0), radius = 0.06, color=color.blue, mass=1, momentum = vector(0,30,0), make_trail = True)
    
dt = 0.0001
t = 0
    
while(True):
    rate(1000)
    
    #FORCES
    star.force = gforce(star, planet1)
    planet1.force = gforce(planet1, star)
    
    #MOMENTUM
    star.momentum = star.momentum + star.force * dt
    planet1.momentum = planet1.momentum + planet1.force * dt
    
    #POSITIONS
    star.pos = star.pos + star.momentum/star.mass * dt
    planet1.pos = planet1.pos + planet1.momentum/planet1.mass * dt
    
    t=t*dt
