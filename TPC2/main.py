def main():
    print("Escreva o seu texto, linha a linha. Para sair da escrita, basta pressionar Enter com a linha vazia.")
    result = 0
    on = ""
    off = ""
    while True:
        line = input()
        if line:
            i = 0
            actual = "0"
            ate_agr = 0
            while i < len(line):
                if line[i].isdigit():
                    actual = actual + line[i]
                    i += 1
                else:
                    if on.lower() == "on" or off.lower() != "off":
                        if line[i] == "=":
                            print(result + ate_agr)
                        ate_agr += int(actual)
                    if line[i].lower() == "o":
                        off += "o"
                        if i + 1 < len(line):
                            if line[i + 1].lower() == 'n':
                                on += "on"
                                off = ""
                            if i + 2 < len(line) and line[i + 1].lower() == 'f' and line[i + 2].lower() == 'f':
                                off = "off"
                                on = ""
                    actual = "0"
                    i += 1
            if on.lower() == "on" or off.lower() != "off":
                result += ate_agr + int(actual)
            else:
                result += ate_agr
        else:
            break

    print("O resultado total:")
    print(result)


if __name__ == "__main__":
    main()
