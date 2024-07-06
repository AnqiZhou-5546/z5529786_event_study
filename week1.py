print('Welcome to the Toolkit fo Finance T2 2024, hello from Anqi Zhou')
# Downloads Qantas share price beginning 1 January 2020
import yfinance                                           # (1)
_tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(_tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')
