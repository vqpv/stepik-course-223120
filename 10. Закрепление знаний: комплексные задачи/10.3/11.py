mass = float(input())
fuel_A = float(input())
fuel_B = float(input())

distance = 1000

cost_A = mass * distance * fuel_A
cost_B = mass * distance * fuel_B

if cost_A < cost_B:
    print("Fuel A")
elif cost_B < cost_A:
    print("Fuel B")
elif cost_B == cost_A:
    print("Equal")
