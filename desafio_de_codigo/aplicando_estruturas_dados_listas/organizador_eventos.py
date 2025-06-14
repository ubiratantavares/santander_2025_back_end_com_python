# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    entrada = input().strip()
    dados = entrada.split(",")
    nome = dados[0].strip()
    tema = dados[1].strip()
    if tema in eventos.keys():
        eventos[tema].append(nome)
    else:
        eventos[tema] = [nome]

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
