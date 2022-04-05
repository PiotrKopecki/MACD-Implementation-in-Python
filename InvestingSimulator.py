
class InvestingSimulator:
    percent_of_capital_to_invest = 0.0
    starting_capital = 0.0
    current_capital = 0.0
    how_much_stock_owned = 0.0

    def __init__(self, p, s):
        self.percent_of_capital_to_invest = p/100
        self.starting_capital = s
        self.current_capital = s

    def buy(self, prize):
        money_in = self.current_capital * self.percent_of_capital_to_invest
        stock_for_money_in = money_in / prize
        self.current_capital -= money_in
        self.how_much_stock_owned += stock_for_money_in

    def sell(self, prize):
        self.current_capital += prize * self.how_much_stock_owned
        self.how_much_stock_owned = 0.0

    def invest(self, buy_or_sell, data):
        for i in range(1, len(buy_or_sell)):
            if(buy_or_sell[i] == "B"):
                self.buy(data[i])
            elif(buy_or_sell[i] == "S"):
                self.sell(data[i])
        if(self.how_much_stock_owned > 0.0):
            self.sell(data[len(data) - 1])

    def get_current_capital(self):
        return round(self.current_capital, 2)
