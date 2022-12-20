from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix

x,y = make_classification(
    n_samples=700,
    n_features=1,
    n_informative=1,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    n_clusters_per_class=1,
    weights=None

)


plt.style.use('seaborn')
plt.xlabel=('x values')
plt.ylabel=('y values')

plt.scatter(x, y, label='logist plots', cmap='rainbow', edgecolors='k')
plt.legend()
plt.grid(True)
plt.tight_layout(0.5,0.4)



lge = LogisticRegression()
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.1, random_state=0)
lge.fit(x_train, y_train)


rlge =lge.predict(x_test)
print(rlge)


clge = lge.coef_

print('coefficients:{}'.format(clge))

ilge = lge.intercept_
print('intercepts:{}'.format(ilge))


_c=confusion_matrix(y_test, rlge)
print(_c)

plt.show()
