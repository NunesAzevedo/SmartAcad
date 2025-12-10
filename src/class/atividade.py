import csv
import os

class TipoAtividade:
    def __init__(self, tipo: str):
        self._tipo = tipo  # tipos = {Tarefa, Trabalho, Prova}

class StatusAtividade:
    def __init__(self, status: str):
        self._status = status # status = {Pendente, Andamento, Concluido}

class Atividade:
    def __init__(self, nome: str, id: int, tipo: TipoAtividade):
        self._nome = nome
        self._id = id
        self._tipo: TipoAtividade = tipo


class AtividadeDisciplina:
    def __init__(self, nota: double, peso: double, status: StatusAtividade, atividade: Atividade):
        self._nota = nota
        self._peso = peso
        self._status: StatusAtividade = status
        self._atividade: Atividade = atividade

    def registrarNota(self, nota: double) -> None:
    # --- Implementação da funcionalidade ... ---
    
    def atualizarPeso(self, peso:double) -> None:
    # --- Implementação da funcionalidade ... ---
    
    def marcarConcluida(self) -> None:
    # --- Implementação da funcionalidade ... ---

class Disciplina:
    def __init__(self, codigo: str, nome: str, cargaHoraria: int, mediaFinal: double):
        self._codigo = codigo
        self._nome = nome
        self._cargaHoraria = int(cargaHoraria)
        self._mediaFinal = double(mediaFinal)
        self._atividades = []

    def adicionarAtividades(atv: Atividade) -> None:
    # --- Implementação da funcionalidade ... ---

    def removerAtividades(atv: Atividade) -> None:
    # --- Implementação da funcionalidade ... ---

    def atualizarMediaFinal(mediaFinal: double) -> None:
    # --- Implementação da funcionalidade ... ---


    # --- Getters - Permite acesso aos dados pelo DisciplinaService
    @property 
    def codigo(self): return self._codigo

    @property 
    def nome(self): return self._nome

    @property 
    def cargaHoraria(self): return self._cargaHoraria

    
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
        return Disciplina(linha[0], linha[1], int(linha[2]), double(linha[3]))

class DisciplinaService:
    BD_DISCIPLINAS = 'disciplinas.csv'

    def __init__(self):
        # Dicionário com código da disciplina como key
        self._bdDisciplinas: dict[str, Disciplinas] = {}
        self._carregarDados() # Carrega dados do arquivo CSV

    def _carregarDados(self):
        """
        Carrega o arquivo CSV para o dicionário 
        """
        if not os.path.exists(self.BD_DISCIPLINAS):
            return 

        
        with open(self.BD_DISCIPLINAS, mode='r', newline='', encoding='utf-8') as csvFile:
            




