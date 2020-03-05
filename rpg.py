class Player:
    fire = 1
    ice = 2
    light = 3
    hp = 10

    def __init__(self,name,role):
        self.name = name
        self.role = role
        print("\nHello",self.name,"the",self.role)

    def fireball(self):
        self.fire -= 1

    def iceShard(self):
        self.ice -= 1

    def lightning(self):
        self.light -= 1

    def default(self):
        self.fire = 1
        self.ice = 2
        self.light = 3
        self.hp = 10

class Enemy:
    hp = 10
    def __init__(self,name,role):
        self.name = name
        self.role = role
        print("\nAn enemy has appeared")

def chooseName():
    name = input("Choose your name: ")
    while len(name) < 7 or len(name) > 15:
        print("Name must have 7 to 15 characters\n")
        name = input("Choose your name: ")
    return name

def chooseRole():
    print("\n1 - Warrior\n2 - Rogue\n3 - Mage\n")
    role = input("Choose your class: ")
    if role == "1" or role.lower() == "warrior":
        return "Warrior"
    elif role == "2" or role.lower() == "rogue":
        return "Rogue"
    elif role == "3" or role.lower() == "mage":
        return "Mage"

def life(player,enemy):
    print(f"\n{player.name}: {player.hp}")
    print(f"{enemy.name}: {enemy.hp}")

def spells(player):
    print(f"\n1 - Fireball: 5 damage ({player.fire} left)")
    print(f"2 - Ice Shard: 3 damage ({player.ice} left)")
    print(f"3 - Lightning: 2 damage ({player.light} left)\n")

def attack(player,enemy):
    choice = input("Choose a spell: ")
    if choice == "1" or choice.lower() == "fireball":
        if player.fire > 0:
            print("You selected Fireball")
            player.fireball()
            enemy.hp -= 5
        else:
            print("You have no Fireball left")

    elif choice == "2" or choice.lower() == "ice shard":
        if player.ice > 0:
            print("You selected Ice Shard")
            player.iceShard()
            enemy.hp -= 3
        else:
            print("You have no Ice Shard left")
            
    elif choice == "3" or choice.lower() == "lightning":
        if player.light > 0:
            print("You selected Lightning")
            player.lightning()
            enemy.hp -= 2
        else:
            print("You have no Lightning left")

    else:
        print("Invalid Choice")

def enemy(player,enemy):
    print("")
    print(enemy.name,"attacked!")
    
    if enemy.name == "Mork":
        player.hp -= 3


def main():
    name = chooseName()
    role = chooseRole()
    p1 = Player(name,role)
    e1 = Enemy("Mork","Elf")

    while p1.hp > 0 and e1.hp > 0:
        life(p1,e1)
        spells(p1)

        attack(p1,e1)
        if e1.hp <= 0:
            print("")
            print(e1.name,"the",e1.role,"died")
            break

        life(p1,e1)
        
        enemy(p1,e1)
        if p1.hp <= 0:
            print("")
            print(p1.name,"the",p1.role,"died")
        


main()
