import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#cerner_2^5_2019

df = pd.read_csv('spreadspoke_scores.csv')
df['weather_humidity'] = pd.to_numeric(df['weather_humidity'], errors = 'coerce')
df = df.dropna(subset = ['score_home', 'score_away', 'weather_humidity'])
df['total_score'] = df['score_home'] + df['score_away']
df['weather_humidity'] = df['weather_humidity'].astype(float)

humidity_grouped = []
for i in range(0, 100, 10):
    humidity_grouped.append(df.loc[(df['weather_humidity'] > i) & (df['weather_humidity'] <= i+10)])

mean_points_grouped = list(map(lambda x: x['total_score'].mean(), humidity_grouped))

axes = plt.axes()
axes.set_ylim([39, 44])
p1 = plt.plot(np.arange(len(mean_points_grouped)), mean_points_grouped, marker = 'o')
plt.ylabel('Average Score')
plt.xlabel('Humidity %')
plt.title('Humidity and Scores')
plt.xticks(np.arange(10), ('0-10%', '11-20%', '21-30%', '31-40%', '41-50%', '51-60%', '61-70%', '71-80%', '81-90%', '91-100%'))
plt.show()


