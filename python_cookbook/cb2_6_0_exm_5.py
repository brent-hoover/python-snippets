beehive = Behave("Queen Bee")
beehive.repeat(3)
beehive.rename("Stinger")
beehive.once()
print beehive.name
beehive.name = 'See, you can rebind it "from the outside" too, if you want'
beehive.repeat(2)
