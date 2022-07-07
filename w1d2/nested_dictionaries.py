x = [[5, 2, 3], [10, 8, 9]]

x[1][0] = 15
print(x[0])


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'andres'
print(sports_directory)

z = [{'x': 10, 'y': 20}]

z[0]['y'] = 30
print(z)


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):

    for list in range(len(students)):
        names = ""
        # print(list)
        for x, y in students[list].items():
            names += f"{x}+{y}"
        print(names)


iterateDictionary(students)


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key_name, some_list):
    for list in range(len(some_list)):
        for x, y in some_list[list].items():
            if key_name == x:
                print(y)


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for value in some_dict[key]:
            print(value)


printInfo(dojo)


# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
