# dunder or magic methods (Double Underscore)

# Methods that python already know about and when you use them you can map them into your own code.

from todo import Todo

k_todo = Todo(name='Kingsley')
e_todo = Todo(name= 'Emmanuel')


# print(k_todo)
# print(repr(k_todo))

# print(str(k_todo))
# print(str(e_todo))

# print(k_todo)
# print(e_todo)

k_todo.add('buy milk')
k_todo.add('Code Python')
k_todo.add('Cook Dinner')


# print(len(k_todo))
# print(len(e_todo))

print(k_todo > e_todo)
print(k_todo < e_todo)










# ==============================
# ==============================
# ==============================


# The below will print things you can use with the list
# x = [1,2,3,4]
# print(dir(x))

# Another way to run it with the same output
# print(x.__dir__())

# To get the length of the list
# print(x.__len__())
# print(len(x))

# print(2+2)
# print(int.__add__(2,2))
# print('c'+'r')
# print(str.__add__('c', 'r'))

# ==============================
# ==============================
# ==============================



















