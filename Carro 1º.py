class Carro:
    def __init__(self, cor, cilindrada):
        self.cor = cor
        self.cilindrada = cilindrada
        self.velocidade = 0
        
    def acelerar(self):
        self.velocidade += 10
    
    def travar(self):
        self.velocidade = 0
        
meu_carro = Carro("vermelho", 1600)
carro_do_pai = Carro("preto", 2000)
carro_do_neto = Carro("roxo brilhante", 5300)

print(meu_carro.cor)
print(carro_do_pai.cilindrada)
print(carro_do_neto.cor)
print(carro_do_neto.cilindrada)


carro_do_neto.acelerar()
print(carro_do_neto.velocidade)

carro_do_neto.travar()
print(carro_do_neto.velocidade)

