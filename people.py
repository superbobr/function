def tallest_people(**people):
    most_tall = max(people.values())
    for i, j in sorted(people.items()):
        if j == most_tall:
            print(f'{i}: {j}')


tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)
