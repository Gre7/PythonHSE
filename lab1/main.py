from Student import Student

student1 = Student('Vasya', 'Trofimov', '2001', 2, 'VPI-20', [8, 6, 9, 4, 10])
student2 = Student('Danil', 'Vasilev', '1999', 3, 'VPI-19', [5, 10, 5, 8, 7])
student3 = Student('Stepan', 'Tyagin', '1996', 3, 'VPI-19', [8, 7, 9, 9, 4])
student4 = Student('Egor', 'Lazarev', '2000', 2, 'VPI-20', [10, 10, 7, 8, 8])
student5 = Student('Alexandr', 'Osipov', '2001', 3, 'VPI-20', [5, 8, 6, 10, 8])

student_list = [student1, student2, student3, student4, student5]

#### <--

def sort_by_course_name(list):
  if len(list) < 2: 
    print(list)
    return list
  list_sorted_by_course = sorted(list, key=lambda item: (item.course, item.name))
  for student in list_sorted_by_course:
    print(student.name)

print('Student list sorted by course and name:')
sort_by_course_name(student_list)

#### <--

def sort_by_age(list_of_students): 
  if len(list_of_students) == 0: 
    return

  if len(list_of_students) == 1:
    print(list_of_students[0].name)
  
  list_sorted_by_course = sorted(list_of_students, key=lambda item: item.year_of_birth, reverse=True)

  junior_student = list_sorted_by_course[0].name
  print('Junior student: ' + junior_student)

  senior_student = list_sorted_by_course[-1].name
  print('Senior student: ' + senior_student)


print('\nSearch for junior and senior students:')
sort_by_age(student_list)

#### <--

def search_average_score_by_matrix(matrix):
  res = [sum(x) / len(matrix) for x in zip(*matrix)]
  print(res)


#### <--

def sort_by_students_group(students):
    groups_of_students = dict.fromkeys(set([stud.group_number for stud in students]))

    
    for student in students: 
      group = student.group_number
      if (groups_of_students[group] == None): 
        groups_of_students[group] = [student]
      else: 
        groups_of_students[group].append(student)

    return groups_of_students

#### <--

def search_gpa_by_students_group():
  groups_of_students = sort_by_students_group(student_list)
  for group, value in groups_of_students.items():
      matrix_of_grades = [stud.subject_grades for stud in value]
      print('\nGPA for ' + group + ' group')
      search_average_score_by_matrix(matrix_of_grades)

search_gpa_by_students_group()

#### <--

def search_best_student():
  groups_of_students = sort_by_students_group(student_list)

  for group, value in groups_of_students.items():
    total = [{stud.name: sum(stud.subject_grades)} for stud in value]
    
    sorted_total = sorted(total, key=lambda item: item[item.keys()[0]], reverse=True)
    
    groups_of_students.update({group: sorted_total[0]})

  print('\nThe Best student in groups:')
  print(groups_of_students)
  

search_best_student()