import pandas as pd

stats = pd.read_csv('mvp_votes/csv/players_mvps_stats.csv')

# Each row is an NBA player. Each row&year are unique
# We're gonna use this PGs stats to predict how many points the player would have won in NBA voting. We want to predict the MVP Share

# print(stats)

del stats['Unnamed: 0']

# ML algotithms don't like null values/missing values
null= pd.isnull(stats).sum() # .sum makes it easier to read
# print(null)

# There are some null values in the %. No attemps???
three_point_perc_check = stats[pd.isnull(stats['3P%'])][['Player', '3PA']] # Any rows in stat where 3p% is null
# print(three_point_perc_check)

# So null value = no attemps

stats= stats.fillna(0)
# null= pd.isnull(stats).sum()
# print(null)

# Let's create pur first attempt at a machine learning algorithm
# We will use all the numer columns to make our predictions

# print(stats.columns)
predictors = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P',
       '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB',
       'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Year', 
       'W', 'L', 'W/L%', 'GB', 'PS/G', 'PA/G', 'SRS']

#  We want to predict the MVP Share and we removed every variables that directly correlate with Share

training = stats[stats['Year'] < 2021] # All the mvp/players data before 2021
test = stats[stats['Year'] == 2021] # Test year is 2021. DON'T TEST ON DATA THAT IS BEFORE DATA WE'RE TRAINING ON. The way we test the algorithm has to be the same way we'll use it in the real world. If we dont'do this the algorithm will overfit, it means that it will look awesome when we're testing it and when we use it, it doesn't work at all. 

from sklearn.linear_model import Ridge 
# Ridge regression is a form linear regression that is design to prevent overfitting. It shrinks the linear regression coefficient to avoid overfitting

reg = Ridge(alpha=.1) # alpha controls how much the coefficient is going to be shrunk to prevent overfitting
reg.fit(training[predictors], training['Share']) # Fit the model first on all of the predictor columns in the training ds. We're taking all of this columns in the training ds and making predictions based on them. We're trying to predict Share 

predictions = reg.predict(test[predictors]) # We're using the predictor columns in the test DF to make this predictions
# print(predictions) --> numpy array
predictions = pd.DataFrame(predictions, columns=['predictions'], index=test.index)
# print(predictions)

# We can compare actual values to our predictions

combination = pd.concat([test[['Player', 'Share']], predictions], axis=1) # We're combining the test Player and Shares columns and the predictions. On axis=1 it means we will combine the columns
# print(combination)

# We basically added an extra column called predictions. FOr every player in the 2021 season we now have the Share and our predictions

# print(combination.sort_values('Share', ascending=False).head(10)) # Who won the mvp is first

# Jokic won the mvp but doesn't have the highest predictors that is Antetokounmpo. Is his share the highest across all the players?

# How we evaluate if this algorithm did a good job? We have to think about an error metric.
# One of the most important part is picking an error metric. It helps you know if the alg performed weel or not

from sklearn.metrics import mean_squared_error # We're trying a default error metric from sklearn
mse = mean_squared_error(combination['Share'], combination['predictions'])  # It takes th actual values and the predicted values and comes up with an error metric based on that
# print(mse) # 0.002668239849159427 is the mean difference between the predictions and the actual values. But is not super meaningfull to us because we dont' care about the actual values and a lot of values are actually 0
# print(combination['Share'].value_counts()) # 525 are 0

# We just care about the top players --> We need a new error metric that thinks about the rank of the player

combination = combination.sort_values('Share', ascending=False)
# print(combination) 

# We have to go ahed and assign a Rank to players
combination['Rk'] = list(range(1, combination.shape[0] +1))  # We have a rank in order of mvp voting
# print(combination)

# We need to figure out the rank for our predictions
combination = combination.sort_values('predictions', ascending=False)
combination['Predicted_Rk'] = list(range(1, combination.shape[0] +1))
# print(combination.head(10)) # We can see the difference between the Rk and the Predicted_rk. There are some outliers

# We need to figure out what our error metric should be. There are a variety of directions we can go but one that makes sense is: of the top five people in the mvp race how many of them have we correctly place on the top 5? 

# average_precision is the one we will use. Not so used because it deal swith rank, but it's our specific case!

