"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 100))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
calculations = {}
additions = {}
subtractions = {}

for num1 in q: # O(n^2)
    if num1 not in calculations:
        calculations[num1] = f(num1)
    for num2 in q:
        if num2 not in calculations:
            calculations[num2] = f(num2)
        added = calculations[num1] + calculations[num2]
        subtracted = calculations[num1] - calculations[num2]
        if added in additions:
            additions[added].append([num1, num2])
        else:
            additions[added] = [[num1, num2]]
        if subtracted in subtractions:
            subtractions[subtracted].append([num1, num2])
        else:
            subtractions[subtracted] = [[num1, num2]]

for calc in additions: # O(n)
    if calc in subtractions:
        for i in range(len(additions[calc])):
            for j in range(len(subtractions[calc])):
                print(f'f({additions[calc][i][0]}) + f({additions[calc][i][1]}) = f({subtractions[calc][j][0]}) - f({subtractions[calc][j][1]})    {calculations[additions[calc][i][0]]} + {calculations[additions[calc][i][1]]} = {calculations[subtractions[calc][j][0]]} - {calculations[subtractions[calc][j][1]]}')