import numpy as np

#Metodo del a tartaglia

#ax^3 + bx^2 + xc + d = 0


def normalizar_ecuacion(a, b, c, d):
    return b/a, c/a, d/a

def calc_pq(a , b, c):
    return (3*b - a**2) / 3, (2*a**3 - 9*a*b + 27*c) / 27

# 1. Transformar a la forma x^3 + ax^2 + bx + c = 0
def tartaglia(a = 0, b = 0, c = 0, d = 0):

    #1. Normalizamos la Ecuación a la forma X³ + aX² + bx + c = 0
    a, b, c = normalizar_ecuacion(a = a, b = b, c = c, d = d)
    x_results = []
    

    #2. Calcular P y Q
    p, q = calc_pq(a = a, b = b, c = c)


    # ^^^ = y^3 + py + q =0
    #3. Calcular discriminante

    delta = (q/2)**2 + (p/3)**3

    if delta == 0:
        if p == q and q == 0:
            print("Raíz triple: ", -a/3)
            return -a/3
        else: 
            x1 = (-3*q)/(2*p) - a/3
            x2 = (-4*p**2)(9*q) - a/3
            x_results.append(x1,x2)
            print("Raíz doble: ", x1,x2)
            return x_results
    elif delta > 0:
        x1 = (-q/2 + np.sqrt(delta))**(1/3) + (-q/2 - np.sqrt(delta))**(1/3) - a/3
    
        #sacar u y v

        u = (-q/2 + np.sqrt(delta))**(1/3)
        v = (-q/2 - np.sqrt(delta))**(1/3)

        #xi1 = [-(u+v)/2 - a/3 + (np.sqrt(3)/2)(u-v)]
    
        xi1 = [-(u+v)/2 - a/3 , (np.sqrt(3)/2)(u-v)] #[Real, Imaginario]
        xi2 = [-(u+v)/2 - a/3 , -(np.sqrt(3)/2)(u-v)]
    
        print("1 real, 2 imaginarias: ", x1, xi1, xi2)
        return x_results.append(x1, xi1, xi2)
    else:
        coseno = (-q/2)/np.sqrt(-(p/3)**3)
        theta = np.arccos(coseno)
    
        X_results = [ float(2 * np.sqrt(-p/3) * np.cos((theta + 2*np.pi*k)/3) - a/3 ) for k in range(3)]
        for k in range(0, 3):
            x_results.append(
                2 * np.sqrt(-p/3) * np.cos((theta + 2*np.pi*k)/3) - a/3                
            )
        #print("3 reales: ", x_results)
        return x_results, X_results
            
            
print(tartaglia(6, 7, -9, 2))