# print(combination.sort_values('Share', ascending=False).head(10))

# Of the top 5 ranked players in the mvp voting how far down do you gahave to go in our predictions to find him.
# For Nikola Jokic you have to go down 3 predictions
# For Joel Embiid you have to go down 2
# Steph Curry you have to go down 6
# Do you have the player who i supposed to be in the top 5 in the top 5?
# If yes we're gonna give you a perfect score if you didn't we're gonna se how long it took you to include that person and penalize you based on how long it took you to actually predict that player in 

""" def find_ap(combination):
    actual = combination.sort_values('Share', ascending=False).head(5)
    predicted = combination.sort_values('predictions', ascending=False)
    ps = []
    found = 0
    seen = 1
    for index, row in predicted.iterrows():
       if row['Player'] in actual['Player'].values:
            found +=1
            ps.append(found/seen)
       seen +=1
    return (ps) """

# print(find_ap(combination))
# [1.0, 1.0, 1.0, 0.6666666666666666, 0.15151515151515152]. Perfect score for the first three thna we have (Curry)4/6, (Paul)5/33 
# return sum(ps) / len(ps) 

def find_ap(combination):
    actual = combination.sort_values('Share', ascending=False).head(5)
    predicted = combination.sort_values('predictions', ascending=False)
    ps = []
    found = 0
    seen = 1
    for index, row in predicted.iterrows():
       if row['Player'] in actual['Player'].values:
            found +=1
            ps.append(found/seen)
       seen +=1
    return sum(ps) / len(ps)

# print(find_ap(combination)) # This is our error metric 0.7636363636363636. The lower it gets the longer it tooks our predicitons to find mvp. This have to be the highest possibile


# BACKTESTING 

years =  list(range(1993, 2024))
aps = []
all_predictions = []
for year in years[5:]:  # We start from the fifth year because we need some data to make predictions
       training = stats[stats['Year'] < year]
       test = stats[stats['Year'] == year] # We are starting in 1996 and we're saying all the data from 1993 trhough 1998 inclusive are or training set. 1998 is our test set which we're making predictions
# This is good because in makes our error metrics more robust. If we look at errors for single year, that year could have been really weird and even if for algorthm looks good it doesn't mean it is. The more years we can test pur algorithm on, the more confidence we can have that it's not going to overfit  nd gonna work properly
       reg.fit(training[predictors], training['Share'])
       predictions = reg.predict(test[predictors])
       predictions = pd.DataFrame(predictions, columns=['predictions'], index=test.index)
       combination = pd.concat([test[['Player', 'Share']], predictions], axis=1)
       all_predictions.append(combination) # List that has predictions for every single year
       aps.append(find_ap(combination)) # Average preciosn scores

mean_average_precision = sum(aps) / len(aps)
print(mean_average_precision)  # 0.7356320654877144. Alg looks a little bit worse when we run across all of our data but it's still pretty accurate



def add_ranks(combination):
       combination = combination.sort_values('Share', ascending=False)
       combination['Rk'] = list(range(1, combination.shape[0] +1)) 
       combination = combination.sort_values('predictions', ascending=False)
       combination['Predicted_Rk'] = list(range(1, combination.shape[0] +1))
       combination['Diff'] = combination['Rk'] - combination['Predicted_Rk'] # This tell us the biggest difference between actual and predicted rank 
       return combination

ranking = add_ranks(all_predictions[1]) # Predictions from 1999 season 
# print(ranking[ranking['Rk'] < 6 ].sort_values('Diff', ascending=False)) # It gives me the top 5 MVP vote getters along with their predicted rank and difference. This is helpfull for diagnostic, we will use it later
# a.to_csv('mvp_votes/csv/top_5_mvp_vote_getter.csv')

