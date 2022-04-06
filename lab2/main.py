import pandas as pd
from requestsData import request_students_in_data_frame
from requestsData import request_students

def search_the_best_course_by_gpa():
  course_average = request_students()
  print(course_average)
  sorted_course_average = sorted(course_average, key=lambda item: item[list(item.keys())[0]], reverse=True)

  print('\nThe best course  by medium score:')
  print(sorted_course_average[0])

search_the_best_course_by_gpa()

### <---

student_data_frame = request_students_in_data_frame()

### <---

def save_to_csv(data: pd.DataFrame):
  data.to_csv('data.csv')

### <---

def search_mid_value(data: pd.DataFrame):
  print("Enter the grade mid")
  value_for_search = float(input())
  student_id = data["gradeMid"].sub(value_for_search).abs().idxmin()
  print(data.iloc[[student_id]])

### <---

save_to_csv(student_data_frame)
search_mid_value(student_data_frame)