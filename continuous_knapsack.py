items, capacity = map(int, input().split())
costs_and_weights = [tuple(int(x) for x in input().split()) for i in range(items)]

sorted_values = sorted(costs_and_weights, key=lambda item:item[0]/item[1], reverse=True)

free_space = capacity
cost_of_items_taken = 0
for value in sorted_values:
    if value[1] > free_space:
        cost_of_items_taken += value[0] * (float(free_space) / float(value[1]))
        break
    else:
        cost_of_items_taken += value[0]
        free_space -= value[1]

print("{0:0.3f}".format(cost_of_items_taken))
