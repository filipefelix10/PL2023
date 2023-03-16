import re
import pandas
import json


# Transforma o ficheiro csv numa lista de dicionarios
def csv_to_struct():
    lista_dict = []
    with open('alunos2.csv', 'r', encoding='utf-8') as csvfile:
        header = None

        n_notas = 0
        for line in csvfile:
            fields = line.strip().split(',')
            print(fields)
            if re.search(r'\{\d+\}', line):
                n_notas = line.split('{')[1].split('}')[0]
                print(n_notas)

            if header is None:
                # Preenche o cabecalho com a primeira linha
                header = fields
            else:
                aluno = {}
                for i in range(4):
                    if i < 3:
                        aluno[header[i]] = fields[i]
                    else:
                        aluno[header[i]] = "".join(re.findall(r',\d+', line)).split(',')
                        break
                lista_dict.append(aluno)
    return lista_dict


# Objeto para uso
dados = csv_to_struct()

# Guarda o dicionario no formato json
with open("alunos.json", "w") as write_file:
    json.dump(dados, write_file, indent=4)


def main():
    exit_loop = -1

    while exit_loop != 0:
        print("\n*********************MENU***************************")
        print("|  Prima 1 para escolher o ficheiro 'alunos.csv'   |")
        print("|  Prima 2 para escolher o ficheiro 'alunos2.csv'  |")
        print("|  Prima 3 para escolher o ficheiro 'alunos3.csv'  |")
        print("|  Prima 4 para escolher o ficheiro 'alunos4.csv'  |")
        print("|  Prima 5 para escolher o ficheiro 'alunos5.csv'  |")
        print("|  Prima 0 para sair                               |")
        print("****************************************************\n")

        exit_loop = int(input("-> Escolha a opcao: "))
        if exit_loop == 0:
            print("Saindo.......")
            break
        if exit_loop == 1:
            print("Escolheu a opcao 1\n")
            input("Prima Enter para continuar")
        elif exit_loop == 2:
            print("Escolheu a opcao 2\n")
            input("Prima Enter para continuar")
        elif exit_loop == 3:
            print("Escolheu a opcao 3\n")
            input("Prima Enter para continuar")
        elif exit_loop == 4:
            print("Escolheu a opcao 4\n")
            input("Prima Enter para continuar")
        elif exit_loop == 5:
            print("Escolheu a opcao 5\n")
            input("Prima Enter para continuar")
        else:
            print("Tecla sem utilidade")
            input("Prima enter para continuar\n")


if __name__ == "__main__":
    main()
