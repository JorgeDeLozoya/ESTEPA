import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import StringIO
from qbstyles import mpl_style
from matplotlib.colors import LinearSegmentedColormap

data_str = StringIO(''' WAFER    0   1   2   3   4   5   6   7   8   9   10
                            11    0   0   0   2   2   2   2   2   0   0  0
                            10    0   0   2   3   4   6   5   2   2   0  0
                            9    0   2   4   2   7   4   6   4   2   2  0
                            8    0   5   7   3   2   3   6   5   2   2  0
                            7    2   4   2   8   9   2   2   2   2   2  2   
                            6    2   6   8   7   6   6   4   5   2   2  2
                            5    3   2   9   5   6   6   6   3   2   2  2   
                            4    2   2   2   2   4   4   2   2   2   2  2
                            3    0   2   2   2   7   5   2   3   4   2  0
                            2    0   2   2   2   2   2   4   2   2   2  0
                            1    0   0   2   2   2   2   3   2   2   0  0
                            0    0   0   0   2   2   2   2   2   0   0  0''')

mpl_style(dark=True)
df = pd.read_csv(data_str, delim_whitespace=True)
df.set_index('WAFER', inplace=True)
values = df.to_numpy(dtype=float)
# ax = sns.heatmap(values, cmap='Blues', vmin=0, vmax=15, linewidth=5, linecolor = "black", square=True)
# sns.heatmap(values, xticklabels=df.columns, yticklabels=df.index,
#             cmap=plt.get_cmap('binary'), vmin=0, vmax=2, mask=values > 0, cbar=False, ax=ax)

cmap_reds = plt.get_cmap('Greens')      #escala de colors dels quadrats
num_colors = 15
colors = ['#0C1C23', 'White'] + [cmap_reds(i / num_colors) for i in range(2, num_colors)]   #Colors de les posicions de valor 0: No hi ha wafer, 1: Valor nul
cmap = LinearSegmentedColormap.from_list('', colors, num_colors)
ax = sns.heatmap(df, cmap=cmap, vmin=0, vmax=num_colors, linewidth=5, linecolor = "#0C1C23", square=True, cbar=False)
cbar = plt.colorbar(ax.collections[0], ticks=range(num_colors + 1))
plt.show()








# 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 
# 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 
# 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'P, 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 
# 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 
# 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'crest', 'crest_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'flare', 'flare_r', 'gist_earth', 
# 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 
# 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 
# 'magma', 'magma_r', 'mako', 'mako_r', 'nipy_spectral', ' 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 
# 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag', 'vlag_r', 'winter', 'winter_r'
