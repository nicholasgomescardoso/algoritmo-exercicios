# Atividade 05 - Estruturas de selecao (aninhada, elif, match case)

def verificar_emprestimo():
    dias_atraso = int(input("Digite os dias de atraso da devolucao (0 se em dia): "))
    tem_reserva_pendente = input("O livro tem reserva pendente? (s/n): ").lower()

    if dias_atraso == 0:
        print("EMPRESTIMO REGULAR")
    else:
        if tem_reserva_pendente == "s":
            print("BLOQUEADO - devolucao urgente")
        else:
            print("ATRASADO - multa aplicada")


def classificar_livro():
    avaliacoes = float(input("Digite a media de avaliacoes do livro (0 a 5): "))

    if avaliacoes >= 4.5:
        print("BEST-SELLER")
    elif avaliacoes >= 3.5:
        print("RECOMENDADO")
    elif avaliacoes >= 2.0:
        print("MEDIANO")
    else:
        print("POUCO PROCURADO")


def processar_menu():
    print("1 - Listar livros\n2 - Cadastrar livro\n3 - Buscar por autor")
    opcao = input("Digite a opcao desejada: ")

    match opcao:
        case "1":
            print("Listar livros")
        case "2":
            print("Cadastrar livro")
        case "3":
            print("Buscar por autor")
        case _:
            print("Opcao invalida")


def avaliar_livro():
    titulo = input("Digite o titulo do livro: ")
    avaliacao = float(input("Digite a avaliacao do livro (0 a 5): "))
    exemplares = int(input("Digite o numero de exemplares disponiveis: "))

    dados = (avaliacao, exemplares)

    match dados:
        case (a, _) if a >= 4.5:
            print(f"{titulo}: DESTAQUE DO ACERVO")
        case (a, e) if a >= 3.5 and e > 0:
            print(f"{titulo}: DISPONIVEL E RECOMENDADO")
        case (a, e) if a >= 2.0 and e > 0:
            print(f"{titulo}: DISPONIVEL")
        case _:
            print(f"{titulo}: INDISPONIVEL")


def main():
    opcao = ""
    while opcao != "5":
        print("\n1-Emprestimo 2-Classificar livro 3-Menu 4-Avaliar livro 5-Sair")
        opcao = input("Escolha uma opcao: ")

        match opcao:
            case "1":
                verificar_emprestimo()
            case "2":
                classificar_livro()
            case "3":
                processar_menu()
            case "4":
                avaliar_livro()
            case "5":
                print("Saindo...")
            case _:
                print("Opcao invalida")


main()