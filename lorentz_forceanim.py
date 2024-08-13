import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

ax = plt.figure().add_subplot(projection = '3d')
class Point_Particle: 
    def __init__(self,position,charge,mass,velocity): 
        self.position = position
        self.charge = charge 
        self.mass = mass
        self.velocity = velocity 
electron = Point_Particle(np.array([0,0,0]),1.6*10**-19, 9.109 * 10**-31, np.array([0,0,1])) # suppose particle has only x component for now
B_field = [0,1,0]
def update_a(charge,mass,velocity,B_field): 
    new_a = (charge/mass)* np.cross(velocity,B_field)
    return new_a
electron.acceleration = update_a(electron.charge,electron.mass,electron.velocity, B_field) 

time_step = 10**-5
position = []
velocity = []
acceleration = []
position.append(electron.position) 
velocity.append(electron.velocity)
acceleration.append(electron.acceleration)



time = np.arange(0,10**5)
print(time* time_step)


for t in time: 
    xnew = position[t] + velocity[t]*time_step+0.5*acceleration[t]*time_step**2
    position.append(xnew)
    new_a = update_a(electron.charge,electron.mass,electron.velocity,B_field)
    acceleration.append(new_a) 
    new_vel = velocity[t] + 0.5 *(acceleration[t] + new_a)*time_step
    velocity.append(new_vel)

position = np.array(position)
print(np.shape(position))
ax.plot(position[:,0], position[:,1], position[:,2])
plt.show()
'''
def Calc_Force(PParticle,Magnetic_Field): 
    return PParticle.charge * (np.cross(PParticle.velocity,Magnetic_Field))
def update_v(Point_Particle,F,time_step): 
    delta_v = (F/Point_Particle.mass)*time_step
    return Point_Particle.velocity + delta_v

def update_pos(Point_Particle,delta_v,time_step):
    return Point_Particle.position + delta_v*time_step
v = electron.velocity
time = np.arange(0,10,time_step)
for t in time:
    F = Calc_Force(electron,M_field)
    v = update_v(electron,F,time_step) 
    p = update_pos(electron,v,time_step)
    electron.position = p 
    position.append(p)
positions = np.array(position)

print(np.shape(positions))
ax.plot(positions[:,0], positions[:,1], positions[:,2])
plt.show()

'''


