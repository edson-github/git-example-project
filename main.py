def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Exemplo de uso
numero = 4
print(f"O fatorial de {numero} é {fatorial(numero)}")