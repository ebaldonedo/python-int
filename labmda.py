my_list= [1,2,3,4,5]

squares = list(map(lambda x:x**2,my_list))

filtred= list(filter(lambda x:x>3,my_list))
print("Squares:  ")
print(squares)

print("Filtred:  ")

print(filtred)