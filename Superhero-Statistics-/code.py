# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data  = pd.read_csv(path)
data.Gender.replace('-', 'Agender', inplace=True)
gender_count = data.Gender.value_counts()
print(gender_count)
gender_count.plot(kind = 'bar')
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment = data.Alignment.value_counts()
print(alignment)
alignment.plot(kind='pie')
plt.show()


# --------------
#Code starts here
#print(data.head())
sc_df = data[['Strength','Combat']].copy()
sc_covariance = round(sc_df.cov().Combat.Strength,2)
print(sc_covariance)
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
sc_pearson = round(sc_covariance/(sc_combat*sc_strength), 2)
print(sc_pearson)

ic_df = data[['Intelligence' ,'Combat']].copy()
ic_covariance = round(ic_df.cov().Combat.Intelligence, 2)
print(ic_covariance)
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
ic_pearson = round(ic_covariance/(ic_intelligence*ic_combat), 2)
print(ic_pearson)

more_correlated = ('Intelligence', "Strength")[ic_pearson < sc_pearson]
print("Combat is more correlated to "+str(more_correlated))


# --------------
#Code starts here
#print(data.head())
total_high = data.Total.quantile(0.99)

super_best = data[data.Total > total_high]

super_best_names = list(super_best.Name)
print(super_best_names)



# --------------
#Code starts here
fig , (ax_1, ax_2, ax_3) = plt.subplots(1,3, figsize=(10,5))

ax_1.set_title('Intelligence')
data.boxplot(column=['Intelligence'], ax=ax_1)

ax_2.set_title("Speed")
data.boxplot(column=['Speed'], ax=ax_2)

ax_3.set_title("Power")
data.boxplot(column=['Power'], ax=ax_3)


plt.show()


