def capital_indexes(word):
     b = -1
     l = []
     for i in word:
          b += 1
          if i.isupper() == True:
               l.append(b)
     return l
capital_indexes("HI")