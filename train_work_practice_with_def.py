# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_to_c(f_temp): #Converts Fahrenheit to Celsius.
  c_temp = (f_temp - 32) * 5/9
  return c_temp


f100_inc_celsius = f_to_c(100) #Input Fahrenheit temp here.
print(f100_inc_celsius)

def c_to_f(c_temp): #Converts Fahrenheit to Celsius.
  f_temp = c_temp * (9/5) + 32
  return c_temp

c0_in_fharenheit = c_to_f(0)
print(c0_in_fharenheit)

def get_force(train_mass, train_acceleration):
  train_force = train_mass * train_acceleration
  return train_force



train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force") 

def get_energy(mass, c=3*10**8):
  energy = mass * c**2
  return energy

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

