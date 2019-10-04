import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_absolute_error

#cerner_2^5_2019

#TEAM_DICT = {'Baltimore Colts': 'Indianapolis Colts','San Diego Chargers': 'Los Angeles Chargers','Houston Oilers': 'Tennessee Titans','Los Angeles Raiders': 'Oakland Raiders','St. Louis Rams': 'Los Angeles Rams','St. Louis Cardinals': 'Arizona Cardinals','Phoenix Cardinals': 'Arizona Cardinals','Tennessee Oilers': 'Tennessee Titans'}
df = pd.read_csv('spreadspoke_scores.csv')
df = df.drop(['schedule_date', 'schedule_week', 'schedule_playoff', 'team_favorite_id', 'stadium', 'stadium_neutral', 'weather_detail'], axis=1)
df = df.dropna()
df = df[ df['over_under_line'] != ' ']
df['actual_score'] = df['score_home'] + df['score_away']
df = df[['spread_favorite', 'over_under_line', 'actual_score']]
df = df.apply(pd.to_numeric)
X = df.drop('actual_score', axis = 1)
y = df['actual_score']
X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
mlp = MLPClassifier(hidden_layer_sizes=(2),max_iter=1000)
mlp.fit(X_train,y_train)
predictions = mlp.predict(X_test)
my_pred = pd.DataFrame({'predicted':predictions,'actual':y_test.values})
print(f'Mean Absolute Error: {mean_absolute_error(y_test.values, predictions)}')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(my_pred)
