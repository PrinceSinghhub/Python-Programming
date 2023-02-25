def revs(sen):
    w=sen.split(' ')
    revs= ' '.join(reversed(w))
    return revs
sen="op good boy"
print(revs(sen))
