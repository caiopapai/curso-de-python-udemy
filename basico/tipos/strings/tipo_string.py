print(dir(str))

nome = 'José de Paula'
print(nome)
primeira = nome[0]
print(primeira)
#string aqui tambem é imutável
#nome[0] = 'X'
texto_multiplas = """esst é um ...
texto quebrado"""
print(texto_multiplas)

x = nome[::]
print(x)

x = nome[::3]
print(x)

sub = nome[0:3]
print(sub)

inverte = nome[::-1]
print(inverte)

frase = "Esta é numa nova frase"
y = 'ras' in frase
print(y)
tamanho = len(frase)
print(tamanho)
print(frase.lower())
print(frase.upper())
print(frase.split())
help(str.center)
