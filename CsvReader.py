import csv


class CsvReader:
    data = []
    date = []

    def get_data(self):
        with open('DIS.csv', 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self.data.append(float(row[3]))
        return self.data

    def get_date(self):
        with open('DIS.csv' , 'r') as file :
            reader = csv.reader(file , delimiter=',')
            i = 0
            for row in reader:
                self.date.append(i)
                i += 1
        return self.date
