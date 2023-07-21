for t in range(T):
    # Calcular Posicion con Velocidad
    P[t+1] = P[t] + V[t]*dt
    # Calcular Velocidad con Fuerza
    V[t+1] = V[t] + A(P[t])*dt
    