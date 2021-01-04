def list_sum(the_list):
    somma=0
    for item in the_list:
        somma= somma+item
    print("La somma e` {}".format(somma))

list_sum([1,4,5])