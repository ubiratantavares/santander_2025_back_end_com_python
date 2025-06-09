# Validador de formato de e-mails

## Descrição

* Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. 

* Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras.

## Regras para um e-mail válido

* Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.

* Não pode começar ou terminar com "@".

* Não pode conter espaços.

## Entrada

* Uma string contendo o e-mail a ser validado.

## Saída

* "E-mail válido" se o e-mail estiver no formato correto.

* "E-mail inválido" caso contrário.

## Exemplos

* A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 

* Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada              | Saída         |
|----------------------|----------------|
| usuario@gmail.com    | E-mail válido  |
| user@outlook.com     | E-mail válido  |
| usuario gmail.com    | E-mail inválido|

## Tenplate

```Python
# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
```
