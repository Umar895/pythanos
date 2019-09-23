
from header import Csv_Parser


file_n = 'chaos.csv'
Csv_Parser = Csv_Parser(file_name=file_n,read_flag=False)


print(Csv_Parser.num_of_rows())
