import numpy

permittivity = 8.9e-12
permeability = 1.3e-6

class Field:
    def get_electric_field(self,pos):
        pass

    def get_magnetic_field(self,pos):
        pass

class RectField(Field):
    def __init__(self,pos,dim,val,mag):
        self.position = pos
        self.dimensions = dim
        self.value = val
        self.magnetic = mag

    def inside(self,pos):
        for i in range(pos):
            dist = pos[i] - corner_pos[i]
            if dist < 0 or dist < dimension[i]:
                return False
        return True

    def get_electric_field(self,pos):
        if inside(self,pos) and not magnetic:
            return value
        else:
            return [0 for n in value]

    def get_magnetic_field(self,pos):
        if inside(self,pos) and magnetic:
            return value
        else:
            return [0 for n in value]

class PointCharge(Field):
    def __init__(self,pos,cha):
        self.position = pos
        self.charge = cha

    def get_electric_field(self,pos):
        return charge / (4 * numpy.pi * permittivity) * (pos - self.position) / numpy.pow(numpy.linalg.norm(pos - self.position), 3)

    def get_magnetic_field(self,pos):
        return [0 for x in pos]

class WireZ(Field):
    def __init__(self,pos,cur):
        self.position = pos
        self.current = cur

    def get_electric_field(self, pos):
        return [0 for x in pos]

    def get_magnetic_field(self,pos):
        return numpy.cross_product([0,0,self.current],pos - self.position) * permeability / (2 * numpy.pi * numpy.linalg.norm(pos - self.position,2))

def force(charge,pos,vel,fields):
    elec = [0 for x in pos]
    mag = [0 for x in pos]
    for field in fields:
        elec += field.get_electric_field
        mag += field.get_magnetic_field
    return charge * (elec + numpy.cross_product(vel,mag))

class Charge:
    def __init__(self,pos,vel,cha):
        self.position = pos
        self.velocity = vel
        self.charge = cha

def time_step(charges,dt):
    for charge in charges:
        charge.position += charge.velocity * dt
        charge.velocity = force(charge.charge, charge.position, charge.velocity) * dt