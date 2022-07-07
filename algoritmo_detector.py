import pickle


def checar_recursos(r: list, a: list, c: list) -> set:
    # Define o número de recursos
    n_recursos = len(a)

    # Define o número de processos
    n_processos = len(c)

    # Cria um conjunto vazio que será preenchido com os índices dos processos envolvidos em um empasse
    # caso haja um.
    impasses = set()

    # O programa irá iterar por todos os processos
    for i_processo in range(0, n_processos):

        # A variável 'liberar' será utilizada para decidir se os recursos disponíveis devem
        # ou não ser liberados para o processo selecionado.
        liberar = 1

        # O programa irá iterar por todos os tipos de recursos.
        for i_recurso in range(0, n_recursos):

            # Se houver um tipo de recurso que não pode ser alocado, ele muda a variável 'liberar'
            # e adiciona o processo selecionado ao conjunto de processos que não puderam ser concluídos.
            if r[i_processo][i_recurso] > a[i_recurso]:
                impasses.add(i_processo)
                liberar = 0

        # Se o loop que itera pelos recursos acabou e a variável 'liberar' não foi modificada, ocorrerá
        # a execução do processo selecionado e a liberação dos recursos que estavam sendo utilizados por ele.
        if liberar == 1:
            for i_recurso in range(0, n_recursos):
                recurso = c[i_processo][i_recurso]
                c[i_processo][i_recurso] = 0
                r[i_processo][i_recurso] = 0
                a[i_recurso] += recurso

    # Printa o estado atual dos dados envolvidos nas operações.
    print(f'A: {A}')
    print(f'E: {E}')
    print(f'C: {C}')
    print(f'R: {R}')
    print('\n\n')

    # Retorna o conjunto de processos que não puderam ser atendidos.
    return impasses


# Abre o arquivo do cenário selecionado e atribui seus dados a uma variável.
with open(r'cenario3.pkl', 'rb') as file:
    cenario = pickle.load(file)

# Atribuindo os devidos valores do cenário escolhido
A = cenario['A']
E = cenario['E']
C = cenario['C']
R = cenario['R']

print(f'A: {A}')
print(f'E: {E}')
print(f'C: {C}')
print(f'R: {R}')
print('\n\n')

a0 = None
a1 = None

# Entra em um loop para alocar os recursos para cada processo possível. Se o estado dos dados não muda, significa
# que, ou há um impasse, ou todos os processos foram atendidos.
while True:
    a1 = checar_recursos(R, A, C)
    # print(a1)

    if a0 == a1:
        break

    a0 = a1

i = 0

# Faz a formatação da saída do programa
if a1 != set():
    qtd_processos = len(a1)
    print(f"Há {qtd_processos} impasses no sistema.")
    print("Processos envolvidos no empasse:", end='')
    for elemento in a1:
        if i > 0:
            print(',', end='')
        print(f' {elemento + 1}', end='')
        i += 1
    print('.')

else:
    print("Não há impasses no sistema.")
