from prettytable import PrettyTable


# Cria uma lista em que cada pessoa é um dicionario
def struct():
    data = []
    with open('myheart.csv', 'r', encoding='utf-8') as csvfile:
        header = None
        for line in csvfile:
            fields = line.strip().split(',')
            if len(fields) <= 6:
                if header is None:
                    # Preenche o cabecalho com a primeira linha
                    header = fields
                else:
                    pessoa = {header[i]: fields[i] for i in range(len(header))}
                    data.append(pessoa)
    return data


# Função que calcula a distribuição da doença por sexo
def dist_sex(data):
    homem_doente = homem = mulher_doente = mulher = 0
    for elemento in data:
        if elemento["sexo"] == 'M':
            homem = homem + 1
            if elemento["temDoença"] == "1":
                homem_doente = homem_doente + 1
        elif elemento["sexo"] == 'F':
            mulher = mulher + 1
            if elemento["temDoença"] == "1":
                mulher_doente = mulher_doente + 1

    dist_hom = int((homem_doente / homem) * 100)
    dist_mul = int((mulher_doente / mulher) * 100)

    dict_sex = {"Homem": dist_hom, "Mulher": dist_mul}

    return dict_sex


# distribuição da doença por escalões etários
def dist_escalao(data):
    # dicionario que contem o numero de pessoas doentes por idade
    dic_escalao = {}
    for pessoa in data:
        if pessoa["temDoença"] == "1":
            if pessoa["idade"] in dic_escalao.keys():
                dic_escalao[pessoa["idade"]] = dic_escalao[pessoa["idade"]] + 1
            else:
                dic_escalao[pessoa["idade"]] = 1
    return dic_escalao


# distribuição da doença por colesterol
def dist_colesterol(data):
    # dicionario que contem o numero de pessoas doentes por idade
    dic_escalao = {}
    for pessoa in data:
        if pessoa["colesterol"] in dic_escalao.keys():
            dic_escalao[pessoa["colesterol"]] = dic_escalao[pessoa["colesterol"]] + 1
        else:
            dic_escalao[pessoa["colesterol"]] = 1
    return dic_escalao


def calcula(dicionario, escala=10):
    dic_final = {}
    x = sorted(dicionario.keys())
    sorted_dict = {key: dicionario[key] for key in x}

    resto = int(list(sorted_dict.keys())[0]) % escala
    i = int(list(sorted_dict.keys())[0]) - resto
    for key, value in sorted_dict.items():
        if int(key) in range(i, i + escala):
            if str(i) + "-" + str(i + escala) in dic_final.keys():
                dic_final[str(i) + "-" + str(i + escala)] = dic_final[str(i) + "-" + str(i + escala)] + value
            else:
                dic_final[str(i) + "-" + str(i + escala)] = value
        else:
            resto = int(key) % escala
            i = int(key) - resto
            dic_final[str(i) + "-" + str(i + escala)] = value

    print(dic_final)
    return dic_final


def tabela_dist(dic: dict, subject: str):
    table = PrettyTable(["Intervalo", subject])

    for content, number in dic.items():
        table.add_row([content, number])

    return table
