import allel
import pandas as pd
from icecream import ic

def _remove_extrakeys(d):
    if 'samples' in d.keys():
        d.pop('samples')
    return d

def _cast_numpy(d):
    for k in d.keys():
        d[k] = d[k].tolist() 
    return d

def preprocess(d):
    d = _remove_extrakeys(d)  # drop key since it has different dimension
    d = _cast_numpy(d) # convert numpy arrays to list
    
    return pd.DataFrame.from_dict(d) # return dataframe

def search(df, chrom='chr1', pos=10001, id='.'):
    return df.loc[(df['variants/CHROM'] == chrom) & (df['variants/ID'] == id) & (df['variants/POS'] == pos)]


if __name__ == "__main__":
    dataset = allel.read_vcf('./input_tiny.vcf')
    df = preprocess(dataset)
    results = search(df)
    ic(results)
