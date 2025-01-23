def f1_score(tp, fp, fn):
    #check kieu du lieu cua tp, fp, fn
    if not isinstance(tp, int):
        print("tp must be int")
        return None
    if not isinstance(fp, int):
        print("fp must be int")
        return None
    if not isinstance(fn, int):
        print("fn must be int")
        return None
    if tp <=0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return None

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    
    print("precision is", precision)
    print("recall is", recall)
    print("f1_score is", round(f1_score, 2))
f1_score(tp= 2, fp= 3, fn= 4)
f1_score(tp = 'a', fp = 3, fn = 4)
f1_score(tp = 2, fp = 'a', fn = 4)
f1_score(tp = 2, fp = 3, fn = 'a')
f1_score(tp = 2, fp = 3, fn = 0)
f1_score(tp = 2.1, fp = 3, fn = 0)

#trac nghiem
f1_score(tp = 2, fp = 4, fn= 5)
