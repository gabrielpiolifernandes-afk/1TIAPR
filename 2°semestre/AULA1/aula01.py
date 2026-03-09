class Animal:
    def __init__(self, animal, raça, idade):
        self.animal = animal
        self.raça = raça
        self.idade = idade
   
    def display_info(self):
        return f"animal: {self.animal}, raça: {self.raça}, idade: {self.idade}"
 
class Gato(Animal):
    def __init__(self, animal, raça, idade, cor_do_pelo):
        super().__init__(animal, raça, idade,)
        self.cor_do_pelo = cor_do_pelo
   
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, cor_do_pelo: {self.cor_do_pelo}"
   
class Cachorro(Animal):
    def __init__(self, animal, raça, idade, pedigree):
        super().__init__(animal, raça, idade,)
        self.pedigree = pedigree
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, pedigree: {self.pedigree}"
 
class passaro(Animal):
    def __init__(self, animal, raça, idade, tipos_de_ninho):
        super().__init__(animal, raça, idade,)
        self.tipos_de_ninho = tipos_de_ninho
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, tipos_de_ninho: {self.tipos_de_ninho}"