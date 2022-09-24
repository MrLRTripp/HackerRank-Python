# An interesting example of the flexibility / features of namedtuples

from collections import namedtuple

def avg_grade (student_list):
    """
    Columns of student info can be entered in any order.
    We populate the student_info namedtuple using positional arguments that match the arbitrary order of the column headers.
    We then extract the student MARK values based on the MARK field name.
    """
    total_grades = sum([int(s.MARK) for s in student_list])

    return round(total_grades/len(student_list), 2)


if __name__ == '__main__':
    num_students = int(input('Enter Number of Students: '))
    col_header_list = input ('Enter Column Headers ID, MARK, NAME, CLASS in any order: ').split()
    student_info = namedtuple('Student',col_header_list)
    student_list = []

    for _ in range(0,num_students):
        student_list.append(student_info(*(input('Enter Student Info: ').split())))

    print(f'Average grade for all students: {avg_grade(student_list)}')