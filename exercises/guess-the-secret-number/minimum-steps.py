target_number = int(input())

low = 0
high = 100

found = False
tries = 0

while not found:
    tries += 1
    mid = int((low + high) / 2)
    print('Guess: %d' % mid)
    if target_number < mid:
        high = mid
    elif target_number > mid:
        low = mid
    else:
        found = True

print('Took %d tries' % tries)

