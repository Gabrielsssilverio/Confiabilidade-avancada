import numpy as np

def eq1(samples=None):
    g = np.zeros(samples.shape[0])
    for i in range(samples.shape[0]):
        g[i] = (samples[i, 0] * samples[i, 1]) - samples[i, 2]
    return g