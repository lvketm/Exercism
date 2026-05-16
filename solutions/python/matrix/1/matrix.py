class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def create_rows(self):
       # create new matrix
       new_matrix = []
       rows = self.matrix_string.split("\n")

       for row in rows:
           number_row = []

           for number in row.split():
               number_row.append(int(number))

           new_matrix.append(number_row)

        # return row
       return new_matrix

    def row(self, index):
        return self.create_rows()[index - 1]

    def column(self, index):
        columns = []

        for i in range(len(self.create_rows())):
            columns.append(int(self.create_rows()[i][index - 1]))

        return columns 
