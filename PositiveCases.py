import pandas as pd
import numpy as np


def main():
    import urllib.request, json 
    with urllib.request.urlopen("https://api.covid19india.org/raw_data.json") as url:
        data = json.loads(url.read().decode())
        df=pd.DataFrame(data["raw_data"])
        df.to_csv('.\\positive.csv',index=False)
if __name__ == '__main__':
    main()

