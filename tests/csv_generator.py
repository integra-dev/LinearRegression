import pandas
import numpy as np

N_ROWS =30

# XY = np.array(np.random.uniform(0.0, 1.0, N_ROWS), np.random.uniform(0.0, 1.0, N_ROWS))
Y = np.round(np.random.rand(N_ROWS, 2), 3)
np.savetxt('../csv_test/0_1_gen_3.csv', Y, delimiter=';', header='WSA;Flow', comments='')
