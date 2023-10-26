class Animal:
    all = []
    def __init__ (self, species, weight, nickname, zoo_name):
        self.nickname = nickname
        self.weight = weight
        self.species = species
        self.zoo_name = zoo_name.name
        Animal.all.append(self)
    
    @classmethod    
    def find_by_species(animal, species):
        return [a.nickname for a in animal.all if a.species == species]

