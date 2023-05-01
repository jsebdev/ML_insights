import random
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import numpy as np

def next_value(prev):
    weights = [-0.3, -0.4, -0.5, 0.4, 0.3, 0.2]
    m = min(len(weights), len(prev))
    z = list(zip(weights[:m], prev[-m:][::-1]))
    # print(f'7: z >>>\n{z}')
    muls = ([a*b for a,b in z])
    # print(f'7: muls >>>\n{muls}')
    next_value = sum(muls)
    # prev.append(next_value + random.randint(-10, 10))
    prev.append(next_value)

serie = [1]

for i in range(30):
    next_value(serie)
print(serie)
plt.figure('serie')
plt.plot(serie)


s = np.array(serie)
# plt.figure('acf')
plot_acf(s, lags=10)
# plt.figure('pacf')
plot_pacf(s, lags=10, method='ols')
plt.show()