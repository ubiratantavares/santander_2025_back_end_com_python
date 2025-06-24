# Sistema de Pedidos de Restarurante

## Descrição

* Crie uma classe Pedido que represente um pedido em um restaurante, contendo os itens pedidos e um método para calcular o valor total da conta.

## Entrada

* Lista de itens e seus respectivos preços.

## Saída

O valor total da conta.

## Exemplos

* A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 

* Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada	         | Saída |
|--------------------|-------|
| 2                  |       |
| Pizza 40.00        |       |
| Suco 7.50	         | 47.50 |
| 3                  |       |
| Hamburguer 15.50   |       |
| Refrigerante 5.00  |       |
| Batata 8.00	     | 28.50 |
| 4                  |       |
| Café 4.50          |       |
| Pão de queijo 6.00 |       |
| Bolo 10.25         |       |
| Chá 3.75	         | 24.50 |

## Template inicial

```Python
class Pedido:
    def __init__(self):
        self.itens = []  
    
    # TODO: Crie um método chamado adicionar_item que recebe um preço e adiciona à lista de itens:
    
        # TODO: Adicione o preço do item à lista:
          

    # TODO: Crie um método chamado calcular_total que retorna a soma de todos os preços da lista:
    
        # TODO: Retorne a soma de todos os preços
        

quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    #TODO: Chame o método adicionar_item corretamente: 

# TODO: Exiba o total formatado com duas casas decimais:
```
