# criacao de arquivo file1.py
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Exemplo de uso
numero = 4
print(f"O fatorial de {numero} é {fatorial(numero)}")
# criacao de arquivo file2.py
def soma(a, b):
    return a + b

print(soma(1, 2))
# criacao de arquivo auxiliar.py
def soma(a, b):
    return a + b

print(soma(1, 2))