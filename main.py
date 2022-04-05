from Macd import Macd
from CsvReader import CsvReader
from Graph import Graph
from InvestingSimulator import InvestingSimulator



csv = CsvReader()
data = csv.get_data()
date = csv.get_date()

starting_money = 1000 * data[0]
percent_of_current_money_invested = 5.0

m = Macd()
m.calc_macd(data)
m.calc_signal()
m.calc_buy_or_sell()
macd = m.get_macd()
signal = m.get_signal()
buy_or_sell = m.get_buy_or_sell()

print("Starting money equals 1000 * starting action prize")
print("Starting money: " + str(starting_money))
i = InvestingSimulator(percent_of_current_money_invested, starting_money)
i.invest(buy_or_sell, data)
print("Money after investing: " + str(i.get_current_capital()))
percent = round(i.get_current_capital()/starting_money * 100, 2)
print("Capital after investing is worth " + str(percent) + " % of starting capital")

g = Graph()
g.draw_exchange_macd_signal(date, data, macd, signal, buy_or_sell, True)







