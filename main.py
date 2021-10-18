import yfinance as yf
company = yf.Ticker('MSFT')
stock_data = company.history(period="1mo")
print(stock_data)