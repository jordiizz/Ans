import numpy as np

#Metodo del a tartaglia
#ax^3 + bx^2 + xc + d = 0


def normalizar_ecuacion(a, b, c, d):
    """_summary_

    Args:
        a (int or float): Es el primer coeficiente 
        b (int or float): Segundo
        c (int or float): Tercero
        d (int or float): Cuarto

    Returns:
        int or float: retorna los tres valores normalizados
        en un orden de a, b, c
    """
    return b/a, c/a, d/a

def calc_pq(a, b, c):
    return (3*b - a**2) / 3, (2*a**3 - 9*a*b + 27*c) / 27

def calc_Δ(p, q):
    return (q/2)**2 + (p/3)**3

def calc_u(q, Δ):
    return np.cbrt(-q/2 + np.sqrt(Δ))

def calc_v(q, Δ):
    return np.cbrt(-q/2 - np.sqrt(Δ))


def tartaglia(a,b,c,d):
    
    #1. Normalizamos la Ecuación a la forma X³ + aX² + bX + c = 0
    a, b ,c = normalizar_ecuacion(a=a, b=b, c=c, d=d)    
    
    #2. Calcular P y Q
    p, q = calc_pq(a=a,b=b,c=c)
 
    #Ecuación y³ + py + q =0
    #3. Calcular discriminante
    Δ = calc_Δ(p=p, q=q)

    if Δ == 0:
        if p == q == 0:
            print(f'La Ecuación Tiene Raíz Triple y Todas son iguales')
            return  [-a / 3] * 3
        print(f'La Ecuación tiene Raíz doble')
        return [(((-3*q) / (2*p)) - (a / 3)),
                (((-3 * q) / (2 * p)) - ((a /3 ))),
                (((-4 * (p**2)) / (9*q)) - (a/3))]
    elif Δ > 0:
        print(f'La Ecuación tiene Una Raíz real, Dos Imaginarias')
        u = calc_u(q=q, Δ=Δ)
        v = calc_v(q=q, Δ=Δ)
        return [np.cbrt(-q/2 + np.sqrt(Δ)) + np.cbrt(-q/2 - np.sqrt(Δ)) - a/3,
                complex(-(u+v) / 2 - a/3 , (np.sqrt(3) / 2) * (u-v)),
                complex(-(u+v) / 2 - a/3 , -(np.sqrt(3) / 2) * (u-v))
                ]  
    print(f'Tres Raíces reales Simples') 
    coseno = (-q/2) / np.sqrt(-(p/3)**3)
    Θ = np.arccos(coseno)        
    return [ float(2 * np.sqrt(-p / 3) * np.cos((Θ + 2*np.pi*k)/3) - a/3)  for k in range(3)]
            
            

            
        
    
    

