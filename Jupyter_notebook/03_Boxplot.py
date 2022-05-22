import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
sns.boxplot(x='day',y='tip',data=tips)

plt.show()
