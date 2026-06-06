# Yield: Instead of returning a value, the yield statement pauses the function and sends a value back to the caller.

# When the generator is resumed, execution continues from the print where yield was called.

def Count_up_to(n):
    Count = 1
    while Count <= n:
        yield Count
        Count += 1

# creater a generator object.
Counter = Count_up_to(5)

#Iteretar over generator.
for num in Counter:
    print(num)
