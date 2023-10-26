from lib.animal import Animal

class Zoo:
    all = []
    def __init__(self, name, location):
        self.name = name
        self.location= location
        Zoo.all.append(self)
    #     self.animals = _species

    # animals = property( species, set_species)

    @property 
    def animals(self):
        return [a for a in Animal.all if a.zoo_name == self.name]
    
    @property
    def species(self):
         return list(set([a.species for a in Animal.all]))

    @property 
    def find_by_species(self, spec):
        return [a for a in self.animals if a.species == spec]



   
