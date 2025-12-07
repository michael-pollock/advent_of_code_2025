def get_input(file_path: str) -> list[str]:
     with open(file_path, 'r') as input_file:
          return input_file.readlines()
     
def get_csv_input(file_path: str) -> list[str]:
     import csv
     with open(file_path, 'r') as csv_file:
          contents: list[list[str]] = list(csv.reader(csv_file))
     single_list_contents = []
     for row in contents:
          single_list_contents.extend(row)
     return single_list_contents