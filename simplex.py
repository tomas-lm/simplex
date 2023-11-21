import sys

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        # Lendo o número de restrições (n) e o número de variáveis (m)
        n, m = map(int, file.readline().split())

        # Lendo o vetor de custos c
        c = list(map(int, file.readline().split()))

        # Verificando se o número de elementos em c corresponde a m
        if len(c) != m:
            raise ValueError("O número de elementos no vetor c deve ser igual a m")

        # Lendo a matriz A e o vetor b
        A = []
        b = []
        for _ in range(n):
            row = list(map(int, file.readline().split()))

            # Verificando se o número de elementos na linha é m + 1
            if len(row) != m + 1:
                raise ValueError("Cada linha deve ter m + 1 elementos")

            A.append(row[:-1])
            b.append(row[-1])

    return n, m, A, b, c



def create_identity_matrix(A):
    """
    Cria uma matriz identidade com o mesmo número de linhas que a matriz A.

    :param A: Matriz de coeficientes das restrições.
    :return: Matriz identidade com o mesmo número de linhas que A.
    """
    num_rows = len(A)
    identity_matrix = [[0 for _ in range(num_rows)] for _ in range(num_rows)]
    
    for i in range(num_rows):
        identity_matrix[i][i] = 1
    
    return identity_matrix



def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <caminho_para_o_arquivo>")
        sys.exit(1)

    file_path = sys.argv[1]
    n, m, A, b, c = read_input_from_file(file_path)

    identity = create_identity_matrix(A)

    print(f"n = {n}\n m = {m}\n A = {A}\n b = {b}\n c = {c}")
    print(f"identity = {identity}")

    # Aqui você pode chamar a função que implementa o método simplex
    # Por exemplo: result = simplex_method(A, b, c)

    # E depois imprimir o resultado
    # print(result)

if __name__ == "__main__":
    main()
