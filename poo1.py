class Animal: #classe pai
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal): #classes filhas, herdam a classe pai e o que tem de dif é o som
    def fazer_som(self):
        print('Au Au!')

class Gato(Animal):
    def fazer_som(self):
        print('Miau!')

cachorro = Cachorro('Rex')
gato = Gato('Felix')

cachorro.fazer_som()  # Output: Au Au! #instanciando 
gato.fazer_som()  # Output: Miau!