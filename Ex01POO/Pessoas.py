class Pessoas:
    def __init__(self,nome,idade, Falando=False,Comendo=False):
        self.nome = nome
        self.idade = idade
        self.Falando = Falando
        self.Comendo = Comendo
    def comer(self,comida):
        if self.Comendo == True:
            print(f'{self.nome} já está comendo!')
        elif self.Falando == True:
            print(f'{self.nome} está falando e não pode comer agora!')
        else:
            self.comendo = True
            print(f'{self.nome} está comendo {comida} agora!')
    def falar(self,fala):
        if self.Falando == True:
            print(f'{self.nome} já está falando!')
        elif self.Comendo == True:
            print(f'{self.nome} está comendo e não pode falar agora!')
        else:
            self.Falando = True
            print(f'{self.nome} está falando {fala} agora!')
    def parar_Falar(self):
        if self.Falando == False:
            print(f'{self.nome} não estava falando!')
        elif self.Comendo == True:
            print(f'{self.nome} não estava falando, e sim comendo!')
        else:
            self.Falando = False
            print(f'{self.nome} Não está mais falando!')
    def parar_Comer(self):
        if self.Comendo == False:
            print(f'{self.nome} não estava comendo!')
        elif self.Falando == True:
            print(f'{self.nome} não estava comendo, e sim falando!')
        else:
            self.Comendo = False
            print(f'{self.nome} Não está mais comendo!')
    def getNome(self):
        return self.nome
    def getComendo(self):
        return self.Comendo
    def getFalando(self):
        return self.Falando
