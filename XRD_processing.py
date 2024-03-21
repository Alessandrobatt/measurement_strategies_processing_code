import os
import matplotlib.pyplot as plt
import numpy as np

data_path = r".\XRD_source_data"

plt.close()
plt.figure(figsize=(7, 5), tight_layout=True, dpi=250)

# idx_to_plot = [1, 4, 7]
idx_to_plot = [1,4,7]

for i, file_name in enumerate(os.listdir(data_path)):
    if file_name[-1] == 'c':

        print(f"Processing file with index {i} | series name: {file_name}", end='')

        f = open(data_path + "\\" + file_name)
        raw_data = f.readlines()[78:-3]
        # data = [item[:-1].split(',') for item in raw_data]
        data = []
        for row in raw_data:
            row_data = row[:-1].split(',')
            for item in row_data:
                data.append(float(item))

        pass

        if i in idx_to_plot:
            plt.plot(np.linspace(10, 90, len(data)), data, linewidth=0.75, label=file_name)
            print("             [PLOTTED]")
        else:
            print("             [SKIPPED]")


plt.xlim([10, 90])
plt.ylim([0, 1800])
plt.xticks(np.linspace(10, 90, 17))
plt.yticks(np.linspace(0, 1800, 19))
plt.xlabel("Angle $2\\theta$ $[\deg]$")
plt.ylabel("Counts [-]")
plt.legend()
plt.grid()

plt.savefig(".\XRD_all_samples.png")
plt.show()
