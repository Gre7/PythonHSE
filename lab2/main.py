import pandas as pd
from requestsData import request_students_data

student_data_frame = request_students_data()

def setup(data): 
  pd.set_option('display.max_columns', None)
  data.head()

def save_to_csv(data: pd.DataFrame):
  data.to_csv('data.csv')

def search_mid_value(data: pd.DataFrame):
  print("Введите среднее число")
  value_for_search = float(input())
  student_id = data["gradeMid"].sub(value_for_search).abs().idxmin()
  print(data.iloc[[student_id]])

setup(student_data_frame)
save_to_csv(student_data_frame)
search_mid_value(student_data_frame)