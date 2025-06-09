# Dicionário com os valores de desconto
descontos = {"DESCONTO10": 0.10,
             "DESCONTO20": 0.20,
             "SEM_DESCONTO": 0.00}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

preco_com_desconto = preco * (1 - descontos[cupom]) 

print(f"{preco_com_desconto:.2f}")   
