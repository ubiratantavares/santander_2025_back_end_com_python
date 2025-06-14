# Organizador de Eventos

## Descrição

Uma empresa quer criar um organizador de eventos que divida os participantes em grupos de acordo com o tema escolhido.

## Entrada

Lista de participantes e o tema escolhido por cada um.

## Saída

Dicionário agrupando os participantes por tema.

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 

Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada                                                                 | Saída                                         |
|-------------------------------------------------------------------------|-----------------------------------------------|
| 3<br>Lucas, Fotografia<br>Ana, Viagem<br>Carlos, Fotografia            | Fotografia: Lucas, Carlos<br>Viagem: Ana      |
| 4<br>João, Música<br>Pedro, Música<br>Maria, Dança<br>Ana, Dança       | Música: João, Pedro<br>Dança: Maria, Ana      |
| 5<br>Ana, Tecnologia<br>Carlos, Esportes<br>Maria, Tecnologia<br>Pedro, Música<br>João, Esportes | Tecnologia: Ana, Maria<br>Esportes: Carlos, João<br>Música: Pedro |

## Template inicial

```Python
# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:




# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
```
