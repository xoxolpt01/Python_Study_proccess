a = 100
b = 200

var_1 = 'чисто "а" больше числа "b"'
var_2 = 'чисто "b" больше числа "a"'

resp = var_2 if b > a else var_1
print(resp)