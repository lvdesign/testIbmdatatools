
# Mode
data['montant'].mode()


# Moyenne
data['montant'].mean()

# Mediane
data['montant'].median()


# Variance empirique: C'est le théorème de König-Huygens
data['montant'].var()

# variance empirique sans biais 
data['montant'].var(ddof=0)


# L'écart-type empirique :la racine carrée de la variance empirique
data['montant'].std()


# Coefficient de variation 
data['montant'].std/data['montant'].mean()




# La boîte à moustaches (boxplot)
'''Elle permet de représenter schématiquement une distribution, en incluant sa dispersion. La boîte est délimitée par Q1 et Q3, et on représente souvent la médiane à l’intérieur de la boîte. '''
data.boxplot(column="montant", vert=False)
plt.show()




# Découvrez les mesures de forme
# Le Skewness empirique Le skewness est une mesure d'asymétrie
data['montant'].skew()


# Le Kurtosis empirique
'''Le kurtosis empirique n'est pas une mesure d'asymétrie, 
mais c'est une mesure d'aplatissement. 
L’aplatissement peut s’interpréter à la condition que la distribution soit symétrique. 
En fait, on compare l'aplatissement par rapport à la distribution la plus célèbre, 
appelée distribution normale (parfois "courbe de Gauss" ou "Gaussienne"). '''

data['montant'].kurtosis()



# les mesures de concentration
# Courbe de Lorenz
depenses = data[data['montant'] < 0]
dep = -depenses['montant'].values # trier les individus dans l'ordre croissant des valeurs de la variable
n = len(dep)
lorenz = np.cumsum(np.sort(dep)) / dep.sum()  #la somme cumulée
lorenz = np.append([0],lorenz) # La courbe de Lorenz commence à 0

xaxis = np.linspace(0-1/n,1+1/n,n+1) #Il y a un segment de taille n pour chaque individu, plus 1 segment supplémentaire d'ordonnée 0. Le premier segment commence à 0-1/n, et le dernier termine à 1+1/n.
plt.plot(xaxis,lorenz,drawstyle='steps-post')
plt.show()


# La médiale de la courbe de Lorenz
'''Nous avons dit que la courbe de Lorenz est un escalier de hauteur 1. Le salaire médial, c'est simplement le salaire de la personne qui se trouve à la moitié de la hauteur : 0,5.'''

# l'indice de Gini
'''La courbe de Lorenz n'est pas une statistique, c'est une courbe ! Du coup, on a créé l'indice de Gini, qui résume la courbe de Lorenz.

Il mesure l'aire présente entre la première bissectrice et la courbe de Lorenz. Plus précisément, si on note S
 cette aire, alors :

gini=2*S'''
AUC = (lorenz.sum() -lorenz[-1]/2 -lorenz[0]/2)/n 
# Surface sous la courbe de Lorenz. Le premier segment (lorenz[0]) est à moitié en dessous de 0, on le coupe donc en 2, on fait de même pour le dernier segment lorenz[-1] qui est à moitié au dessus de 1.
S = 0.5 - AUC # surface entre la première bissectrice et le courbe de Lorenz
gini = 2*S
gini