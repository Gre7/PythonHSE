import requests
import pandas as pd
from Student import Student


urls = ['https://www.hse.ru/n/student-ratings/api?unit=122392301&course=1&from=576252978', 'https://www.hse.ru/n/student-ratings/api?unit=122392301&course=2&from=576252978', 'https://www.hse.ru/n/student-ratings/api?unit=122392301&course=3&from=576252978', 'https://www.hse.ru/n/student-ratings/api?unit=122392301&course=4&from=576252978']

def request_students_data():
  dataframe = []
  for url in urls:
    students_data = requests.get(url).json()
    parsed_students_data = students_data["data"]
    student_list = [Student(**s) for s in parsed_students_data]
    dataframe.append(pd.DataFrame(data=student_list))

  student_data_frame = pd.concat(dataframe, ignore_index=True)
  
  return student_data_frame

