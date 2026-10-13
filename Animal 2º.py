class Animal:
    def __init__(self, raca, porte, idade):
        self.raca = raca
        self.porte = porte
        self.idade = idade
        self.late = 0
        
    def latir(self):
        self.late += 1
        
    def parar_de_latir(self):
        self.late = 0


Cao_1 = Animal("Pitbull", "Grande", "3")
print("Raça: ", Cao_1.raca)
print("Porte: ",Cao_1.porte)
print("Idade: ",Cao_1.idade)

print()
print("****|PRÓXIMO ANIMAL|****")
print()

Cao_2 = Animal("Dalmata", "Grande", "1")
print("Raça: ",Cao_2.raca)
print("Porte: ",Cao_2.porte)
print("Idade: ",Cao_2.idade)

print()
print("****|Aquilo Que Faz|****")
print()

Cao_2.latir()
print("Latiu: ",Cao_2.late)

Cao_2.parar_de_latir()
print("Parou: ",Cao_2.late)



