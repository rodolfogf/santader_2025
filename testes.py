# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for item in range(n):
    participante_tema = input('').split(',')
    
    tema = participante_tema[1].strip()
    participante = participante_tema[0].strip()
    
    participantes = eventos.get(tema)
    if participantes is None:
        participantes = [participante]
    else:
        participantes.append(participante)
    
    eventos.update({tema:participantes})


# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
    
