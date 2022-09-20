import numpy as np
import matplotlib.pyplot as plt
import pandas as p

# pa is a list of numbers and cai is a pandas series of numbers.

cai = p.Series([1.414419,0.437525,0.840999,0.552292,0.395373,0.381073,0.416165,0.437319,0.653811,0.495697,0.426237,0.468068,0.416777,0.377957,0.527219,0.418195,0.505802,0.410247,0.457362,0.405840])
pa = [125.0, 736.0, 269000.0, 26300.0, 1920.0, 861.0, 768.0, 1380.0, 38300.0, 16900.0, 967.0, 6800.0, 2780.0, 217.0, 6510.0, 304.0, 606.0, 1170.0, 2210.0, 227.0]

plt.scatter(pa, cai, s=2)
plt.plot(pa, np.poly1d(np.polyfit(pa, cai, 1))(pa), color='red')
plt.text(9, 0.25, f'Spearman R = {round(p.Series(pa).corr(cai, method="spearman"), 3)}')
plt.show()
