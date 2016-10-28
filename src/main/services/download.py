import urllib
import os

def fetch_data(symbols):
    for symbol in symbols:
        url = "http://ichart.finance.yahoo.com/table.csv?s="+symbol+\
        "&amp;d=1&amp;e=1&amp;f=2016&amp;g=d&amp;a=8&amp;b=7&amp;c=2000&amp;ignore=.csv"

        time_frame = "m" # d -> daily, w -> weekly, m -> monthly.
        url = "http://real-chart.finance.yahoo.com/table.csv?s="+symbol+\
                "&a=11&b=22&c=1998&d=09&e=21&f=2016&g="+time_frame+"+&ignore=.csv"

        fileName = 'C:/data_stock/{}.csv'.format(symbol)
        if os.path.isfile(fileName):
            open(fileName, 'a').close()

        urllib.urlretrieve(url, fileName)
        print "DEBUG: Downloading for "+symbol
        print "DEBUG: URL:"+url

"""
def test_run():
    # Choose stock symbols to read
    #symbols = ['XLY', 'XLF','XLU','XLP','XLE','XLV','XLB','XLK','XLI']
    symbols = ['AAPL', 'SPY', 'IBM']
    for symbol in symbols:
       fetch_data(symbol) #Download csv for symbol loading.
test_run()
"""
symbols = ['SPY', 'GOOG','AAPL','GLD','XOM']
fetch_data(symbols)
#fetch_data("GLD")