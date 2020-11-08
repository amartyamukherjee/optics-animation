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
        if pos[0] - self.position[0] < 0 or pos[0] - self.position[0] < self.dimensions[0] or pos[1] - self.position[1] < 0 or pos[1] - self.position[1] < self.dimensions[1]:
            return False
        return True

    def get_electric_field(self,pos):
        if self.inside(pos) and not self.magnetic:
            return self.value
        else:
            return [0, 0]

    def get_magnetic_field(self,pos):
        if self.inside(pos) and self.magnetic:
            return self.value
        else:
            return [0, 0, 0]

class PointCharge(Field):
    def __init__(self,pos,cha):
        self.position = pos
        self.charge = cha

    def get_electric_field(self,pos):
        return self.charge / (4 * numpy.pi * permittivity) * numpy.subtract(pos, self.position) / numpy.linalg.norm(numpy.subtract(pos, self.position))**3

    def get_magnetic_field(self,pos):
        return [0, 0, 0]

class WireZ(Field):
    def __init__(self,pos,cur):
        self.position = pos
        self.current = cur

    def get_electric_field(self, pos):
        return [0, 0]

    def get_magnetic_field(self,pos):
        return numpy.cross([0,0,self.current],numpy.subtract(pos, self.position)) * permeability / (2 * numpy.pi * numpy.linalg.norm(numpy.subtract(pos, self.position),2))

class InfiniteWire(Field):
    def __init__(self,pos,dire,cur):
        self.position = pos
        self.direction = dire
        self.current = cur

    def get_electric_field(self,pos):
        return [0, 0]

    def get_magnetic_field(self,pos):
        return self.current * permeability * numpy.cross(self.direction,numpy.subtract(pos, self.position)) / (2 * numpy.pi * numpy.cross(self.direction,numpy.subtract(pos, self.position)**2))

def force(charge,pos,vel,fields):
    elec = [0, 0]
    mag = [0, 0, 0] #Magnetic fields are three dimensions to account for the z axis
    for field in fields:
        elec = numpy.add(elec, field.get_electric_field(pos))
        mag = numpy.add(mag, field.get_magnetic_field(pos))
    return charge * numpy.add(elec, numpy.cross(vel,mag)[0:-1])

class Charge:
    def __init__(self,pos,vel,cha,mas):
        self.position = pos
        self.velocity = vel
        self.charge = cha
        self.mass = mas

def time_step(charges,fields,dt):
    for charge in charges:
        #We use a 4th order runge-kutta method to calculate the change in velocity
        #we can do this because our force function gives us a definite function for acceleration
        k1 = force(charge.charge, charge.position, charge.velocity, fields) / charge.mass
        k2 = force(charge.charge, charge.position + k1 / 2, charge.velocity, fields) / charge.mass
        k3 = force(charge.charge, charge.position + k2 / 2, charge.velocity, fields) / charge.mass
        k4 = force(charge.charge, charge.position + k3 / 2, charge.velocity, fields) / charge.mass
        charge.velocity += 1/6 * dt * (k1 + 2 * k2 + 2 * k3 + k4)
        #Since we're determining velocity numerically we can't use the same method here so we settle for the less accurate Euler approximation
        charge.position += charge.velocity * dt