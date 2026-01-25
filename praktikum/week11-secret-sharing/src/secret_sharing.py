import random

# Modulo prima
P = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def polynom(x, coefficients):
    result = 0
    for i, coef in enumerate(coefficients):
        result = (result + coef * pow(x, i, P)) % P
    return result

def split_secret(secret, k, n):
    coefficients = [secret] + [random.randint(1, P-1) for _ in range(k-1)]
    shares = [(x, polynom(x, coefficients)) for x in range(1, n+1)]
    return shares

# Contoh penggunaan
secret = 1234
shares = split_secret(secret, 3, 5)
print("Shares:", shares)
