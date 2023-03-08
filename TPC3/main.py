import json
import re


def main():
# Cria uma lista em que cada pessoa é um dicionario
    data = []
    with open('processos.txt', 'r', encoding='utf-8') as file:
        header = None
        for line in file:
            dicionario = {}
            dicionario["names"] = []
            i = 0
            r = re.split(r':+', line)
            for inf in r:
                if i == 0:
                    dicionario["id"] = inf
                elif i == 1:
                    dicionario["date"] = inf
                else:
                    pessoa = {}
                    nomes = re.split(r"(::[A-Z][a-z]+) [a-zA-Z ]*([A-Z][a-z]+)::", inf)
                    relacoes = re.search(r",\w+(\s\w+)*\.", inf)
                    n = nomes[0].split(' ')
                    pessoa["nome"] = n[0]
                    pessoa["apelido"] = n[-1]
                    if relacoes:
                        pessoa["parentesco"] = relacoes.group(0).split(',')[1].split('.')[0]
                    else:
                        pessoa["parentesco"] = None
                    if not re.search('^\n$', inf):
                        dicionario["names"].append(pessoa)
                i += 1
            if not re.search('^\n$', line):
                data.append(dicionario)



    exit_loop = -1

    while exit_loop != 0:
        print("1-Frequencia de processos por ano")
        print("2-Frequencia de nomes próprios e apelidos")
        print("3-Frequencia dos vários tipos de relação: irmão, sobrinho, etc")
        print("4-Converta todos registos num novo ficheiro de output mas em formato Json")
        print("0-Exit")

        exit_loop = int(input("Escolha a opcao "))
        if exit_loop == 0:
            print("Leaving.......")
            break
        elif exit_loop == 1:
            dici = {}
            for x in data:
                date = x["date"].split('-')[0]
                if date in dici:
                    dici[date] += 1
                else:
                    dici[date] = 0
            print(dici)
            input("Prima Enter para continuar")
        elif exit_loop == 2:
            dici = {}
            for x in data:
                for nome1 in x["names"]:
                    if nome1["nome"] in dici:
                        dici[nome1["nome"]] += 1
                    else:
                        dici[nome1["nome"]] = 1
                    if nome1["apelido"] in dici:
                        dici[nome1["apelido"]] += 1
                    else:
                        dici[nome1["apelido"]] = 1
            sorted_dic = sorted(dici.items(), key=lambda x: x[1])
            print(sorted_dic[-6:-1])
            input("Prima Enter para continuar")
        elif exit_loop == 3:
            dici = {}
            for x in data:
                for nome1 in x["names"]:
                    if nome1["parentesco"] in dici:
                        dici[nome1["parentesco"]] += 1
                    else:
                        dici[nome1["parentesco"]] = 1
            print(dici)
        elif exit_loop == 4:
            fileOut = open("processos.json", "w")
            json.dump(data, fileOut, indent=2, ensure_ascii=False)

        else:
            print("You didn't add anything")
            input("prima enter para continuar")



if __name__ == "__main__":
    main()
