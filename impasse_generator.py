from random import randint
import copy
from algoritmo_detector import checar_recursos


def impasse_generator(n_processos: int, n_recursos: int, n_impasses: int) -> dict:

    # Gera o vetor de recursos existentes E.
    vetor_e = list()
    for recurso in range(0, n_recursos):
        vetor_e.append(randint(5, 15))

    # Gera o vetor de recursos disponíveis A.
    vetor_a = list()
    for recurso in range(0, n_recursos):
        vetor_a.append(vetor_e[recurso])

    # Inicializa a matriz de recursos alocados C.
    matriz_c = list()

    # Coloca os devidos valores na matriz C.
    for processo in range(0, n_processos):

        # O loop se certifica de que não haja processos com 0 recursos alocados.
        while True:

            # Faz uma deep copy do vetor A para que ele não seja modificado antes
            # de se ter certeza de que o procedimento dará certo
            vetor_a_backup = copy.deepcopy(vetor_a)

            linha_processo = []

            # Distribui os recursos de maneira mais ou menos distribuída.
            for recurso in range(0, n_recursos):
                qtd_recurso = randint(0, vetor_e[recurso]//2)
                if qtd_recurso >= vetor_a_backup[recurso]:
                    qtd_recurso = 0
                linha_processo.append(qtd_recurso)
                vetor_a_backup[recurso] -= qtd_recurso

            # O loop while continua se todos os recursos alocados para o processo
            # forem iguais a 0.
            if not all(v == 0 for v in linha_processo):
                matriz_c.append(linha_processo)
                vetor_a = copy.deepcopy(vetor_a_backup)
                break

            # Como os recursos atribuídos são gerados aleatóriamente, há a possibilidade
            # dos recursos acabarem antes de preencher todos os processos. Nesse caso,
            # o programa irá induzir a um erro e terminará.
            if all(v == 1 for v in vetor_a):
                raise(TypeError("Execute o código novamente."))

    # Esse loop irá continuar até que se forme uma matriz requisição R que atenda ao número de
    # impasses passado como parâmetro na função
    while True:
        matriz_r = []
        vetor_checagem = []
        for i in range(0, n_processos):
            vetor_checagem.append(0)

        # Preenche a matriz de requisição C.
        for processo in range(0, n_processos):
            recursos_r = []
            for recurso in range(0, n_recursos):
                recursos_r.append(randint(0, vetor_e[recurso] - matriz_c[processo][recurso]))

                # A variável 'vetor_checagem' vai ser responsável por registrar se todos os valores
                # de requisição do atual processo são maiores que 0.
                if recursos_r[recurso] != 0:
                    vetor_checagem[processo] = 1
            matriz_r.append(recursos_r)

        # Faz uma deep copy dos dados que entrarão na função checar_recursos.
        matriz_rcopia = copy.deepcopy(matriz_r)
        a_copia = copy.deepcopy(vetor_a)
        c_copia = copy.deepcopy(matriz_c)

        # Verifica se vai ocorrer um empasse.
        impasse1 = checar_recursos(matriz_rcopia, a_copia, c_copia)

        # Verifica se o empasse é entre a quantidade de processos especificada.
        if len(impasse1) == n_impasses:

            # Se certifica que nem todas as colunas de cada processo da matriz requisição R são iguais a 0.
            for i in vetor_checagem:
                if i == 0:
                    break
            return {'C': matriz_c,
                    'R': matriz_r,
                    'E': vetor_e,
                    'A': vetor_a,
                    }
          
          
if __name__ == '__main__':
    # Testa a função.
    print(impasse_generator(4, 5, 2))
