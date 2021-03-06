# -*- coding: utf-8 -*-
"""split_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R89HBtv2LIm6XL6dBr_B-NnxeFLGYY9Y
"""

# from google.colab import drive
# drive.mount('/content/drive')

!pip install iterative-stratification

import pandas as pd 
from iterstrat.ml_stratifiers import MultilabelStratifiedKFold

# ROOT = '/content/drive/My Drive/Colab Notebooks/kaggle/MoA/input'

if __name__ == "__main__":
    df = pd.read_csv(f"{ROOT}/train_targets_scored.csv")
    df.loc[:, "kfold"] = -1
    df = df.sample(frac=1).reset_index(drop=True)

    targets = df.drop("sig_id", axis=1).values

    mskf = MultilabelStratifiedKFold(n_splits=5)
    
    for fold_, (trn_, val_) in enumerate(mskf.split(X=df, y=targets)):
        df.loc[val_, "kfold"] = fold_

    df.to_csv(f"{ROOT}/train_targets_folds.csv", index=False)