myList = [1, 3 + 2j, True, 4.0, 'slaves', 12, 'cumming']


for search in myList:
    if type(search) == int:
        print()
        print(str(search) +':it`s type int')
    elif type(search) == str:
        print()
        print(str(search)+': it`s type STR')
    else:
        print()
        print(str(search)+'other is bullshit')