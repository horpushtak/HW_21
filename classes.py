from abc import abstractmethod, ABC

'''Абстрактный класс в пайтон это скорее подсказка другим разработчикам, как выглядит функционал,
в отличие от других языков, где без абстрактного класса можно и не унаследоваться
Каркас для базового, от которого уже другие классы наследуются'''

class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        self.__items = items  # Приватные поля, чтобы ...
        self.__capacity = capacity

    def add(self, name, count):
        if name in self.__items.keys():
            if self.get_free_space() >= count:
                self.__items[name] += count  # Просто добвить количество
            else:
                return "Недостаточно места на складе"
        else:
            if self.get_free_space() >= count:
                self.__items[name] = count  # Сделать в словаре новую запись name = count
            else:
                return "Недостаточно места на складе"

    def remove(self, name, count):
        if self.get_free_space() > count:
            self.__items[name] -= count
        else:
            return "Недостаточно товара на складе"

    def get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    def get_items(self):  # Странно, что здесь не попросили сделать property как геттер, мы берём поле класса,
        # обращаясь не к полю, а к методу. Свойством это сделать было бы разумно.
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items.keys())

    def __repr__(self):  # Репр лучше всегда прописывать, причём именно так, чтобы нормально показывал словарь
        st = ""
        for key, value in self.__items.items():
            st += f'{key}: {value}\n'  # С переносом, чтобы в столбик
        return st


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)  # Пропихиваем 20, что в Shop по умолчанию, super().__init__ - это ...

    def add(self, name, count):
        if self.get_unique_items_count() >= 5:
            return "Слишком много уникальных товаров"
        else:
            super().add(self, name, count)

        """
        Доставить {3} {печеньки} из {склад} в {магазин}. Три действия: 
        Доставить (перемещение)
        Забрать (удаление)
        Привезти (добавление)
        """
class Request:
    def __init__(self, request_str):
        req_list = request_str.split()
        action = req_list[0]
        self.__count = int(req_list[1])
        self.__item = req_list[2]
        if action == 'Доставить':
            self.__from = req_list[4]
            self.__to = req_list[6]
        if action == 'Забрать':
            self.__from = req_list[4]
            self.__to = None
        if action == 'Привезти':
            self.__to = req_list[6]
            self.__from = None

    def move(self):
        if self.__to:
            eval(self.__to).add(self.__item, self.__count)
        if self.__from:
            eval(self.__from).remove(self.__item, self.__count)









        # storage_1 = Store(items={'Телефон': 10, 'Компьютер': 20}, capacity=50)  # Аргументы можно для наглядности прописать

# storage_1.add('Планшет', 5)
# storage_1.remove('Телефон', 2)
# print(storage_1.get_free_space())
# print(storage_1.get_items())
# print(storage_1.get_unique_items_count())
# print(storage_1)  # Тут репр выполняется