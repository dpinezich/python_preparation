# importing packages
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# loading dataset
data = pd.read_csv('iris.csv')
#data = sns.load_dataset("https://github.com/mwaskom/seaborn-data/iris")


def plot():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)


with sns.axes_style('darkgrid'):
    # Adding the subplot
    plt.subplot(211)
    plot()

plt.subplot(212)
plot()
plt.show()
