import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
 conditions = (world.area >= 3000000)  | (world.population >= 25000000)
 return world[conditions][['name','area','population']]
