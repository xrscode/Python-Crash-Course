#Sal's Shipping Project
weight = 41.5

#Ground Shipping
if weight <= 2:
  print("Price per pound: 1.5 and flat charge: 20.  Final cost:", (weight*1.5+20))
elif (weight > 2 ) and (weight <= 6):
  print("Price/lb: 3 and flat charge: 20.  Final cost:", (weight*3+20))
elif (weight > 6) and (weight <= 10):
  print("Price/lb: 4 and flat charge: 20.  Final cost:", (weight*4+20))
else:
  print("Price/lb: 4.75: and flat charge: 20. Final cost:", (weight*4.75+20))

#Ground Shipping Premium
print("Ground Shipping Premium, Flat Charge: 125.  Total Cost:", (125))

#Drone Shipping
if weight <= 2:
  print("Price per pound: 4.5.  Final cost:", (weight*4.5))
elif (weight > 2 ) and (weight <= 6):
  print("Price/lb: 9. Final cost:", (weight*9))
elif (weight > 6) and (weight <= 10):
  print("Price/lb: 12.  Final cost:", (weight*12))
else:
  print("Price/lb: 14.25. Final cost:", (weight*14.25))