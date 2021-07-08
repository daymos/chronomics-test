import allel
import pandas as pd
from icecream import ic

def preprocess(d):
    d.pop('samples')  # drop key since it had different dimension
    
    for k in d.keys():
        d[k] = d[k].tolist() # convert numpy arrays to list
    
    return pd.DataFrame.from_dict(d) # return dataframe

def search(df, chrom='chr1', pos=10001, id='.'):
    return df.loc[(df['variants/CHROM'] == chrom) & (df['variants/ID'] == id) & (df['variants/POS'] == pos)]


if __name__ == "__main__":
    dataset = allel.read_vcf('./input_tiny.vcf')
    df = preprocess(dataset)
    results = search(df)
    ic(results)


