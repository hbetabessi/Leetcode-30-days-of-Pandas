import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    conditions = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    return products.loc[conditions, ['product_id']]
