import random

x, y = 1.0, 1.0
deltas = [0.062, 0.125, 0.250, 0.500, 1.000, 2.000, 4.000]
n_trials = 2**12
print "delta | acceptance"
for delta in deltas:
    n_hits = 0
    for i in range(n_trials):
        del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
        if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
            x, y = x + del_x, y + del_y
        if x**2 + y**2 < 1.0: n_hits += 1
    print delta, "|", 4.0 * n_hits / float(n_trials)

