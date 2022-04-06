import requests
import pandas as pd
from Student import Student


urls = ['https://www.hse.ru/n/student-ratings/api?unit=122392301&course=1&from=576252978', 'https://www.hse.ru/n/student-ratings/api?unit=122392301&course=2&from=576252978', 'https://www.hse.ru/n/student-ratings/api?unit=122392301&course=3&from=576252978', 'https://www.hse.ru/n/student-ratings/api?unit=122392301&course=4&from=576252978']


def request_students():
  sum_of_gpa_each_course = []
  for url in urls:
    students_data = requests.get(url).json()
    parsed_students_data = students_data["data"]
    student_list = [Student(**s) for s in parsed_students_data]
    #мог написать код ниже в одну строчку, но сильно ухудшалась читабельность
    total_gpa = round(sum(list(map(lambda item: item.gpa, student_list))), 2)
    sum_of_gpa_each_course.append(total_gpa)

  
  sum_of_gpa_for_each_course = [{x + 1: y} for x, y in enumerate(sum_of_gpa_each_course)]
  return sum_of_gpa_for_each_course

#### <----

def request_students_in_data_frame():
  dataframe = []
  for url in urls:
    students_data = requests.get(url).json()
    parsed_students_data = students_data["data"]
    student_list = [Student(**s) for s in parsed_students_data]
    dataframe.append(pd.DataFrame(data=student_list))

  student_data_frame = pd.concat(dataframe, ignore_index=True)
  return student_data_frame
