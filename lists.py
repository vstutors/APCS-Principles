# Lists as a data abstraction
# take tons of data and show it in a simple way - that's a list

groceries = ["cake", "chips", "cookies", "orange"]

groceries.append("fish")

print(groceries) # calling a function on a list rather than just calling a function

groceries.insert(0, "potatoes")

print(groceries)

unhealthy_stuff = groceries[1:4]
print(unhealthy_stuff)

# combining with boolean expressions...
if len(unhealthy_stuff) > 2:
    print("Tooo much unhealthy stuff, mom's not gonna buy it")
else:
    print("This amount of unhealthy is okay...")