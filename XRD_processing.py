import os
import matplotlib.pyplot as plt
import numpy as np

data_path = r".\XRD_source_data"

for i, file_name in enumerate(os.listdir(data_path)):
    if file_name[-1] == 'c':
        f = open(data_path + "\\" + file_name)
        raw_data = f.readlines()[78:-3]
        # data = [item[:-1].split(',') for item in raw_data]
        data = []
        for row in raw_data:
            row_data = row[:-1].split(',')
            for item in row_data:
                data.append(float(item))

        pass

        plt.plot(np.linspace(10, 90, len(data)), data, label=file_name)
        # plt.show()

plt.xlabel("Angle $2\\theta$ $[\deg]$")
plt.ylabel("Counts [-]")
plt.legend()
plt.grid()

plt.savefig(".\XRD_all_samples.png")
plt.show()
