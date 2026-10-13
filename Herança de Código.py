class Animal:
    def __init__(self, porte, idade):
        self.porte = porte
        self.idade = idade
        
class Cao(Animal):
    def __init__(self, porte, idade, raca):
      super().__init__(porte, idade)
      self.raca = raca
      
      
      
bobi=Cao("G",12,"bbb")

print(bobi.idade)











