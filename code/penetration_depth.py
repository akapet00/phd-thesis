import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from misc import load_tissue_properties
from misc import reflection_coefficient
from misc import update_rc


def main():
    f = np.array([1, 2, 5, 10, 20, 50, 100]) * 1e9  # frequency in Hz
    _, eps_r, _, penetration_depth = np.vectorize(  # power penetration depth
        load_tissue_properties
        )('skin_dry', f)
    gamma = reflection_coefficient(eps_r)
    T_tr = 1 - gamma ** 2  # power transmission coefficient

    # visualize
    update_rc()
    cs = sns.color_palette('rocket', 2)
    fig, ax1 = plt.subplots()
    ax1.plot(f / 1e9, penetration_depth * 1000, 'o-', c=cs[0], lw=3,
             label='penetration\ndepth')
    ax1.tick_params(axis='y', labelcolor=cs[0])
    ax1.set(
        xscale='log',
        xlabel='frequency (GHz)',
        ylabel='power penetration depth (mm)',
        yticks=[0, 25, 50],
        yticklabels=[0, 25, 50],
        )
    ax1.legend(loc='upper left', frameon=False)
    ax2 = ax1.twinx()
    ax2.plot(f / 1e9, np.abs(T_tr), '^--', c=cs[1], lw=3,
            label='transmission\ncoefficient')
    ax2.tick_params(axis='y', labelcolor=cs[1])
    ax2.set(
        xscale='log',
        ylabel='power transmission coefficient',
        xticks=[1, 10, 100],
        xticklabels=[1, 10, 100],
        yticks=[0.4, 0.7, 1],
        yticklabels=[0.4, 0.7, 1],
        ylim=[0.385, 1]
        )
    ax2.legend(loc='upper right', frameon=False)
    fig.tight_layout()
    sns.despine(right=False)
    plt.show()
    # fig.savefig(os.path.join('figures', 'penetration_depth.pdf'),
    #             bbox_inches='tight')


if __name__ == '__main__':
    main()
