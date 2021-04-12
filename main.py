#importing the module
from chempy import chemistry
#creating the reaction
reaction=chemistry.Reaction({'C':2,'O2':1},{'CO2':2})
#displaying the reaction
print(reaction)
#displaying the reaction order
print(reaction.order())
