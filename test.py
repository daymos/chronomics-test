import allel
import pandas as pd
from icecream import ic


def _remove_extrakeys(d):
    return  { key: value for key, value in d.items() if key in ['POS_ID', 'CHROM', 'ALT']}


def _rename(d): # type: ignore
    d['ALT'] = d.pop('variants/REF')
    d['POS_ID'] = d.pop('variants/POS')
    d['CHROM'] = d.pop('variants/CHROM')
    return d

def _cast_to_list(d):
    return { key: value.tolist() for key, value in d.items() }

def preprocess(d):
    d = _rename(d)
    d = _remove_extrakeys(d)  # drop unused keys 
    d = _cast_to_list(d) # convert numpy arrays to list
    
    return pd.DataFrame.from_dict(d) 


def search(df, chrom='chr1', pos=10001):
    df_result = df.loc[(df['CHROM'] == chrom) & (df['POS_ID'] == pos)]
    if df_result.shape[0] == 0:
        print('no results')
    else: 
        print(chrom, pos, ' is ',  df_result['ALT'][0])


if __name__ == "__main__":
    dataset = allel.read_vcf('./input_tiny.vcf')
    df = preprocess(dataset)
    results = search(df)
