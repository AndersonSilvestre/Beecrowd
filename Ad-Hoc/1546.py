'''2 - Dias
    4 - Feedback por dia
        1 -\
        1 - \Feedbacks do dia
        3 - /
        4 -/
    3
        3 -\
        3 - - Feedback do dia
        2 -/

    1 - Rolien
    2 - Naej
    3 - Elehcim
    4 - Odranoel

'''

dias = int(input())

while dias > 0 :
    feedback = int(input())
    while feedback > 0:
        at = int(input())
        if at == 1:
            print("Rolien")
        elif at == 2:
            print("Naej")
        elif at == 3:
            print("Elehcim")
        else:
            print("Odranoel")
        feedback -= 1
    dias -= 1
