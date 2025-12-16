import classes as cls


def main():
    inter = Interface()

    inter.bemVindo()
    inter.selecionaOpcao()
    opc = input(int("Operacao selecionada: "))

    if opc == 0:  # Cancelar Operação
        inter.operacaoCancelada()
        return
    elif opc == 1:  # Cadastrar Disciplina
        inter.cadastraDisciplina()
        codigo = input(str("Insira o codigo da disciplina a ser cadastrada"))


class Interface:
    def __init__(self): ...

    def bemVindo():
        print("##################################")
        print("# Seja Bem-vindo(a) ao SmartAcad #")
        print("##################################")

    def selecionaOpcao(self):
        print("====================")
        print("Selecione uma opcao:")
        print("====================")

        print("[0] - Cancelar Operação")
        print("[1] - Cadastrar Disciplina")
        print("[2] - Editar Disciplina")
        print("[3] - Excluir Disciplina")
        print("[4] - Associar atividade a uma Disciplina")

    def operacaoCancelada(self):
        print("##############################")
        print("Obrigado por usar a SmartAcad!")
        print("##############################")

    def cadastraDisciplina():
        print("##############################")
        print("#   Cadastro de Disciplina   #")
        print("##############################")

    def editaDisciplina():
        print("##############################")
        print("#    Edicao de Disciplina    #")
        print("##############################")

    def excluiDisciplina():
        print("##############################")
        print("#   Exclusao de Disciplina   #")
        print("##############################")

    def associaAtividade():
        print("##############################")
        print("#  Associacao de Atividade   #")
        print("##############################")


if __name__ == "__main__":
    main()
