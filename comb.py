syms = '1234'
count = 0


def comb(text='', blago=True):
    global count
    if len(text) == 4:
        print(text)
        count += 1
        return
    for s in syms:
        if blago:
            if s not in text:
                comb(text + s)
        else:
            comb(text + s, blago)


comb('1', blago=True)
print()
print(count)
