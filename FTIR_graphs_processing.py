import numpy as np
import matplotlib.pyplot as plt
import os

data_path = r".\FTIR_source_data"

# idx_to_skip = [0, 2, 4, 6, 8]       # index of files to skip
# idx_to_plot = [1, 3, 5, 7, 9]       # index of files to plot
idx_to_plot = [1, 5, 7, 9]

plt.close()
plt.figure(figsize=(7, 5), tight_layout=True, dpi=250)

for i, file_name in enumerate(os.listdir(data_path)):

    print(f"Processing file with index {i} | series name: {file_name}", end='')

    f = open(data_path + '\\' + file_name)
    data_lst_temp = [item[:-1].replace(',', '.').split(';') for item in f.readlines()[2:]]

    data = []
    for pair in data_lst_temp:
        data.append([float(pair[0]), float(pair[1])])
    data = np.array(data)

    if i in idx_to_plot:
        plt.plot(data[:,0], data[:,1])#, label=)
        print("             [PLOTTED]")
    else:
        print("             [SKIPPED]")

plt.grid()
# plt.ylim([0, 120])
# plt.yticks(np.linspace(0, 120, 13))
plt.ylim([50, 120])
plt.yticks(np.linspace(50, 120, 8))


plt.xlim([600, 4000])
plt.xticks(np.linspace(600, 4000, 9))

plt.xlabel("Wavenumber $[cm^{-1}]$")
plt.ylabel("Transmittance $[\%]$")

# plt.legend(["Natural Hematite (1) [AEFE01]", "Natural Hematite (2) [AEFE01]"])
# plt.legend(["Industrial Silicon Oxide (1) [AEQ02]", "Industrial Silicon Oxide (2) [AEQ02]"])
# plt.legend(["Magnetite (1) [AEFE02]", "Magnetite (2) [AEFE02]"])
# plt.legend(["Natural Quartz (1) [AEQ01]", "Natural Quartz (2) [AEQ01]"])
# plt.legend(["Mars Analogue (1) [AEMA01]", "Mars Analogue (2) [AEMA01]"])
plt.legend(["Hematite", "Mars Analogue", "Natural Quartz", "Industrial Quartz"])

plt.gca().invert_xaxis()

plt.savefig(".\FTIR_all_samples.png")

plt.show()

    # pass
