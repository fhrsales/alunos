import pandas as pd
import random

# Carregue o arquivo CSV
df = pd.read_csv('alunos.csv')

# Crie uma lista de alunos e suas escolhas
alunos = df['aluno'].tolist()
escolhas = df[['escolha1', 'escolha2']].values.tolist()

# Inicialize a lista de grupos
grupos = []

# Função para verificar se um aluno já está em algum grupo
def aluno_em_grupo(aluno, grupos):
    for grupo in grupos:
        if aluno in grupo:
            return True
    return False

# Algoritmo para criar grupos com 2 alunos
while alunos:
    grupo = []
    
    while len(grupo) < 2 and alunos:
        aluno = random.choice(alunos)
        escolhas_aluno = escolhas[alunos.index(aluno)]
        
        if not aluno_em_grupo(aluno, grupos):
            grupo.append(aluno)
            alunos.remove(aluno)
    
    if grupo:
        grupos.append(grupo)

# Salve o resultado em um arquivo CSV
with open('grupos2.csv', 'w') as f:
    f.write("aluno,escolha1,escolha2\n")
    for grupo in grupos:
        f.write(','.join(map(str, grupo)) + "\n")
