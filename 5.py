import sys 
import urllib
import pickle

obj = pickle.load(urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for tmp in obj:
    for value in tmp:
        sys.stdout.write(value[0] * value[1])
    print