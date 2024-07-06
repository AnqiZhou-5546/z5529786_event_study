""" yf_example2.py
Example of a function to download stock prices from Yahoo Finance.
"""
import yfinance as yf

def yf_prc_to_csv(tic, pth, start=None, end=None):
    """ Downloads stock prices from Yahoo Finance and saves the
    information in a CSV file
    Parameters
    ----------
    tic : str
        Ticker

    pth : str
        Location of the output CSV file

    start: str, optional
    Download start date string (YYYY-MM-DD)
    If None (the default), start is set to '1900-01-01'
    end: str, optional
    Download end date string (YYYY-MM-DD)
    If None (the default), end is set to the most current date available
    """
    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)

# In Python, '__name__' is a special built-in variable that holds the name of the module in which it is used
# When a Python module is executed directly, not imported from another script, '__name__' is set to '__main__'
#print(f'current module __name__: {__name__}')

#import yf_example1
#print(f'imported module __name__: {yf_example1.__name__}')
#outcome: imported module __name__: yf_example1

#Windows user
#pth= 'D:\\看什么看    学习\\pycharm\\toolkit\\data\\test.csv'
#pth = r'D:\看什么看    学习\pycharm\toolkit\data'

if __name__ == '__main__':
    import os
    tic = 'QAN.AX'
    #datadir = r'D:\看什么看    学习\pycharm\toolkit\data'
    #pth = f'{datadir}\\test1.csv'
    import toolkit_config as cfg
    pth = os.path.join(cfg.DATADIR,'test1.csv')
    #yf_prc_to_csv(tic,pth)
    print(pth)

