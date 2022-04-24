"""
Holistic cGPA calculator program to demonstrate the integration of major topics in the introduction to computer science course.
Code presented in the final exam review on December 8, 2021.
@author Vincent Zhang
@since 8 December 2021
"""

END = 'END'
COURSE = 'Course'
SPACE = ' '
COL_GRADE = 0
COL_WEIGHT = 1

def read_data(file):
    file = open(file)
    data = {}
    block = False
    course_key = ''

    line = file.readline()
    while line != '':
        line = line[:-1]
        if line[:2] not in ['$$', '']:
            course = line.split(':')
            if len(course) > 0 and course[0] == COURSE:
                block = True
                course_key = course[1]
                if course_key not in data:
                    data[course_key] = []
            elif line == END:
                block = False
            elif block:
                data[course_key].append(tuple(line.split(SPACE)))
        line = file.readline()

    file.close()
    return data

def scale_gpa(grade):
    if grade >= 85:
        return 4.0
    if grade >= 80:
        return 3.7
    if grade >= 77:
        return 3.3
    if grade >= 73:
        return 3.0
    if grade >= 70:
        return 2.7
    if grade >= 67:
        return 2.3
    if grade >= 63:
        return 2.0
    if grade >= 60:
        return 1.7
    if grade >= 57:
        return 1.3
    if grade >= 53:
        return 1.0
    if grade >= 50:
        return 0.7
    return 0.0


def calculate_max_percentage(data):
    obtained = 0
    subtotal = 0
    for d in data:
        obtained += float(d[COL_GRADE]) * float(d[COL_WEIGHT]) / 100
        subtotal += float(d[COL_WEIGHT]) # sum of weights
    lost = subtotal - obtained
    undetermined = 100 - subtotal
    max_final = 100 - lost

    # print(f"Obtained: \t{obtained:.3f}%")
    # print(f"Lost: \t\t{lost:.3f}%")
    # print(f"Undetermined: \t{undetermined:.3f}%")
    # print(f"Max Final: \t{max_final:.3f}%")

    return max_final
    

def calculate_gpa(data):
    gpa_by_course = {}

    for k, v in data.items():
        gpa_by_course[k] = scale_gpa(calculate_max_percentage(v))

    return gpa_by_course

def get_cGPA(gpa_by_course):
    sum = 0
    for k, v in gpa_by_course.items():
        sum += v
    return sum / len(gpa_by_course)

def invert_dictionary(data):
    inverted = {}
    for k, v in data.items():
        if v not in inverted:
            inverted[v] = []
        inverted[v].append(k)
    return inverted

def flatten_inverted_dictionary(data):
    inverted = invert_dictionary(data)
    flattened = []
    for k, v in inverted.items():
        flattened.append((k, *v))
    return flattened

from sorting_algorithms import insertion_sort
def get_max_gpa_course_by_insertion_sort(course_by_gpa):
    insertion_sort(course_by_gpa)
    return course_by_gpa[-1]

from binary_search import bin_search
def contains_gpa_course_by_binary_search(gpa_by_course, gpa):
    keys = list(invert_dictionary(gpa_by_course).keys())
    insertion_sort(keys)
    return bin_search(keys, gpa) is not None


if __name__ == '__main__':
    data = read_data('Input.txt')
    # {course: [(grade, weight, description), (grade, weight, description)]}

    gpa_by_course = calculate_gpa(data)
    # {course: gpa}
    print("cGPA is", get_cGPA(gpa_by_course))

    course_by_gpa = flatten_inverted_dictionary(gpa_by_course)
    gpa_exists = 3.7
    gpa_does_not_exist = 3.5
    print("highest GPA course is", get_max_gpa_course_by_insertion_sort(course_by_gpa))
    print(f"GPA {gpa_exists} course exists is", contains_gpa_course_by_binary_search(gpa_by_course, gpa_exists))
    print(f"GPA {gpa_does_not_exist} course exists is", contains_gpa_course_by_binary_search(gpa_by_course, gpa_does_not_exist))
