# Sistema de Controle de Acesso

## Descrição

* Uma empresa deseja criar um sistema simples de login para permitir acesso de funcionários. 

* O sistema precisa verificar se o usuário está cadastrado e se a senha informada está correta.

## Entrada

* O programa recebe duas linhas de entrada:

	- Primeira linha: Nome do usuário cadastrado.

	- Segunda linha: Senha correspondente ao usuário.

## Saída

* "Acesso permitido" se as credenciais estiverem corretas.

* "Usuário ou senha incorretos" caso contrário.

## Exemplos

* A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 

* Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada        | Saída                       |
|--------------- | --------------------------- |
| joao 1234      | Acesso permitido            |
| maria senha123 | Acesso permitido            |
| ana 1234       | Usuário ou senha incorretos |

## Template inicial

```Python
# Dicionário com usuários cadastrados e suas senhas
usuarios = {
    "joao": "1234",
    "ana": "abcd",
    "maria": "senha123",
    "marcelo": "iou789",

}

# Entrada do usuário
usuario = input().strip()
senha = input().strip()

# TODO: Verifique se o usuário existe e a senha está correta:
```
