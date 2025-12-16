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
        
        # Verifica se o código da disciplina já foi cadastrado no sistema
        isCodigoValid = cls.Control().validaDisciplina(codigo)
        if !(isCodigoValid):
            inter.erro()
            return
       
        
        inter.inserirDadosDisciplina()
        nome = input(str("Nome: "))
        cargaHoraria = input(int("Carga Horaria: "))
        pesoTarefa = input(float("Peso da Tarefa: "))
        pesoTrabalho = input(float("Peso do Trabalho: "))
        pesoProva = input(float("Peso da Prova: "))
        pesos = {pesoTarefa, pesoTrabalho, pesoProva}
        cls.Control().criarDisciplina(codigo, nome, cargaHoraria, pesos)

    elif opc == 2: # Editar Disciplina
        inter.editaDisciplina()
    
        codigo = input(str("Insira o codigo da disciplina a ser editada"))
        
        # Verifica se o código da disciplina já foi cadastrado no sistema
        isCodigoValid = cls.Control().validaDisciplina(codigo)
        if !(isCodigoValid):
            inter.erro()
            return
       
        inter.inserirDadosDisciplina()
        nome = input(str("Nome: "))
        cargaHoraria = input(int("Carga Horaria: "))
        pesoTarefa = input(float("Peso da Tarefa: "))
        pesoTrabalho = input(float("Peso do Trabalho: "))
        pesoProva = input(float("Peso da Prova: "))
        pesos = {pesoTarefa, pesoTrabalho, pesoProva}
        cls.Control().editarDisciplina(codigo, nome, cargaHoraria, pesos)
    
    elif opc == 3: # Excluir Disciplina
        inter.excluiDisciplina()
    
        codigo = input(str("Insira o codigo da disciplina a ser excluida"))
        
        # Verifica se o código da disciplina já foi cadastrado no sistema
        isCodigoValid = cls.Control().validaDisciplina(codigo)
        if !(isCodigoValid):
            inter.erro()
            return
      
        cls.Control().excluirDisciplina(codigo)
    
    elif opc == 4: # Associar Atividade a uma Disciplina
        inter.associaAtividade()
    
        

class Interface:
    def __init__(self): ...

    def bemVindo(self):
        print("##################################")
        print("# Seja Bem-vindo(a) ao SmartAcad #")
        print("##################################")

    def erro(self):
        print("===================================")
        print("Ocorreu um erro, tente novamente...")
        print("===================================")


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

    def cadastraDisciplina(self):
        print("##############################")
        print("#   Cadastro de Disciplina   #")
        print("##############################")

    def editaDisciplina(self):
        print("##############################")
        print("#    Edicao de Disciplina    #")
        print("##############################")

    def excluiDisciplina(self):
        print("##############################")
        print("#   Exclusao de Disciplina   #")
        print("##############################")

    def associaAtividade(self):
        print("##############################")
        print("#  Associacao de Atividade   #")
        print("##############################")


    def inserirDadosDisciplina(self):
        print("==============================================")
        print("Insira os dados da Disciplina a ser cadastrada")
        print("==============================================")
    





if __name__ == "__main__":
    main()
