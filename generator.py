def generator():
    for i in range(0,5):
        yield str(i)


print(''.join(generator()))


