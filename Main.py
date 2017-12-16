from Hero import Hero

jack = Hero('jack')
marry = Hero('Mary')

print('The name of the Hero is {} and his health is {}. Our hero has {} limbs'.format(jack.name,jack.health,jack.limbs))

print('The name of the Hero is {} and his health is {}. Our hero has {} limbs'.format(marry.name,marry.health,marry.limbs))

print('Chopped!')
marry.chopLimb(2)

print('The name of the Hero is {} and his health is {}. Our hero has {} limbs'.format(jack.name,jack.health,jack.limbs))

print('The name of the Hero is {} and his health is {}. Our hero has {} limbs'.format(marry.name,marry.health,marry.limbs))