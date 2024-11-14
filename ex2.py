import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

w = pd.read_csv('ch5-1.csv')
w_n = w.iloc[:, 1:5]


model_lm_food = smf.ols(formula='weight ~ food', data=w_n)
result_lm_food = model_lm_food.fit()

print(result_lm_food.summary())


plt.figure(figsize=(10, 7))
plt.scatter(w.food, w.weight, alpha=0.5)


slope, intercept = result_lm_food.params
plt.plot(w.food, w.food * slope + intercept, color='red')


plt.text(5, 132, f'weight = {slope:.4f}*food + {intercept:.4f}', fontsize=12)


plt.title('Scatter Plot')
plt.xlabel('food')
plt.ylabel('weight')

plt.show()
