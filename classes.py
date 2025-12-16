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
    def __init__(
        self,
        nome: str,
        id: int,
        tipo: TipoAtividade,
        status: StatusAtividade = StatusAtividade.PENDENTE,
    ):
        self._nome: str = nome
        self._id: int = id
        self._tipo: TipoAtividade = tipo
        self._nota: float = 0.0
        self._status: StatusAtividade = status

    def registrarNota(self, nota: float) -> None:
        self._nota = nota

    def atualizarStatus(self, status: StatusAtividade) -> None:
        self._status = status


class Disciplina:
    def __init__(self, codigo: str, nome: str, cargaHoraria: int):
        self._codigo = codigo
        self._nome = nome
        self._cargaHoraria: int = cargaHoraria
        self._pesos: list[float] = []
        self._atividades: list[AtividadeDisciplina] = []
        self._mediaTarefa: float = 0.0
        self._mediaTrabalho: float = 0.0
        self._mediaProva: float = 0.0
        self._mediaFinal: float = 0.0

    def adicionarAtividade(self, atv: Atividade) -> None:
        self._atividades.append(atv)

    def atualizarPesos(self, listaPeso: list[float]) -> None:
        self._pesos = listaPeso

    def atualizarMediaTarefa(self, mediaTarefa: float) -> None:
        """Implementação da funcionalidade..."""

    def atualizarMediaTrabalho(self, mediaTrabalho: float) -> None:
        """Implementação da funcionalidade..."""

    def atualizarMediaProva(self, mediaProva: float) -> None:
        """Implementação da funcionalidade..."""

    def atualizarMediaFinal(self, mediaFinal: float) -> None:
        self._mediaFinal = MediaService(self).calcularMediaFinal()

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


class Control:
    BD_DISCIPLINAS = "disciplinas.csv"

    def __init__(self):
        # Dicionário com código da disciplina como key
        self._bdDisciplinas: dict[str, Disciplina] = {}
        self._carregarDados()  # Carrega dados do arquivo CSV

    def carregarDados(self) -> None:
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

    def salvaDados(self) -> None:
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

    def validaDisciplina(self, codigo: str) -> bool:
        codigo = str(codigo).strip()
        if codigo in self._bdDisciplinas:
            print(f"[ERRO]: A disciplina de codigo {codigo} ja existe!")
            return False
        else:
            return True

    def criarDisciplina(
        self, codigo: str, nome: str, cargaHoraria: int, pesos: list[float]
    ) -> None:
        codigo = str(codigo).strip()
        if codigo in self._bdDisciplinas:
            print(f"[ERRO]: A disciplina de codigo {codigo} ja existe!")
            return

        new_dis = Disciplina(codigo, nome, cargaHoraria)
        new_dis._pesos = pesos
        self._bdDisciplinas[codigo] = new_dis
        self._salvaDados()
        print(f"A disciplina {codigo} - {nome} foi cadastrada com sucesso")

    def editarDisciplina(
        self, codigo: str, nome: str, cargaHoraria: int, pesos: list[float]
    ) -> None:
        codigo = str(codigo).strip()
        if codigo not in self._bdDisciplinas:
            print(f"[ERRO]: A disciplina {codigo} nao existe!")
            return

        dis = self._bdDisciplinas[codigo]
        dis._nome = nome
        dis._cargaHoraria = cargaHoraria
        dis._pesos = pesos

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

    def associarAtividade(self, codigo: str, atv: Atividade) -> None:
        if codigo not in self._bdDisciplinas:
            print(f"[ERRO]: A disciplina {codigo} nao existe!")
            return

        dis = self._bdDisciplinas[codigo]
        dis._atividades.append(atv)
        self._salvaDados()

        print(
            f"A atividade {atv._nome} foi adicionada a disciplina {codigo} - {dis._nome}"
        )

    def calcularMediaTipo(self, codigo: str, tipo: TipoAtividade) -> None:
        if codigo not in self._bdDisciplinas:
            print(f"[ERRO]: A disciplina {codigo} nao existe!")
            return

        somaNotas = 0
        dis = self._bdDisciplinas[codigo]
        atividades = dis._atividades

        for atv in atvividades:
            if atv._tipo == tipo:
                somaNotas += atv._nota

        if tipo == TipoAtividade.TAREFA:
            dis.atualizarMediaTarefa(media)
        elif tipo == TipoAtividade.TRABALHO:
            dis.atualizarMediaTrabalho(media)
        elif tipo == TipoAtividade.PROVA:
            dis.atualizarMediaProva(media)

    def calcularMediaFinal(self, codigo: str) -> None:
        if codigo not in self._bdDisciplinas:
            print(f"[ERRO]: A disciplina {codigo} nao existe!")
            return

        somaNotas = 0
        somaPesos = 0
        atvividades = self._dis._atividades

        dis = self._bdDisciplinas[codigo]

        pesoTarefa = dis._pesos[0]
        pesoTrabalho = dis._pesos[1]
        pesoProva = dis._pesos[2]

        somaPesos = pesoTarefa + pesoTrabalho + pesoProva

        mediaFinal = dis.mediaTarefa * pesoTarefa
        mediaFinal += dis.mediaTrabalho * pesoTrabalho
        mediaFinal += dis.mediaProva * pesoProva

        mediaFinal = mediaFinal / somaPesos

        dis.atualizarMediaFinal(mediaFinal)

        # Proteção para divisão por 0
        if somaPesos == 0.0:
            return 0.0

        media = somaNotas / somaPesos
        return media
