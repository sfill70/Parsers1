# def check_is_admin(username):
#     if username!='admin':
#         raise Exception('not allow')
#

#


# def check_is_admin(f):
#     def wrapper(*args, **kwargs):
#         if args[1]!='admin':
#             raise Exception('not allowed')
#         return f(*args, **kwargs)
#     return wrapper
#
#
# class Store(object):
#     name=''
#     @check_is_admin
#     def get_food(self, username, food):
#         return food
#     @check_is_admin
#     def put_food(self,username, food):
#         self.name=food
#
# storage=Store()
# storage.get_food('admin', 'pretty')
#
# def my_shiny_new_decorator(function_to_decorate):
#      # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
#      # получая возможность исполнять произвольный код до и после неё.
#      def the_wrapper_around_the_original_function():
#          print("Я - код, который отработает до вызова функции")
#          function_to_decorate() # Сама функция
#          print("А я - код, срабатывающий после")
#      # Вернём эту функцию
#      return the_wrapper_around_the_original_function
#
#  # Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
# def stand_alone_function():
#      print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
#
# stand_alone_function()
# #Я простая одинокая функция, ты ведь не посмеешь меня изменят
#  # Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
#  # который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
#  # готовую к использованию функцию:
# stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function_decorated()

#
# # -*- coding: utf-8 -*-
# def another_function(func):
#     """
#     Функция которая принимает другую функцию.
#     """
#
#     def other_func():
#         val = "Результат от %s это %s" % (func(),
#                                           eval(func())
#                                           )
#         return val
#
#     return other_func
#
#
# @another_function
# def a_function():
#     """Обычная функция"""
#     return "1+1"

#
#
# value = a_function()
# print(value)

class Pizza(object):
    size=0
    @staticmethod
    def mix_ingredients(x,y):
        return x+y

    chesse='cheese'
    vegetable='vegetable'
    def cook(self):
        return self.mix_ingredients(self.chesse, self.vegetable)
    radius=42
    @classmethod
    def get_radius(cls):
        return cls.radius

print(Pizza.cook)
print(Pizza.get_radius())
print(Pizza.mix_ingredients(45,56))

print(Pizza().cook is Pizza().cook)
print(Pizza().mix_ingredients is Pizza().mix_ingredients)
print('...')