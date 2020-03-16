class Pessoa:
    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    pedro = Pessoa(nome='Pedro')
    joão = Pessoa(pedro, nome='João')
    print(Pessoa.cumprimentar(joão))
    print(id(joão))
    print(joão.cumprimentar())
    print(joão.nome)
    print(joão.idade)
for filhos in joão.filhos:
    print(filhos.nome)