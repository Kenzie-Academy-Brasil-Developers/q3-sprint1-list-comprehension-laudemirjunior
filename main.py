def list_comprehension_exercise_1():
    list =  []
    for i in range(11):
        list.append(i)
    return list

def list_comprehension_exercise_2():
    list =  []
    for i in range(22):
        if i % 2 == 0 or i % 3 == 0:
            list.append(i)
    return list

def list_comprehension_exercise_3():
    list = []
    for i in range(-4,32):
        print(i)
        if(i % 2 != 0 and i % 5 != 0):
            list.append(i)
    return list

def list_comprehension_exercise_4():
    list = []
    for i in range(11):
        list.append(i * i)
    return list

def list_comprehension_exercise_5(sentence):
    sentence = list(sentence)
    new_list = []
    for i in sentence:
        if(i.isupper()):
            new_list.append(i)
    return new_list

def list_comprehension_exercise_6(sentence):
    sentence = sentence.split(' ')
    list = []
    for i in sentence:
        if i[0].lower() == "r" and len(i) > 3:
            list.append(i)
    return list

result = list_comprehension_exercise_3()
print(result)