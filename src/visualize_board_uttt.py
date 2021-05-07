#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib.table import Table
import pandas as pd
import numpy as np



def view_board(np_data, fmt='{:s}', bkg_colors=['pink', 'pink']):
    """
    Remember to add a '-' sign to the cell that is the old move
    leading to the current state;
    :param np_data: numpy array of shape (9,9)
    :param fmt: format of the data
    :param bkg_colors: originally used for chess board with intermittent colors
    :return:
    """
    data = pd.DataFrame(np_data, columns=['0','1','2','3','4','5','6','7','8'])
    fig, ax = plt.subplots(figsize=[9,9])
    ax.set_axis_off()
    tb = Table(ax, bbox=[0,0,1,1])
    nrows, ncols = data.shape
    width, height = 1.0 / ncols, 1.0 / nrows

    for (i,j), val in np.ndenumerate(data):
        idx = [j % 2, (j + 1) % 2][i % 2]
        color = bkg_colors[idx]

        tb.add_cell(i, j, width, height, text=fmt.format(val), 
                    loc='center', facecolor=color)

    for i, label in enumerate(data.index):
        tb.add_cell(i, -1, width, height, text=label, loc='right', 
                    edgecolor='none', facecolor='none')

    for j, label in enumerate(data.columns):
        tb.add_cell(-1, j, width, height/2, text=label, loc='center', 
                           edgecolor='none', facecolor='none')
    tb.set_fontsize(24)
    ax.add_table(tb)
    return fig