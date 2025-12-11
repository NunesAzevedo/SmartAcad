import classes as cls


def main():
    # cls.DisciplinaService().criarDisciplina("111", "POO", 120, 9.5)
    cls.DisciplinaService().criarDisciplina("123", "Calculo I", 120, 9.5)
    cls.DisciplinaService().criarDisciplina("SMA178", "Calculo II", 120, 8.7)
    cls.DisciplinaService().criarDisciplina("SCC-7897", "ICC 1", 180, 10.0)
    # cls.DisciplinaService().editarDisciplina("123", "Calculo I", 120, 9.8)
    # cls.DisciplinaService().excluirDisciplina("123")


if __name__ == "__main__":
    main()
