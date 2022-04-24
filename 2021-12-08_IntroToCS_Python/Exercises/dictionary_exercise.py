"""
Set of dictionary traversal exercises created for the final exam review for the introduction to computer science course.
@author Vincent Zhang
@since 8 December 2021
"""

print("****************** EXERCISE 1 ***************************************************")
# Dict[str, str]
d = {
    'a': 'aa',
    'b': 'bb'
}
## Code Start ######################################
for v in d.values():
    print(v)
## Code End ##
# Expected Output
"""
aa
bb

"""
## Remark
"""
>>> d.values()
dict_values(['aa', 'bb'])

>>> d.values() == ['aa', 'bb']
False

Why? d.values() returns 'dict_values object' not 'list object'

>>> list(d.values()) == ['aa', 'bb']
True

>>> [d.values()] == ['aa', 'bb']
False

Why?

>>> [d.values()]
[dict_values(['aa', 'bb'])]
"""
## Summary
"""
1. dictionary.values() return dict_values([dictionary elements])
2. dictionary.keys() return dict_keys([dictionary dictionary elements])
3. dictionary.items() return dict_items([(key, value), (key, value), ..., (key, value)])
4. dict_values object not list object, dict_keys another type of object
5. list(dict_values([2, 3, 4])) changes dict_values object to list object
6. [dict_values([2, 3, 4])] wraps dict_values object in a list object
7. dictionary keys must be 'immutable', (no modify), so keys cannot be list
"""


print("****************** EXERCISE 2 ***************************************************")
# Dict[str, List[str]]
d = {
    'a': ['aa', 'bb'],
    'b': ['bb', 'cc']
}
## Code Start ######################################
for v in d.values():
    for e in v:
        print(e)
## Code End ##
# Expected Output
"""
aa
bb
bb
cc

"""
# Explanation
"""
>>> d.values()
dict_values([['aa', 'bb'], ['bb', 'cc']])

Layer 1 values:
['aa', 'bb']
['bb', 'cc']

outer loop iterates over value lists
inner loop iterates within each value list
"""


print("****************** EXERCISE 3 ***************************************************")
# Dict[str, Dict[str, List[str]]]
NAMES = 'NAMES'
d = {
    'a': {
        "LABEL1": 'abc',
        "LABEL2": 'abcd',
        "NAMES": ['jia', 'yi']
    },
    'b': {
        "LABEL1": 'ac',
        "LABEL2": 'ad',
        "NAMES": ['bing', 'yi']
    }
}
## Code Start ######################################
for v in d.values():
    for vv in v[NAMES]:
        print(vv)
## Code End ##
# Expected Output
"""
jia
yi
bing
yi
"""

# Explanation
"""
Difference between Exercise 3 and 2, middle layer of keys
so sub_dict[NAMES] is needed
"""


# Looping notes
"""
Use loops to iterate over the values to be searched for

1 layer: Dict[immutable object, object]
3 ways:

1. iterate over dictionary keys
for k in dictionary:
for k in dictionary.keys():

2. iterate over dictionary values
for v in dictionary.values():

3. iterate over dictionary key and values (out of scope)
for k, v in dictionary.items():


2 layers: Dict[immutable object, list[object]]
1 layer's 3 ways all apply
need to iterate within layer only if we want to find the elements in the list

for ... iterate values: every value is a list
    for item in list:


2 layer: Dict[immutable object, Dict[immutable object, object] ]
for iterate values: every value is a dictionary:
    use one layer method on the sub-dictionary, can ignore outer layer dictionary

e.g.,
for sub_dict in dict.values():
    for v in sub_dict.values():
    ...

if we only want one type of key, e.g., KEYY
for sub_dict in dict.values():
   v = sub_dict[KEYY]:

"""




print("\n############################## SUPPLEMENTARY EXERCISE ###################")
# Notice
"""
(2,) is a single element tuple
[2] is a single element list
(None,) single element tuple

(2, 3) is 2 element tuple
"""
# Supplementary Exercise
d = {
   ('a', 'b'): {None: [(-1, -2), ('2', '-2'), ('3', '5', {(2,): [(2, 3), (5,), (None,)], None: [(2,), (None,)]})]}
}
# Print
"""
2
3
5
None
2
None
"""

# Structure
"""
d =
{
    Key:   ('a', 'b'):
    Value:
    {
        Key:    None:
        Value:
        [
            List element 1: (-1, -2),
            List element 2: ('2', '-2'),
            List element 3:
            (
                Tuple element 1: '3',
                Tuple element 2: '5',
                Tuple element 3:
                {
                    dictionary key/value pair:    (2,): [(2, 3), (5,), (None,)],
                    dictionary key/value pair:    None: [(2,), (None,)]
                }
            )
        ]
    }
}

Print tuple elements at layer 8
"""

for v in d.values():
    for vv in v.values():
        for tup in vv:
            if len(tup) == 3: # tuple has 3 elements, this is hard coded to work only for this example, the purpose of this exercise is to become comfortable with traversing any level of nests
                for element in tup:
                    if type(element) == dict: # again, hard coded, this will only work for this specific example
                        for vvv in element.values():
                            for tupp in vvv:
                                for t in tupp:
                                    print(t)
