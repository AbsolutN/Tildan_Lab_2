# Här ska lab 1 skrivas

class Pokemon:

    def __init__(self, row):
        divided_row = row.split(",")
        self.number = divided_row[0]
        self.name = divided_row[1]
        self.type1 = divided_row[2]
        self.type2 = divided_row[3]
        self.total = divided_row[4]
        self.hp = divided_row[5]
        self.attack = divided_row[6]
        self.defense = divided_row[7]
        self.sp_atk = divided_row[8]
        self.sp_def = divided_row[9]
        self.speed = divided_row[10]
        self.generation = divided_row[11]
        self.legendary = divided_row[12]


    def __str__(self):
        return self.name + " " + self.type1 + " HP: " + self.hp


    def __lt__(self, other):
        if self.number > other.number:
            return True
        else:
            return False


    def __add__(self, other):
        total_hp = int(self.hp) + int(other.hp)
        return "This is the summed HP: " + str(total_hp)


    def change_hp(self,new_hp):
        self.hp = new_hp



def testing_my_class_methods():
    pokedex1 = Pokemon("1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False")
    pokedex2 = Pokemon("56,Mankey,Fighting,,305,40,80,35,35,45,70,1,False")
    print(pokedex1)
    print(pokedex2)
    print(pokedex2 < pokedex1)

    Pokemon.change_hp(pokedex2,"100")
    print(pokedex2)
    print(pokedex2 + pokedex1)

#testing_my_class_methods()

pokedex = []

def main():

    with open("pokemon.csv") as file:
        headline = file.readline()
        row = file.readline()
        while row:
            Pokemon(row)
            pokedex.append(row.strip())
            row = file.readline()
    return pokedex

main()

print(pokedex)

def search():
    your_choice = input("Choose a pokemon: ")
    for i in pokedex:
        i = i.split(",")
        if your_choice in i:
            i.pop(0)
            i.pop(0)
            print(i)



search()






