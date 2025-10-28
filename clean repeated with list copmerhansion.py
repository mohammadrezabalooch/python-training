my_list = ["a", "a", "b", "a", "b", "c", "c", "a", "e", "f", "z", "e", "d", "d"]
print(my_list, len(my_list))

filtred_list = []

filtred_list = [x for x in my_list if not (x in filtred_list or filtred_list.append(x))]
print(filtred_list, len(filtred_list))