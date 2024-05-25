class Jogo:
    def __init__(self, nome):
        self.nome = nome
        self.escolha = ""

    def pedra(self):
        if self.escolha == "":
            print(f'{self.nome} jogou pedra')
            self.escolha = 'pedra'

    def tesoura(self):
        if self.escolha == "":
            print(f'{self.nome} jogou tesoura')
            self.escolha = 'tesoura'

    def papel(self):
        if self.escolha == "":
            print(f'{self.nome} jogou papel')
            self.escolha = 'papel'

    def resultado(self, jogador):
        if self.escolha == "":
            print(f'{self.nome} não fez uma jogada ainda.')
            return

        if self.escolha == jogador.escolha:
            print('Empate!')
            return

        if (self.escolha == 'pedra' and jogador.escolha == 'tesoura' or
            self.escolha == 'tesoura' and jogador.escolha == 'papel' or
            self.escolha == 'papel' and jogador.escolha == 'pedra'):
            print(f'{self.nome} ganhou!')
        else:
            print(f'{jogador.nome} ganhou!')



