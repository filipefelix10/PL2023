import estrutura

x = estrutura.struct()


def main():
    exit_loop = -1

    while exit_loop != 0:
        print("1-Informacao do ficheiro num modelo")
        print("2-Distribuicao da doenca por sexo")
        print("3-Distribuicao da doenca por escaloes etarios")
        print("4-Distribuicao da doenca por niveis de colesterol")
        print("0-Exit")

        exit_loop = int(input("Escolha a opcao "))
        if exit_loop == 0:
            print("Leaving.......")
            break
        elif exit_loop == 1:
            print(x)
            input("Prima Enter para continuar")
        elif exit_loop == 2:
            print(estrutura.tabela_dist(estrutura.dist_sex(x), "Percentagem"))
            input("Prima Enter para continuar")
        elif exit_loop == 3:
            print(estrutura.tabela_dist(estrutura.calcula(estrutura.dist_escalao(x), 5), "Idade"))
            input("Prima Enter para continuar")
        elif exit_loop == 4:
            print(estrutura.tabela_dist(estrutura.calcula(estrutura.dist_colesterol(x), 10), "colesterol"))
            input("Prima Enter para continuar")
        else:
            print("You didn't add anything")
            input("prima enter para continuar")


if __name__ == "__main__":
    main()
