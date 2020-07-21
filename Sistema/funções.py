from random import randint

class Aluno():
    def __init__(self, nome, idade, serie, turma, periodo):
        self.nome = nome
        self.idade = idade
        self.serie = serie
        self.turma = turma
        self.periodo = periodo


#def registro_do_aluno():



    def registrar_aluno():
        r_a = Aluno.registrar_aluno()
        nome = input('Nome do aluno: ')
        idade = input('Idade: ')
        serie = input('Serie: ')
        turma = input('Turma: ')
        periodo = input('Periodo: ')
        r_a = Aluno(nome, idade, serie, turma, periodo)

        return r_a
        

def titulo(txt):
    c = len(txt) + 10
    print("==" * c)
    print(txt)
    print("==" * c)