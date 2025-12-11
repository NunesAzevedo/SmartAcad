import csv
import os
from enum import Enum

class TipoAtividade(Enum):
    TAREFA = 'Tarefa'
    TRABALHO = 'Trabalho'
    PROVA = 'Prova'

class StatusAtividade(Enum):
    PENDENTE = 'Pendente'
    ANDAMENTO = 'Andamento'
    CONCLUIDO = 'Concluido'

class Atividade:
    def __init__(self, nome: str, id: int, tipo: TipoAtividade):
        self._nome = nome
        self._id = id
        self._tipo: TipoAtividade = tipo


class AtividadeDisciplina:
    def __init__(self, nota: float, peso: float, status: StatusAtividade, atividade: Atividade):
        self._nota = nota
        self._peso = peso
        self._status: StatusAtividade = status
        self._atividade: Atividade = atividade

    def registrarNota(self, nota: float) -> None: 
        # --- Implementação da funcionalidade ... ---
    
    def atualizarPeso(self, peso:float) -> None:
        # --- Implementação da funcionalidade ... ---
    
    def marcarConcluida(self) -> None:
        # --- Implementação da funcionalidade ... ---

class Disciplina:
    def __init__(self, codigo: str, nome: str, cargaHoraria: int, mediaFinal: float):
        self._codigo = codigo
        self._nome = nome
        self._cargaHoraria = int(cargaHoraria)
        self._mediaFinal = float(mediaFinal)
        self._atividades: list[Atividade] = []

    def adicionarAtividades(self, atv: Atividade) -> None:
        # --- Implementação da funcionalidade ... ---

    def removerAtividades(self, atv: Atividade) -> None:
        # --- Implementação da funcionalidade ... ---

    def atualizarMediaFinal(self, mediaFinal: float) -> None:
        # --- Implementação da funcionalidade ... ---
   

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
        return Disciplina(linha[0], linha[1], int(linha[2]), float(linha[3]))


    # --- Getters - Permite acesso aos dados pelo DisciplinaService
    @property 
    def codigo(self): return self._codigo

    @property 
    def nome(self): return self._nome

    @property 
    def cargaHoraria(self): return self._cargaHoraria

    @property 
    def mediaFinal(self): return self._mediaFinal



class DisciplinaService:
    BD_DISCIPLINAS = 'disciplinas.csv'

    def __init__(self):
        # Dicionário com código da disciplina como key
        self._bdDisciplinas: dict[str, Disciplinas] = {}
        self._carregarDados() # Carrega dados do arquivo CSV

    # --- Métodos Privados
    def _carregarDados(self):
        """
        Carrega o arquivo CSV para o dicionário 
        """
        if not os.path.exists(self.BD_DISCIPLINAS):
            return 
        
        with open(self.BD_DISCIPLINAS, mode='r', newline='', encoding='utf-8') as csvFile:
            reader = csv.reader(csvFile)
            for line in reader:
                if line: # Verifica se a linah está vazia
                    disciplina = Disciplina.carregaDados(line)
                    self._bdDisciplinas[disciplina.codigo] = disciplina

    def _salvaDados(self):
        """
        Atualiza o Banco de Dados (Arquivo CSV)
        """
        with open(self.BD_DISCIPLINAS, mode='w', newline='', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile)
            for disciplina in self._bdDisciplinas.values():
                writer.writerow(disciplina.salvaDados())


    # --- Métodos Públicos
    def criarDisciplina(self, codigo: str, nome: str, cargaHoraria: int) -> None:
        # --- Implementação da funcionalidade ... ---

    def editarDisciplina(self, codigo: str, nome: str, cargaHoraria: int) -> None:
        # --- Implementação da funcionalidade ... ---
  
    def excluirDisciplina(self, codigo: str) -> None:
        # --- Implementação da funcionalidade ... ---

    def associarAtividade(self, dis: Disciplina, atv: Atividade, peso: float) -> None:
        # --- Implementação da funcionalidade ... ---


class MediaService:
    def __init__(self, dis: Disciplina):
        self._dis: Disciplina = dis

    def calcularMediaTipo(self):
        # --- Implementação da funcionalidade ... ---

    def calcularMediaFinal(self):
        # --- Implementação da funcionalidade ... ---



