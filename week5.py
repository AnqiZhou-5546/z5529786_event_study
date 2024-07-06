import os
import toolkit_config as cfg

ISO = os.path.join(cfg.DATADIR,'iso.txt')
def most_common_word(filepath):
    with open(ISO,mode='rt') as FOBJ:
    #open的default就是‘rt’
        counts = dict()
        for lines in FOBJ:
            words = lines.split()
            for word in words:
                counts[word] = counts.get(word,0) + 1
    #find the most frequent
                maxcount = None
                maxword = None
        for word, count in counts.items():
            if maxcount is None or count > maxcount:
                maxword = word
                maxcount = count
    return (f'The most frequent word is: {maxword}, and the number of times appeared is: {maxcount}')
print(most_common_word(ISO))

import pandas as pd
df=pd.DataFrame({'a':[1,2,3],'b':[4,5,6]},['c','d','e'])
print(df)