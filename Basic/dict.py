# Function

first_arg = 10
second_arg = 20


def sum_fun(first_arg,second_arg) :
    first_arg = first_arg + 10
    first_arg = first_arg + 10
    second_arg = second_arg +10
    c = first_arg + second_arg
    return c

def my_fn ():
 pass

result_sum = sum_fun(first_arg,second_arg)

print(type(sum_fun) )

print(result_sum)

print (my_fn())

# Change parameters

person = {
    'name': 'Valentin',
    'age': 20
}


def increaase_person_age(person):
    person['age'] =+1
    return person

print(increaase_person_age(person))



print(person['age'])


