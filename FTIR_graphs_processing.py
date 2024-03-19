import numpy as np
import matplotlib.pyplot as plt
import os

data_path = r".\FTIR_source_data"

idx_to_skip = [0, 2, 4, 6, 8]       # index of files to skip
plt.close()

for i, file_name in enumerate(os.listdir(data_path)):

    print(f"Processing file with index {i} | series name: {file_name}", end='')

    f = open(data_path + '\\' + file_name)
    data_lst_temp = [item[:-1].replace(',', '.').split(';') for item in f.readlines()[2:]]

    data = []
    for pair in data_lst_temp:
        data.append([float(pair[0]), float(pair[1])])
    data = np.array(data)

    if not i in idx_to_skip:
        plt.plot(data[:,0], data[:,1], label=file_name)
        print("             [PLOTTED]")
    else:
        print("             [SKIPPED]")

plt.grid()
plt.xlabel("Wavenumber $[cm^{-1}]$")
plt.ylabel("Reflectance $[-]$")
plt.legend()
plt.gca().invert_xaxis()

plt.savefig(".\FTIR_all_samples.png")

plt.show()

    # pass
