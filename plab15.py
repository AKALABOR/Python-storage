class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def info(self):
        print(f"Ім'я: {self.name}, Рівень: {self.level}, Здоров'я: {self.health}, Атака: {self.attack}")

    def attack_enemy(self, enemy):
        if enemy.health <= 0:
            print(f"{enemy.name} вже переможений!")
            return
        damage = self.attack
        enemy.health -= damage
        print(f"{self.name} атакує {enemy.name} на {damage} шкоди.")
        if enemy.health <= 0:
            enemy.health = 0
            print(f"{enemy.name} переможений!")
        else:
            print(f"{enemy.name} має {enemy.health} здоров'я.")

class Warrior(Character):
    def __init__(self, name, level, health, attack, armor):
        super().__init__(name, level, health, attack)
        self.armor = armor

    def heal(self):
        self.health += 30
        print(f"{self.name} відновив здоров'я до {self.health} (воїн).")

class Mage(Character):
    def __init__(self, name, level, health, attack, mana):
        super().__init__(name, level, health, attack)
        self.mana = mana

    def heal(self):
        if self.mana >= 10:
            self.health += 40
            self.mana -= 10
            print(f"{self.name} відновив здоров'я до {self.health} (магія).")
        else:
            print(f"{self.name} не має достатньо мани для відновлення.")

class Archer(Character):
    def __init__(self, name, level, health, attack, arrows):
        super().__init__(name, level, health, attack)
        self.arrows = arrows

    def heal(self):
        self.health += 20
        print(f"{self.name} відновив здоров'я до {self.health} (лучник).")

hero1 = Character("Герой1", 5, 100, 20)
hero2 = Character("Герой2", 4, 80, 15)
hero1.info()
hero2.info()
hero1.attack_enemy(hero2)
hero2.attack_enemy(hero1)
hero1.attack_enemy(hero2)

w = Warrior("Тан", 6, 120, 25, armor=50)
m = Mage("Фаєр", 5, 90, 30, mana=20)
a = Archer("Лук", 4, 85, 22, arrows=10)
w.info()
m.info()
a.info()
m.attack_enemy(w)
w.heal()
a.heal()
