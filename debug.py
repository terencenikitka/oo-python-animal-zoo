from lib.animal import Animal
from lib.zoo import Zoo

# code here


# e.g.  

z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
z2 = Zoo('Cincinnati Zoo', 'Cincinnati, OH')
a1 = Animal( 'Lion', 75, 'Luke', z1 )
a2 = Animal('Lion', 78, 'Leia', z2)
a3 = Animal('Hippo', 700, 'Fiona', z1)
z1 = Zoo('Micke Grove Zoo', 'Lodi, CA')




# ipdb allows us to stop our code & test stuff
import ipdb; ipdb.set_trace()
# print( 'Thanks for visiting the zoo!' )
# print(z1.location)
# print(z2.all)
# print(a1.zoo_name)
# print(Animal.find_by_species('Lion'))
# print(z1.animals) 
# print(z1.species)
print(z1.find_by_species('Lion','Lion'))
