# Definição de uma classe
class Pessoa:
    # Método construtor, inicializa o objeto
    def __init__(self, nome, idade): #init=construtor
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade

    # Método para exibir informações
    def mostrar_info(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa('João', 25)
pessoa1.mostrar_info()  # Output: Nome: João, Idade: 25

pessoa2 = Pessoa('Maria', 15)
pessoa2.mostrar_info()  

pessoa3 = Pessoa('Gustavo', 38)
pessoa3.mostrar_info()  