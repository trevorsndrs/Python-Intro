#Your inputs here!
weight = 6.9
#Would you like premium ground shipping? "yes/no"
premium_ground = "no"
#Would you like drone shipping? "yes/no"
drone_shipping = "no"

##############################################
#You shall not pass! Go no further adventurer!
cost_ground = 20
shipping_total = ""

#Ground Shipping
if weight <= 2:
  shipping_total = 2.00 * weight + cost_ground
elif weight > 2 and weight <= 6:
  shipping_total = 3.00 * weight + cost_ground
elif weight > 6 and weight <= 10:
  shipping_total = 4.00 * weight + cost_ground
else:
  shipping_total = 4.75 * weight + cost_ground

#Drone Shipping

if weight <= 2:
  drone_shipping_total = 4.50 * weight 
elif weight > 2 and weight <= 6:
  drone_shipping_total = 9.00 * weight 
elif weight > 6 and weight <= 10:
  drone_shipping_total = 12.00 * weight 
else:
  drone_shipping_total = 14.25 * weight

# Itemized Readout

print("Itemized Customer Copy")
print(" ")

if premium_ground == "yes" and drone_shipping == "yes":
  premium_ground_total = 0
  print("Premium shipping is not available for drones.")
elif premium_ground == "yes" and drone_shipping == "no":
  premium_ground_total = 125
  print("Premium shipping: $" + str(premium_ground_total))
else:
  premium_ground_total = 0

if drone_shipping == "no":
  print("Package weight: " + str(weight) + "lbs")
  print("_______________________________________")
  print("Package total with ground shipping: $" + str(shipping_total + premium_ground_total))
else:
  print("Package weight: " + str(weight) + "lbs")
  print("_______________________________________")
  print("Package total with drone shipping: $" + str(drone_shipping_total)) 
