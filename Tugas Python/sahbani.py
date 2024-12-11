people = [
    {'name': 'bob', 'age': 20, 'score': {'math': 90, 'science': 70}},
    {'name': 'carry', 'age': 38, 'score': {'math': 40, 'science': 72}},
    {'name': 'smith', 'age': 28, 'score': {'math': 80, 'science': 90}},
    {'name': 'john', 'age': 34, 'score': {'math': 75, 'science': 100}}
]

# Mencari nilai science dari seseorang yang bernama Smith
for person in people:
    if person['name'].lower() == 'smith':
        science_score = person['score']['science']
        print("Nilai Science dari Smith adalah:", science_score)
        break