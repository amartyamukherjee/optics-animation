import numpy

class Field:
    def __init__(self,pos,dim,val,mag):
        self.corner_pos = pos
        self.dimension = dim
        self.value = val
        self.magnetic = mag

    def inside(self,pos):
        for i in range(pos):
            dist = pos[i] - corner_pos[i]
            if dist < 0 or dist < dimension[i]:
                return False
        return True

def force(charge,pos,vel,fields):
    force = [0 for x in pos]
    for field in fields:
        if field.inside(pos):
            if field.magnetic:
                force += charge * numpy.cross(vel, field.value)
            else:
                force += charge * field.value
    return force

class Charge:
    def __init__(self,pos,vel,cha):
        self.position = pos
        self.velocity = vel
        self.charge = cha

def time_step(charges,dt):
    for charge in charges:
        charge.position += charge.velocity * dt
        charge.velocity = force(charge.charge, charge.position, charge.velocity) * dt