# Sistema de Gestão de Veículos

## Descrição

Implemente uma classe Veiculo que represente um carro com marca, modelo e ano. 

Crie um método que verifique se o carro é considerado antigo (mais de 20 anos).

## Entrada

* Marca, modelo e ano do veículo.

## Saída

* "Veículo antigo" se o carro tiver mais de 20 anos.

* "Veículo novo" caso contrário.

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 

Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada           | Saída         |
|-------------------|---------------|
| Toyota Corolla 2000 | Veículo antigo |
| Honda Civic 2005    | Veículo novo   |
| Ford Fiesta 1999    | Veículo antigo |

## Template inicial

```Python
from datetime import datetime

# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:

        
    # TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:
    

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())
```
