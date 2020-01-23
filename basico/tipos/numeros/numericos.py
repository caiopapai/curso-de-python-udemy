print(dir(int))
#toda operação entre inteiro e float vai prevalecer a tipagem do float
a = 5
b = 2.5
c = a / b
tipo = type(c)

print(tipo)

resultado = b.is_integer
print(resultado)

x = 1.1 + 3.3
print(x)

from decimal import Decimal, getcontext
#precisão
getcontext().prec = 4

dec = Decimal(1) / Decimal(7)
print(dec)