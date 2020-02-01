
try:
    _list = [1, 2, 5]
    print(_list[7])
except Exception as e:
    print(e)
    print("The element is not on the index suggested")
finally: # si o si
    print("the scripts its over...")