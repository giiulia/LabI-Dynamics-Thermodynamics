import numpy as np
B = np.array([14.494])
A = np.array([-0.958 ])
N = np.array([5, 5, 5, 5, 5])
x = np.array([1, 2, 3, 4, 5])
y = np.array([13.88, 27.89,  42.13, 56.85, 71.87])
s_y = np.sqrt(sum((y-A-B*x)**2)/(N-2))
print(s_y)
#calcolo il coefficiente B
pesi = 1/np.power(s_y,2)
#print(sum(pesi))
delta = (sum(pesi)*sum(pesi*np.power(x,2)))-(np.power(sum(pesi*x),2)) 
coefficiente = ((sum(pesi)*sum(pesi*x*y))-(sum(pesi*x)*sum(pesi*y)))/delta

print("il coefficiente è: B={0:.3f}".format(coefficiente))

#calcolo l'intercetta A 
intercetta = ((sum(pesi*np.power(x,2))*sum(pesi*y))-(sum(pesi*x)*sum(pesi*x*y)))/delta

print("l'intercetta è: A={} dunque non posso trascurarla".format(intercetta))

#calcolo sigma intercetta
sigma_A = np.sqrt(sum(pesi*np.power(x, 2)))/np.sqrt(delta)
print("l'incertezza su A è: sigma_A={}".format(sigma_A))

#calcolo sigma coefficiente
sigma_B = np.sqrt(sum(pesi))/np.sqrt(delta)
print("l'incertezza su B è: sigma_B={}".format(sigma_B))

#k = 9.81/coefficiente #statica
#sigma_k = np.sqrt(np.power(0.01/coefficiente, 2)+np.power(9.81*sigma_B/coefficiente**2, 2))
v = coefficiente*2*1.08
sigma_v = 2*1.08*sigma_B
print("la velocità è {}±{}".format(v, sigma_v))