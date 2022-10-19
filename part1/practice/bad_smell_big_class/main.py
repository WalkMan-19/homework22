# в задании представлен один класс который нужно разбить на 4
# Воин      - Warrior
# Лекарь    - Healer
# Дерево    - Tree
# Ловушка   - Trap

# Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю
# Лекарь может защищаться, лечить воина и панически спасаться бегством
# Дерево может защищаться (попробуй разруби сходу) и гореть в огне
# Ловушка не может ничего кроме как атаковать того, кто на нее наступит
# Для решения этой задачи не используйте наследование

#class Obj:
    ##
    # тут представлено поведение четырех различных игровых объектов:
    # - воина
    # - лекаря
    # - дерева
    # - ловушки


class Warrior:
    def attack(self):
        print('воин атакует')

    def defense(self):
        print('воин защищается')

    def move(self):
        print('воин передвигается')


class Healer:
    def healer_defense(self):
        print('лекарь защищается')

    def healer_move(self):
        print('лекарь движется')

    def heal(self):
        print('лекарь лечит')


class Tree:
    def tree_defense(self):
        print('дерево защищается')

    def on_fire(self):
        print('дерево горит')


class Trap:
    def trap_attack(self):
        print("It's a trap!")


if __name__ == '__main__':
    unit = Warrior()
    unit.move()
    unit.attack()

    healer = Healer()
    healer.healer_defense()
    healer.heal()

    tree = Tree()
    tree.on_fire()

    trap = Trap()
    trap.trap_attack()
