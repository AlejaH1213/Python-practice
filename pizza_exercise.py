toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
# number of occurrences of 2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
# length of the toppings list
num_pizzas = len(toppings)

print("we sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
# sorting the two dimensional list by ascending order
pizza_and_prices.sort()
print(pizza_and_prices)
# first element of the pizza and prices list
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
# last element of the pizza and prices list
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
# removing the last item 
pizza_and_prices.pop()
print(pizza_and_prices)
# adding a new topping in the right place, insert also takes two arguments. 
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)
# new list with three lower pizzas using slicing
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
