# list
item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        # no need to access anything, we have the item in i
        print(i)
    # forgot to increase the counter (n)
    n += 1

# both get last item in the list
print(item_list[len(item_list) - 1])
# print(item_list[-1])
