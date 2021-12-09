def list_comprehension_exercise_1():
    return [i for i in range(0, 11)]

def list_comprehension_exercise_2():
    return [i for i in range(0, 22)  if i % 2 == 0 or i % 3 == 0]
    
def list_comprehension_exercise_3():
   return [i for i in range(-4,32) if i % 2 != 0 and i % 5 != 0]

def list_comprehension_exercise_4():
    return [i * i for i in range(11)]

def list_comprehension_exercise_5(sentence):
    return [i for i in list(sentence) if i.isupper()]

def list_comprehension_exercise_6(sentence):
    return [i for i in sentence.split(' ') if i[0].lower() == "r" and len(i) > 3]