def backtest(stats, model, year, predictors):
       aps = []
       all_predictions = []
       for year in years[5:]:  # We start from the fifth year because we need some data to make predictions
              training = stats[stats['Year'] < year]
              test = stats[stats['Year'] == year] # We are starting in 1996 and we're saying all the data from 1993 trhough 1998 inclusive are or training set. 1998 is our test set which we're making predictions
       # This is good because in makes our error metrics more robust. If we look at errors for single year, that year could have been really weird and even if for algorthm looks good it doesn't mean it is. The more years we can test pur algorithm on, the more confidence we can have that it's not going to overfit  nd gonna work properly
              model.fit(training[predictors], training['Share'])
              predictions = reg.predict(test[predictors])
              predictions = pd.DataFrame(predictions, columns=['predictions'], index=test.index)
              combination = pd.concat([test[['Player', 'Share']], predictions], axis=1)
              combination = add_ranks(combination)
              all_predictions.append(combination) # List that has predictions for every single year
              aps.append(find_ap(combination)) # Average preciosn scores
       return sum(aps)/len(aps), aps, pd.concat(all_predictions)

mean_ap, aps, all_predictions = backtest(stats, reg, years[5:], predictors)
# print(mean_ap) # 0.7356320654877144 We got the same result as before. but we now have this function

# DIAGNOSTIC

ten_biggest = all_predictions[all_predictions['Rk'] <= 5 ].sort_values('Diff').head(10) # It's looking at all predictions and at anyone who is ranked higher or lower than 5 and it looks at biggest differences, the ten biggest differences 
# print(ten_biggest)
""" 
                 Player  Share  predictions  Rk  Predicted_Rk  Diff
1369         Jason Kidd  0.712     0.024669   2            66   -64
5443         Steve Nash  0.839     0.036338   1            43   -42
8884    Peja Stojaković  0.228     0.034965   4            40   -36
13146       Joakim Noah  0.258     0.046147   4            38   -34
3857   Chauncey Billups  0.344     0.050896   5            36   -31
5461         Steve Nash  0.739     0.057325   1            32   -31
1534         Chris Paul  0.138     0.071666   5            33   -28
5267         Jason Kidd  0.135     0.047001   5            23   -18
5476         Steve Nash  0.785     0.080034   2            18   -16
1302        Gary Payton  0.372     0.072364   3            16   -13 """

# ten_biggest.to_csv('mvp_votes/csv/ten_biggest.csv')

# We can also look at the coefficient of the regression 
# print(reg.coef_) # This tells us which variables the algorithm is keying in most. The highest coefficient indicates the variables that are most important for the regression 

""" 
[ 2.60322428e-04  8.36567762e-05 -6.19280132e-06 -3.82593515e-03
  1.83681637e-04  7.91563850e-03 -1.71735246e-01  3.29381772e-03
 -1.27638912e-02 -9.96266559e-03  1.88459266e-02 -1.93272151e-02
  9.42220008e-03  1.03935227e-01 -6.38441164e-03  1.06457605e-02
 -4.92802532e-03  2.26288955e-02  3.56267832e-02 -2.83840306e-02
  6.83896806e-03  1.10293075e-02  1.04861244e-02 -8.15952423e-03
 -3.14142009e-03  6.74774734e-03 -1.99533205e-04  1.27761717e-04
 -2.79477652e-04  2.98960701e-02  2.48313047e-04 -8.25976647e-04
  9.46781237e-05 -3.90606300e-04] """

# Not so usefull, we don't have the names of the variables

conc= pd.concat([pd.Series(reg.coef_), pd.Series(predictors)], axis=1)
# print(conc.sort_values(0, ascending=False))

""" 
          0     1
13  0.103935  eFG% This is the most effective 
18  0.035627   DRB
29  0.029896  W/L%
17  0.022629   ORB
10  0.018846    2P
21  0.011029   STL
15  0.010646   FTA
22  0.010486   BLK
12  0.009422   2P%
5   0.007916   FGA
20  0.006839   AST
25  0.006748   PTS
7   0.003294    3P
0   0.000260   Age
30  0.000248    GB
4   0.000184    FG
27  0.000128     W
32  0.000095  PA/G
1   0.000084     G
2  -0.000006    GS
26 -0.000200  Year
28 -0.000279     L
33 -0.000391   SRS
31 -0.000826  PS/G
24 -0.003141    PF
3  -0.003826    MP
16 -0.004928   FT%
14 -0.006384    FT
23 -0.008160   TOV
9  -0.009963   3P%
8  -0.012764   3PA
11 -0.019327   2PA
19 -0.028384   TRB
6  -0.171735   FG% """

# conc.to_csv('mvp_votes/csv/alg_variables.csv')