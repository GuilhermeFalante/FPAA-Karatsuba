from karatsuba import karatsuba

def main():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))

    resultado = karatsuba(x, y)
    print(f"\nResultado da multiplicação: {resultado}")

if __name__ == "__main__":
    main()
