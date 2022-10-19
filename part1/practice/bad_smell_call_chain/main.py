# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

# class Room:
#   def get_name(self):
#       return 42


# class Street:
#   def get_room(self) -> Room:
#       return Room()


# class City:
#   def get_street(self) -> Street:
#       return Street()

#   def population(self):
#       return 100500


# class Country:
#    def get_city(self) -> City:
#        return City()


# class Planet:
#   def get_contry(self) -> Country:
##       return Country()


class Person:
    def __init__(self, city_population, room_num):
        self._city_population = city_population
        self._room_num = room_num

    def get_person_room(self):
        return self._room_num

    def get_city_population(self):
        return self._city_population


# сделать экземпляр класса person и вызвать новые методы.


if __name__ == '__main__':
    person = Person(city_population=10000, room_num=47)
    print(person.get_city_population())
    print(person.get_person_room())
