class Pessoa:
    olhos = 2

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
    joão.sobrenome = 'Silva'
    del pedro.filhos
    pedro.olhos = 1
    del pedro.olhos
    print(joão.__dict__)
    print(pedro.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(joão.olhos)
    print(pedro.olhos)
    print(id(Pessoa.olhos), id(joão.olhos), id(pedro.olhos))