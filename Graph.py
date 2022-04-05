import matplotlib.pyplot as plt


class Graph:

    def draw_exchange(self, x, y):
        plt.plot(x, y, label="Kurs DIS")
        plt.xlabel("Data")
        plt.ylabel("Kurs w danym dniu")
        plt.legend()
        plt.grid(True)

    def draw_macd_signal(self, x, macd, signal, buy_or_sell, with_or_without_letter):
        plt.plot(x, macd, label="macd", color='blue')
        plt.plot(x, signal, label="signal", color='red')

        if(with_or_without_letter):
            for i in range(1, len(macd) - 1):
                if buy_or_sell[i] != "-":
                    plt.annotate(buy_or_sell[i], xy=(x[i], macd[i]))

        plt.legend()
        plt.grid(True)
        plt.ylabel('Wartość MACD/SIGNAL')
        plt.xlabel('Data')

    def draw_exchange_macd_signal(self, x, y, macd, signal, buy_or_sell, with_or_without_letter):
        plt.figure('Piotr Kopecki 184746')
        plt.subplot(2, 1, 1)
        self.draw_exchange(x, y)
        plt.subplot(2, 1, 2)
        self.draw_macd_signal(x[35::], macd, signal, buy_or_sell, with_or_without_letter)
        plt.savefig("Caly_wykres.png")
        plt.show()

