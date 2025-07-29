import numpy as np
from scipy.sparse import lil_matrix, eye
from scipy.sparse.linalg import spsolve


# ------------- gridworld -------------
states  = list(range(1, 16))                    # non-terminal state labels
actions = ['up', 'down', 'left', 'right']
pi_prob = 1 / len(actions)                      # equiprobable random policy
idx     = {s:i for i, s in enumerate(states)}
alter_thirteen =  False

def step(state, action, alter_thirteen):
    """Deterministic next‑state + reward."""
    next_state = None
    
    # Handle state 15 separately
    if state == 15:
        moves = {'up': 13, 'down': 15, 'left': 12, 'right': 14}
        return moves[action], -1
    
    # Handle the altered state 13 separately
    if alter_thirteen and state == 13:
        moves = {'up': 9, 'down': 15, 'left': 12, 'right': 14}
        return moves[action], -1

    if action == "up":
        if state > 4:
            next_state = state - 4
        elif state in [1, 2, 3]:
            next_state = state
    if action == "down":
        if state < 11:
            next_state = state + 4
        elif state in [12, 13, 14]:
            next_state = state
    if action == "left":
        if state % 4 == 0:
            next_state = state
        elif state > 1:
            next_state = state - 1
    if action == "right":
        if (state + 1) % 4 == 0:
            next_state = state
        elif state < 14:
            next_state = state + 1

    return next_state, -1

# ------------- build P_pi and r_pi -------------
n  = len(states)
P  = lil_matrix((n, n))                     # mutable sparse format
r  = np.zeros(n)

for s in states:
    i = idx[s]
    for a in actions:
        s_next, reward = step(s, a, alter_thirteen)
        j = idx.get(s_next, None)       
        if j is not None:               # only non‑terminal next states go in P
            P[i, j] += pi_prob
        r[i] += pi_prob * reward

P  = P.tocsr()                          # efficient CSR format for solves
A  = eye(n, format='csr') - P           # I - P_pi
v  = spsolve(A, r)                      # exact solution vector
print(v)
if alter_thirteen:
    np.save('docs/ch04_ex04-02/altered_state_values.npy', v)
else:
    np.save('docs/ch04_ex04-02/original_state_values.npy', v)