# class Test:
#     # double underline
#     def __init__(self, name):
#         self.name = name
#
#     # def __str__(self):
#     #     return self.name
#
# test_obj = Test("Test")
#
# print(test_obj)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x
    def __gt__(self, other):
        return self.y > other.x

obj_1 = Vector(1, 2)
obj_2 = Vector(3, 4)
obj_3 = Vector(3,4)

print(obj_3 > obj_2)

23

