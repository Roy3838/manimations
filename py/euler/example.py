for t in range(T):
    # Calculate Position with Velocity
    P[t+1] = V[t]*dt + P[t] 
    # Calculate Velocity with Force
    V[t+1] = A(P[t])*dt + V[t] 
    