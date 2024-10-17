import math

def pitagoras(a=None, b=None, c=None):
    if a is not None and b is not None:
        c = math.sqrt(a**2 + b**2)
        return c
    elif a is not None and c is not None:
        b = math.sqrt(c**2 - a**2)
        return b
    elif b is not None and c is not None:
        a = math.sqrt(c**2 - b**2)
        return a
    else:
        return "Por favor, forneça pelo menos dois lados."

def trigonometria(angulo):
    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    tangente = math.tan(math.radians(angulo))
    return seno, cosseno, tangente

def main():
    print("Calculadora de Teorema de Pitágoras")
    a = float(input("Digite o valor do lado a (ou deixe em branco se não souber): ") or 0)
    b = float(input("Digite o valor do lado b (ou deixe em branco se não souber): ") or 0)
    c = float(input("Digite o valor do lado c (ou deixe em branco se não souber): ") or 0)

    resultado = pitagoras(a if a else None, b if b else None, c if c else None)
    print(f"O lado faltante é: {resultado}")

    print("\nCalculadora de Seno, Cosseno e Tangente")
    angulo = float(input("Digite o ângulo em graus: "))
    seno, cosseno, tangente = trigonometria(angulo)
    print(f"Seno: {seno}, Cosseno: {cosseno}, Tangente: {tangente}")

if __name__ == "__main__":
    main()
