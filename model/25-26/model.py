import pandas 
import numpy
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pandas.read_csv('prem25-26.csv')
df = df[df['Result'].notna() & (df['Result'] != '')]

df[['home_team_score', 'away_team_score']] = df['Result'].str.split(' - ', expand=True).astype(int)
features_list = []
for i, (idx, row) in enumerate(df.iterrows()):
    features = {
        'home_team': row['Home Team'],
        'away_team': row['Away Team'],
        'matchweek': row['Round Number'],
        'home_goals': row['home_team_score'],
        'away_goals': row['away_team_score']
    }
    features_list.append(features)
df_features = pandas.DataFrame(features_list)
print(df_features)