string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
counter = 0

for i in string:
    for j in vowels:
        if i == j:
            counter += 1
print(counter)

