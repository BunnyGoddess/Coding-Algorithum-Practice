# Lowest Shipping Price Problem

weight = input()
weight = float(weight)

Ground_Shipping_Price = 20
Ground_Shipping_Premium_Price = 125.00
Drone_Shipping_Price = 0

if weight <= 2:
    Ground_Shipping_Price += (weight * 1.50)
elif weight <= 6:
    Ground_Shipping_Price += (weight * 3.00)
elif weight <= 10:
    Ground_Shipping_Price += (weight * 4.00)
else:
    Ground_Shipping_Price += (weight * 4.75)

if weight <= 2:
    Drone_Shipping_Price += (weight * 4.50)
elif weight <= 6:
    Drone_Shipping_Price += (weight * 9.00)
elif weight <= 10:
    Drone_Shipping_Price += (weight * 12.00)
else:
    Drone_Shipping_Price += (weight * 14.75)

if Ground_Shipping_Premium_Price <= Drone_Shipping_Price and Ground_Shipping_Price:
    print('Lowest Price is $125 using Ground Shipping Premium')
elif Drone_Shipping_Price <= Ground_Shipping_Price:
    print(f'Lowest Price is ${str(Drone_Shipping_Price)} using Drone Shipping Price')
else:
    print(f'Lowest Price is ${str(Ground_Shipping_Price)} using Drone Shipping Price')