
class Csv_Parser:

    def __init__(self, file_name=None, columns=0, rows=0,
                 header=None, read_flag=False):

        num_rows = 0
        if read_flag:
            with open(file_name, 'r') as f:
                for line in f:
                    if num_rows == 0:
                        header = line.split(',')

                    num_rows += 1

            f.close()

        self.filename = file_name
        self.header   = list(header)
        self.columns  = len(header)
        self.rows     = num_rows


    def get_header(self):
        return self.header

    def num_of_columns(self):
        return self.columns

    def num_of_rows(self):
       return self.rows


    def download_csv(self, url_path=None, path_to_store=None):

        try:
            print("Raw file downloading . . . ")
            wget.download(url_path, path_to_store)
            print("file downloaded successfully")
            return True
        except Exception as e:
            print(e)
            return False


    def split_csv(filehandler, delimiter=',', row_limit=10000,
              output_name_template='output_%s.csv', output_path='.', keep_headers=True):

        reader = csv.reader(filehandler, delimiter=delimiter)
        current_piece = 1
        current_out_path = os.path.join(
            output_path,
            output_name_template % current_piece
        )
        current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
        current_limit = row_limit
        if keep_headers:
            headers = next(reader)
            current_out_writer.writerow(headers)
        for i, row in enumerate(reader):
            if i + 1 > current_limit:
                current_piece += 1
                current_limit = row_limit * current_piece
                current_out_path = os.path.join(
                    output_path,
                    output_name_template % current_piece
                )
                current_out_writer = csv.writer(open(current_out_path, 'w', encoding='utf-8'), delimiter=delimiter)
                if keep_headers:
                    current_out_writer.writerow(headers)
            current_out_writer.writerow(row)


