import pandas as pd

# Carregue os dois arquivos CSV em DataFrames
df_original = pd.read_csv('alunos.csv')
df_atual = pd.read_csv('grupos3.csv')

# Inicialize uma lista para armazenar os alunos que mantêm pelo menos uma escolha igual
alunos_com_pelo_menos_uma_escolha_igual = []

# Inicialize uma lista para armazenar os alunos sem nenhuma escolha igual
alunos_sem_escolha_igual = []

# Percorra os alunos da base de dados original
for aluno_original in df_original.itertuples():
    aluno = aluno_original[1]
    escolhas_originais = set(aluno_original[2:])
    
    # Verifique se as escolhas do aluno estão presentes na base de dados atual
    encontrou_escolha_igual = False
    for aluno_atual in df_atual.itertuples():
        escolhas_atuais = set(aluno_atual[2:])
        if not escolhas_originais.isdisjoint(escolhas_atuais):
            alunos_com_pelo_menos_uma_escolha_igual.append(aluno)
            encontrou_escolha_igual = True
            break
    if not encontrou_escolha_igual:
        alunos_sem_escolha_igual.append(aluno)

# Imprima a lista de alunos com pelo menos uma escolha igual à original
print('Alunos com pelo menos uma escolha igual à original:')
print(alunos_com_pelo_menos_uma_escolha_igual)

# Imprima a lista de alunos sem nenhuma escolha igual à original
print('\nAlunos sem nenhuma escolha igual à original:')
print(alunos_sem_escolha_igual)
