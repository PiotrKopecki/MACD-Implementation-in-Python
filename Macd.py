
class Macd:
    macd = []
    signal = []
    buy_or_sell = []

    def get_reversed_data_from_to_from(self, data, n, date):
        temp = data[date - n : date + 1]
        temp.reverse()
        return temp

    def calc_ema(self, n, data, date):
        alfa = 2 / (n + 1)
        counter = 0.0
        denominator = 0.0
        d = self.get_reversed_data_from_to_from(data, n, date)
        for i in range(n + 1):
            if i == 0:
                counter += d[i]
                denominator += 1
            else:
                counter += ((1 - alfa) ** i) * d[i]
                denominator += (1 - alfa) ** i
        return counter / denominator

    def calc_macd(self, data):
        self.macd = []
        for i in range(len(data)):
            if i >= 26:
                ema_26 = self.calc_ema(26, data, i)
                ema_12 = self.calc_ema(12, data, i)
                self.macd.append(ema_12 - ema_26)
            else:
                self.macd.append(0.0)

    def calc_signal(self):
        self.signal = []
        for i in range(35, len(self.macd)):
            self.signal.append(self.calc_ema(9, self.macd, i))

    def calc_buy_or_sell(self):
        self.buy_or_sell = []
        tempM = self.get_macd()
        tempS = self.get_signal()
        for i in range(1, len(tempM)):
            if tempM[i] > tempS[i] and tempM[i-1] < tempS[i-1] and tempM[i] > 0:
                self.buy_or_sell.append("B")
            elif tempM[i] < tempS[i] and tempM[i-1] > tempS[i-1] and tempM[i] < 0:
                self.buy_or_sell.append("S")
            else:
                self.buy_or_sell.append("-")

    def get_macd(self):
        return self.macd[35::]

    def get_signal(self):
        return self.signal

    def get_buy_or_sell(self):
        return self.buy_or_sell


