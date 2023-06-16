import os

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(12346789)
import seaborn as sns

from misc import update_rc
from misc import pca


def generate_random_points(N=100, slope=(0.5, 0.), extent=2, noise=1.5):
    """Return a randomly distributed point cloud generated around the
    target point.
    
    Parameters
    ----------
    N : int, optional
        Number of points in the point cloud.
    slope : tuple, optional
        Slope of the x- and y-component of the point cloud.
    extent : number, optional
        Limits for x- and y-axis.
    noise : number, optional
        Additional noise.
    
    Returns
    -------
    tuple
        Array of points and the target point.
    """
    slope_x, slope_y = slope
    x_target = 0
    y_target = 0
    z_target = slope_x * x_target + slope_y * y_target
    target = (0, 0, z_target)
    x = np.random.normal(loc=x_target, scale=extent, size=N)
    y = np.random.normal(loc=y_target, scale=extent, size=N)
    z = slope_x * x + slope_y * y + np.random.normal(scale=noise, size=x.size)
    points = np.c_[x, y, z]
    return points, target


def main():
    # noisy data sampled on 2D plane in 3D space
    slope = (0.5, 0)
    points, target = generate_random_points(slope=slope)
    evec, evalue = pca(points)
    n = evec[:, np.argmin(evalue)]
    b = evec[:, 0]
    t = evec[:, 1]

    # clean counterpart to above
    xs = np.linspace(points[:, 0].min(), points[:, 0].max(), 33)
    ys = np.linspace(points[:, 1].min(), points[:, 1].max(), 33)
    X, Y = np.meshgrid(xs, ys)
    Z = slope[0] * X + slope[1] * Y

    # visualize
    update_rc()
    c = sns.color_palette('rocket', 1)
    fig = plt.figure(figsize=(4, 4))
    ax = plt.axes(projection ='3d')
    
    # noisy point cloud
    ax.scatter(*points.T,
               fc='w', ec='k', lw=1, rasterized=True,
               label='$nbhd(\\mathbf{x}_{i})$')
    ax.plot(*target, 'o',
            mfc=c[0], mec='k', mew=1, ms=5, zorder=5,
            label='$\\mathbf{x}_{i}$')
    
    # ground truth 2-D plane
    ax.plot_surface(X, Y, Z,
                    color='k', ec='none', alpha=0.1, rasterized=True)
    ax.text(x=xs.max(),
            y=ys.min(),
            z=slope[0] * xs.max() + slope[1] * ys.min(),
            s='$tp(\\mathbf{x}_{i})$')
    
    # unit normal vector
    ax.quiver(*target, *n,
              normalize=True, color='k', rasterized=True,
              lw=2, length=5, arrow_length_ratio=0.15)
    ax.text(x=n[0]-2,
            y=n[1],
            z=n[2]+3.5, 
            s='$\\mathbf{\\hat n}$')
    
    # binormal vector
    ax.quiver(*target, *b,
              normalize=True, color='k', rasterized=True,
              lw=2, length=5, arrow_length_ratio=0.15)
    ax.text(x=b[0]-7.5,
            y=b[1]-1.5,
            z=b[2]-0.5,
            s='$\\mathbf{\\hat b}$')
    
    # tangential vector
    ax.quiver(*target, *t,
              normalize=True, color='k', rasterized=True,
              lw=2, length=5, arrow_length_ratio=0.15)
    ax.text(x=t[0]-1,
            y=t[1]-4,
            z=t[2]-0.5,
            s='$\\mathbf{\\hat t}$')
    
    ax.legend(loc=1)
    ax.view_init(15, -135)
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()
    fig.tight_layout()
    plt.show()
    # fig.savefig(os.path.join('figures', 'normal_estimation.pdf'),
    #             dpi=300,
    #             bbox_inches='tight')


if __name__ == '__main__':
    main()
