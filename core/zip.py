'''
    Zip
        - expects any  no. of iterators with equal indeces
            to combine it into a single object.

            * Note *    if iterators contains unequal length,
                        iteration stops at the smallest index
'''

names = ["rodel", "ryan"]
grades = [1, 2]

# combine
result = zip(names, grades)
list_result = list(result)
print(list_result) # [('rodel', 1), ('ryan', 2)]

# unzip
names, grades = zip(*list_result)
print(names, grades) # ('rodel', 'ryan') (1, 2)


