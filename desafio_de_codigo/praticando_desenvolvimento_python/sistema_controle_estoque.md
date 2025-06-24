# Sistema de Controle de Estoque

## Descrição

* Uma loja deseja um sistema que registre os produtos disponíveis em estoque e permita verificar se um produto solicitado está disponível.

## Entrada

* Lista de produtos em estoque.

* Nome do produto solicitado.

## Saída

* "Produto disponível" se o produto estiver no estoque.

* "Produto esgotado" caso contrário.

## Exemplos

* A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 

* Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada   | 	Saída              |
| --------- |  ------------------  |
| Camiseta	|  Produto disponível  |
| Jaqueta	|  Produto disponível  |
| Vestido	|  Produto esgotado    |

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

## Template inicial

```Python
# Lista de produtos disponíveis no estoque
estoque = ["Camiseta", "Calça", "Tênis", "Boné", "Jaqueta"]

# Entrada do usuário
produto = input().strip()

# TODO: Verifique se o produto está no estoque:
```
