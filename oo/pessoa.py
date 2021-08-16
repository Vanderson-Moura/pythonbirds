class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':

    vanderson = Pessoa(nome='Vanderson')
    moura = Pessoa(vanderson, nome='Moura')
    print(Pessoa.cumprimentar(moura))
    print(id(moura))
    print(moura.cumprimentar())
    print(moura.nome)
    print(moura.idade)
    for filho in moura.filhos:
        print(filho.nome)
    moura.sobrenome = 'Soares'
    del moura.filhos
    moura.olhos = 1
    del moura.olhos
    print(vanderson.__dict__)
    print(moura.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(moura.olhos)
    print(vanderson.olhos)
    print(id(Pessoa.olhos), id(moura.olhos), id(vanderson.olhos))