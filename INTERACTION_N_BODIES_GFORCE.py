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
planet2 = sphere(pos = vector(0,3,0), radius = 0.075, color = color.red, mass = 4, momentum = vector(-35, 0 ,0), make_trail = True)
planet3 = sphere(pos = vector(0, -4, 0), radius = 0.1, color = color.green, mass = 10, momentum = vector(200, 0 ,0), make_trail = True)
comet = sphere(pos = vector(-6, 6, 0), radius = 0.04, color = color.white, mass = 0.5, momentum = vector(-1, -1, 0), make_trail = True)
tail = cone(pos = comet.pos, axis = comet.pos - star.pos, size = vector(1,1,1)*comet.radius, color=color.yellow)

dt = 0.0001
t = 0


while(True):
    rate(1500)
    
    #FORCES
    star.force = gforce(star, planet1) + gforce(star, planet2) + gforce(star, planet3)
    planet1.force = gforce(planet1, star) + gforce(planet1, planet2) + gforce(planet1, planet3)
    planet2.force = gforce(planet2, star) + gforce(planet2, planet1) + gforce(planet2, planet3)
    planet3.force = gforce(planet3, star) + gforce(planet3, planet1) + gforce(planet3, planet2)
    comet.force = gforce(comet, star)
    
    #MOMENTUM
    star.momentum = star.momentum + star.force * dt
    planet1.momentum = planet1.momentum + planet1.force * dt
    planet2.momentum = planet2.momentum + planet2.force * dt
    planet3.momentum = planet3.momentum + planet3.force * dt
    comet.momentum = comet.momentum + comet.force * dt
    
    #POSITIONS
    star.pos = star.pos + star.momentum/star.mass * dt
    planet1.pos = planet1.pos + planet1.momentum/planet1.mass * dt
    planet2.pos = planet2.pos + planet2.momentum/planet2.mass * dt
    planet3.pos = planet3.pos + planet3.momentum/planet3.mass * dt
    comet.pos = comet.pos + comet.momentum/comet.mass * dt
    
    tail.pos = comet.pos + comet.radius * vector(1,1,1)
    tail.axis = comet.pos - star.pos
    tail.axis = tail.axis/mag(tail.axis)
    
    t = t*dt
