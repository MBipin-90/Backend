""" Write a generator function that generates the first 10 even numbers. """

def even_numbers():
    for i in range(1, 21):
        if i%2==0:
            yield i

# Using the generator
for num in even_numbers():
    print(num)
