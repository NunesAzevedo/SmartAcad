import csv
import os
from enum import Enum


class TipoAtividade(Enum):
    TAREFA = "Tarefa"
    TRABALHO = "Trabalho"
    PROVA = "Prova"


class StatusAtividade(Enum):
    PENDENTE = "Pendente"
    ANDAMENTO = "Andamento"
    CONCLUIDO = "Concluido"


class Atividade:
    def __init__(self, nome: str, id: int, tipo: TipoAtividade):
        self._nome = nome
        self._id = int(id)
        self._tipo: TipoAtividade = tipo


class AtividadeDisciplina:
    def __init__(
        self, nota: float, peso: float, status: StatusAtividade, atividade: Atividade
    ):
        self._nota = float(nota)
        self._peso = float(peso)
        self._status: StatusAtividade = status
        self._atividade: Atividade = atividade

    def registrarNota(self, nota: float) -> None:
        self._nota = nota

    def atualizarPeso(self, peso: float) -> None:
        self._peso = peso

    def marcarConcluida(self) -> None:
        self._status.CONCLUIDO


class Disciplina:
    def __init__(self, codigo: str, nome: str, cargaHoraria: int, mediaFinal: float):
        self._codigo = codigo
        self._nome = nome
        self._cargaHoraria: int = cargaHoraria
        self._mediaFinal: float = mediaFinal
        self._atividades: list[Atividade] = []

    def adicionarAtividade(self, atv: Atividade) -> None:
        self._atividades.append(atv)

    def removerAtividade(self, id: int) -> None:
        for atv in self._atividades:
            if atv._id == id:
                self._atividades.remove(atv)
                return
                

    def atualizarMediaFinal(self, mediaFinal: float) -> None:
        self._mediaFinal = mediaFinal

    # --- Métodos de tratamento de dados em .csv
    """
    O objeto "Disciplina" terá seus dados salvos 
    da seguinte forma no arquivo CSV:
    ---
    codigo, nome, cargaHoraria, mediaFinal
    ---
    """

    def salvaDados(self) -> list:
        """
        Retorna uma lista com os dados da disciplina
        para salvar no arquivo CSV
        ---
        Objeto Disciplina -> Arquivo CSV
        ---
        """
        return [self._codigo, self._nome, self._cargaHoraria, self._mediaFinal]

    @staticmethod
    def carregaDados(linha: list):
        """
        Carrega uma linha do arquivo CSV e
        retorna um objeto "Disciplina"
        ---
        Arquivo CSV -> Objeto Disciplina
        ---
        """
        return Disciplina(linha[0], linha[1], linha[2], linha[3])

    # --- Getters - Permite acesso aos dados pelos objetos do tipo Service
    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def cargaHoraria(self):
        return self._cargaHoraria

    @property
    def mediaFinal(self):
        return self._mediaFinal


class DisciplinaService:
    BD_DISCIPLINAS = "disciplinas.csv"

    def __init__(self):
        # Dicionário com código da disciplina como key
        self._bdDisciplinas: dict[str, Disciplina] = {}
        self._carregarDados()  # Carrega dados do arquivo CSV

    # --- Métodos Privados
    def _carregarDados(self):
        """
        Carrega o arquivo CSV para o dicionário
        CSV -> Dicionário
        """
        if not os.path.exists(self.BD_DISCIPLINAS):
            return

        with open(
            self.BD_DISCIPLINAS, mode="r", newline="", encoding="utf-8"
        ) as csvFile:
            reader = csv.reader(csvFile)
            for line in reader:
                if line:  # Verifica se a linah está vazia
                    disciplina = Disciplina.carregaDados(line)
                    self._bdDisciplinas[disciplina.codigo] = disciplina

    def _salvaDados(self):
        """
        Salva o Banco de Dados no arquivo CSV
        Dicionário -> CSV
        """
        with open(
            self.BD_DISCIPLINAS, mode="w", newline="", encoding="utf-8"
        ) as csvFile:
            writer = csv.writer(csvFile)
            for disciplina in self._bdDisciplinas.values():
                writer.writerow(disciplina.salvaDados())

    # --- Métodos Públicos
    def criarDisciplina(
        self, codigo: str, nome: str, cargaHoraria: int, mediaFinal: float
    ) -> None:
        codigo = str(codigo).strip()
        if codigo in self._bdDisciplinas:
            print(f"[ERRO]: A disciplina de codigo {codigo} ja existe!")
            return

        new_dis = Disciplina(codigo, nome, cargaHoraria, mediaFinal)
        self._bdDisciplinas[codigo] = new_dis
        self._salvaDados()
        print(f"A disciplina {codigo} - {nome} foi cadastrada com sucesso")

    def editarDisciplina(
        self, codigo: str, nome: str, cargaHoraria: int, mediaFinal: float
    ) -> None:
        codigo = str(codigo).strip()
        if codigo not in self._bdDisciplinas:
            print(f"[ERRO]: A disciplina {codigo} nao existe!")
            return

        dis = self._bdDisciplinas[codigo]
        dis._nome = nome
        dis._cargaHoraria = cargaHoraria
        dis._mediaFinal = mediaFinal

        self._salvaDados()
        print(f"A disciplina {codigo} - {nome} foi editada com sucesso")

    def excluirDisciplina(self, codigo: str) -> None:
        codigo = str(codigo).strip()
        if codigo not in self._bdDisciplinas:
            print(f"[ERRO]: A disciplina {codigo} nao existe!")
            return

        nome = self._bdDisciplinas[codigo]._nome
        self._bdDisciplinas.pop(codigo)
        self._salvaDados()
        print(f"A disciplina {codigo} - {nome} foi excluida com sucesso")

    def associarAtividade(self, dis: Disciplina, atv: Atividade) -> None:
        if dis._codigo not in self._bdDisciplinas:
            print(f"[ERRO]: A disciplina {dis._codigo} nao existe!")
            return

        disciplina = self._bdDisciplinas[dis._codigo]
        disciplina._atividades.append(atv)
        self._salvaDados()

        print(
            f"A atividade {atv._nome} foi adicionada a disciplina {dis._codigo} - {dis._nome}"
        )


class MediaService:
    def __init__(self, dis: Disciplina):
        self._dis: Disciplina = dis

    def calcularMediaTipo(self):
        # --- Implementação da funcionalidade ... ---
        print("Implementacao nao realizada")

    def calcularMediaFinal(self):
        # --- Implementação da funcionalidade ... ---
        print("Implementacao nao realizada")
