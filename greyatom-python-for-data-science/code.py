# --------------
# Code starts here
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

new_class = class_1 + class_2
print(new_class)

new_class.append('Peter Warden')
print(new_class)

new_class.remove('Carla Gentry')
print(new_class)
# Code ends here


# --------------
# Code starts here
courses = {'Math':65,'English': 70,'History': 80,'French': 70,'Science'	: 60}

total = sum(courses.values())
print(total)

percentage = total*100/500
print(percentage)
# Code ends here


# --------------
# Code starts here
mathematics = {'Geoffrey Hinton':78,'Sebastian Raschka':65,'Andrew Ng':95,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

topper = max(mathematics, key = mathematics.get)



# Code ends here  


# --------------
# Given string
topper = 'andrew ng'

first_name, last_name = topper.split(' ')
full_name = last_name+' '+first_name
certificate_name = full_name.upper()
print(certificate_name)
# Code starts here



# Code ends here


