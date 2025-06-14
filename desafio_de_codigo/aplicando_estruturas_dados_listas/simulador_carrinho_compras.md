# Simulador de Carrinho de Compras

## Descrição

Crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.

## Entrada
Lista de produtos adicionados ao carrinho (cada um com nome e preço).

## Saída
Lista dos produtos adicionados e o total da compra.


## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 

Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                                                   | Saída                                                |
|-----------------------------------------------------------|------------------------------------------------------|
| 2<br>Pão 3.50<br>Leite 4.00                               | Pão: R$3.50<br>Leite: R$4.00<br>Total: R$7.50        |
| 3<br>Arroz 2.50<br>Brigadeiro 3.00<br>Sorvete 14.50       | Arroz: R$2.50<br>Brigadeiro: R$3.00<br>Sorvete: R$14.50<br>Total: R$20.00 |
| 3<br>Maçã 2.00<br>Pera 3.50<br>Biscoito 5.50              | Maçã: R$2.00<br>Pera: R$3.50<br>Biscoito: R$5.50<br>Total: R$11.00        |

## Template inicial

```Python
# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# TODO: Exiba os itens e o total da compra
```
