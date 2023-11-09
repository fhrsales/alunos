import pandas as pd
import random

# Carregue o arquivo CSV
df = pd.read_csv('alunos.csv')

# Crie uma lista de alunos e suas escolhas
alunos = df['aluno'].tolist()
escolhas = df[['escolha1', 'escolha2', 'escolha3']].values.tolist()

# Inicialize os grupos vazios
grupos = [[] for _ in range(70)]

# Função para verificar se um aluno já está em algum grupo
def aluno_em_grupo(aluno, grupos):
    for grupo in grupos:
        if aluno in grupo:
            return True
    return False

# Algoritmo para criar grupos com 70 grupos, cada um com 3 alunos
for i in range(70):
    grupo = []
    
    while len(grupo) < 3 and alunos:
        aluno = random.choice(alunos)
        escolhas_aluno = escolhas[alunos.index(aluno)]
        
        if not aluno_em_grupo(aluno, grupos):
            grupo.append(aluno)
            alunos.remove(aluno)
    
    grupos[i] = grupo

# Salve o resultado em um arquivo CSV
with open('grupos3.csv', 'w') as f:
    f.write("aluno,escolha1,escolha2\n")
    for grupo in grupos:
        f.write(','.join(map(str, grupo)) + "\n")