
"""Faça um programa em Python composto por funções que implemente o cenário descrito a seguir. 

Cenário (história do usuário)
Como Diretor Acadêmico do IFRN eu preciso de um programa para matricular estudantes em uma turma.
Deve ser possível, além de inserir o estudante na turma, obter a lista de todos os matriculados,
obter um aluno dada a sua matrícula e verificar se um estudante já está matriculado. 

Estudante: matricula, nome, curso, período(1, 2, 3...)

Testes:
1. Adicione pelo menos 3 estudantes na turma;
2. liste todos os estudantes;
3 busque (e obtenha) um estudante dada a sua matrícula."""

turma = {202501:"Bruce Wayne" , 202502: "Isaac Asimov", 202503: "Luke Skywalker"}

def adcionar_estudante (nome, matricula):
    global turma
    turma = {202501:"Bruce Wayne" , 202502: "Isaac Asimov", 202503: "Luke Skywalker"}
    turma[matricula] = nome
        
    
def consultar_matricula(matricula):
    return turma[matricula]
   
