for t in range(T):
    # Calcular Posción con Velocidad
    P[t+1] = V[t]*dt + P[t] 
    # Calcular Velocidad con Fuerza
    V[t+1] = A(P[t])*dt + V[t] 
    