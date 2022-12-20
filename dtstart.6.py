from matplotlib import pyplot as plt
import statistics as st
import random
plt.style.use('classic')


types = ['cat fish', 'tillapia', 'baracuda', 'sharks',
         'lady fish', 'start fish', 'crayfish', 'lubster',
         'mockrel fish', 'titus', 'octopus', 'saw fish']


frequency = [200, 250, 240, 15,
             90, 80, 70, 60,
             150, 120, 90, 65]

m=st.mean(frequency)
me=st.median(frequency)


print(m, me)
colors = []


explode = [0]*12
explode[1] = 0.2

for i in range(12):

    rgb =(random.uniform(0,.7),random.uniform(0,.7),random.uniform(0,.7))
    colors.append(rgb)

plt.pie(frequency, colors=colors, autopct='%2.0f%%', startangle=100, textprops=dict(color='w'), shadow=True, explode=explode)

plt.legend(types, loc='right', bbox_to_anchor=(1,0.1,0.4,1))

plt.grid(True)

plt.show()



