# FPAA-Karatsuba
## 📋Algoritmo de Karatsuba
 Este projeto foi desenvolvido para a disciplina de FPAA, implementando o algoritmo de multiplicação de Karatsuba, um método de divisão e conquista para multiplicação de números grandes.

## 🧮Sobre o projeto

O Karatsuba é um algoritmo criado em 1960 por Anatoly Karatsuba, que mostrou que é possível multiplicar dois números grandes em menos operações do que o método padrão de multiplicação longa.

Enquanto o método tradicional realiza O(n²) operações para multiplicar dois números de 𝑛 dígitos, o Karatsuba consegue reduzir para O(n^{1.58}), tornando-se muito mais eficiente para números grandes.

## Explicação do projeto

## karatsuba.py
```python
def karatsuba(x: int, y: int) -> int:  # 1. Define função que recebe dois inteiros e retorna seu produto
    if x < 10 or y < 10:  # 2. Caso base: se algum número tem apenas 1 dígito
        return x * y  # 3. Retorna multiplicação direta (computacionalmente barata)

    n = max(len(str(x)), len(str(y)))  # 4. Determina tamanho do maior número
    m = n // 2  # 5. Calcula ponto médio para divisão

    alto_x, baixo_x = divmod(x, 10**m)  # 6. Divide x em parte alta e baixa
    alto_y, baixo_y = divmod(y, 10**m)  # 7. Divide y em parte alta e baixa

    a0 = karatsuba(baixo_x, baixo_y)  # 8. Recursão: multiplica partes baixas
    a1 = karatsuba(baixo_x + alto_x, baixo_y + alto_y)  # 9. Recursão: multiplica somas das partes
    a2 = karatsuba(alto_x, alto_y)  # 10. Recursão: multiplica partes altas

    # 11. Combina resultados usando fórmula de Karatsuba:
    # resultado = a2*10²ᵐ + (a1 - a2 - a0)*10ᵐ + a0
    return (a2 * 10**(2*m)) + ((a1 - a2 - a0) * 10**m) + a0 
```
## main.py
```python
from karatsuba import karatsuba  # 1. Importa a função karatsuba do módulo

def main():
    x = int(input("Digite o primeiro número: "))  # 3. Lê primeiro número como inteiro
    y = int(input("Digite o segundo número: "))   # 4. Lê segundo número como inteiro

    resultado = karatsuba(x, y)# 5. Executa multiplicação usando algoritmo de Karatsuba
    
    print(f"\nResultado da multiplicação: {resultado}")# 6. Exibe resultado formatado

if __name__ == "__main__":
    main()  # 7. Executa função principal quando script é rodado diretamente
```
## Como rodar o projeto

1. Primeiro clone o projeto com o link à seguir: `https://github.com/GuilhermeFalante/FPAA-Karatsuba.git`

2. Logo em seguida, entre na pasta devida utilizando o comando `cd FPAA-Karatsuba`.

3. E depois execute o projeto utilizando o comando `python main.py` no terminal.

4. Insira os dois números que deseja multiplicar.

## Relatório técnico

### Análise da complexidade ciclomática:

#### fluxo de controle

1. Início da função.

2. Verificação da condição if x < 10 or y < 10.

 - Se verdadeiro: retorna diretamente x * y.

 - Se falso: continua a execução.

3. Cálculo de n = max(len(str(x)), len(str(y))).

4. Cálculo de m = n // 2.

5. Divisão de x em (alto_x, baixo_x) usando divmod(x, 10**m).

6. Divisão de y em (alto_y, baixo_y) usando divmod(y, 10**m).

7. Chamada recursiva a0 = karatsuba(baixo_x, baixo_y).

8. Chamada recursiva a1 = karatsuba(baixo_x + alto_x, baixo_y + alto_y).

9. Chamada recursiva a2 = karatsuba(alto_x, alto_y).

10. Combinação dos resultados pela fórmula de Karatsuba:

 - (a2 * 10**(2*m)) + ((a1 - a2 - a0) * 10**m) + a0.

11. Retorno do resultado final.


#### Estruturando o grafo de fluxo

##### Nós:
- N1: Início da função karatsuba.

- N2: Verificação do if `(x < 10 or y < 10)`.

- N3: Retorno da multiplicação `(x * y)`.

- N4: Cálculo do número de dígitos de x e y e atribui à n.

- N5: Divide n em 2 e atribui ao m

- N6: Divisão de x em `(alto_x, baixo_x)`.

- N7: Divisão de y em `(alto_y, baixo_y)`.

- N8: Chamada recursiva `a0 = karatsuba(baixo_x, baixo_y)`.

- N9: Chamada recursiva `a1 = karatsuba(baixo_x + alto_x, baixo_y + alto_y)`.

- N10: Chamada recursiva `a2 = karatsuba(alto_x, alto_y)`.

- N11: Combinação dos resultados pela fórmula de Karatsuba.

##### Arestas:

1. N1 → N2: Início da função, para verificação do caso base

2. N2 → N3: Da verificação do caso base para o retorno da multiplicação do x e y

3. N2 → N4: Se a condição do if for falsa, continua para o cálculo de n.

4. N4 → N5: Do cálculo de n para o cálculo de m.

5. N5 -> N6: Do cálculo de m para a divisão de x em (alto_x, baixo_x).

6. N6 -> N7: Da divisão de x para a divisão de y em (alto_y, baixo_y).

7. N7 -> N8: Da divisão de y para a chamada recursiva a0 = karatsuba(baixo_x, baixo_y).

8. N8 -> N9: Da chamada recursiva a0 para a chamada recursiva a1 = karatsuba(baixo_x + alto_x, baixo_y + alto_y).

9. N9 -> N10: Da chamada recursiva a1 para a chamada recursiva a2 = karatsuba(alto_x, alto_y).

10. N10 -> N11: Da chamada recursiva a2 para a combinação dos resultados pela fórmula de Karatsuba.

11. N8 -> N1: Recursão: a0 chama novamente a função karatsuba.

12. N9 -> N1: Recursão: a1 chama novamente a função karatsuba.

13. N10 -> N1: Recursão: a2 chama novamente a função karatsuba.

##### Cálculando a clomplexidade ciclomática:

- Nós (N) = 12 (N1 até N12)

- Arestas (E) = 13 

M = 13 - 11 + 2x1

M = `4`

##### Grafo construído:

![alt text](grafo.png)

### Análise da complexidade assintótica:

 -Melhor caso: `O(1)` → quando um dos números tem apenas 1 dígito.
 -Caso médio: `O(n^1.585) ou O(n^log(3))`
 -Pior caso: `O(n^1.585) ou O(n^log(3))` 

