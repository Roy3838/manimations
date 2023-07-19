for t in range(T):
    # Calcular Velocidad con Fuerza
    V[t+1] = V[t] + F(X[t])*dt
    # Calcular Posicion con Velocidad
    X[t+1] = X[t] + V[t+1]*dt