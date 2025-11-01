print("Welcome to the mini shop!")


banana = 25
apple = 12
orange = 30 


print("how many fruitsdo you want?")
num_banana = int(input("bananas: "))
num_apple = int(input("apples: "))
num_orange = int(input("oranges: "))
total_cost = (banana * num_banana) + (apple * num_apple) + (orange * num_orange)
print(f"total cost is: {total_cost} UAH")
