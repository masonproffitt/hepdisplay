import numpy as np
import matplotlib.pyplot as plt

from .util import Arrow3D

def draw_beam_axis(z_min=-25000, z_max=25000, color='black', **kwargs):
    plt.gca(projection='3d').plot([0, 0], [0, 0], [z_min, z_max], color=color, **kwargs)

def draw_cylinder(radius, z_min=-25000, z_max=25000, longitudinal_sections=36, transverse_sections=10, alpha=0.25, **kwargs):
    phi = np.linspace(0, 2 * np.pi, longitudinal_sections + 1)
    z = np.linspace(z_min, z_max, transverse_sections + 1)
    phi_grid, z_grid = np.meshgrid(phi, z)
    x_grid = radius * np.cos(phi_grid)
    y_grid = radius * np.sin(phi_grid)
    plt.gca(projection='3d').plot_wireframe(x_grid, y_grid, z_grid, alpha=alpha, **kwargs)

def draw_arrow(xs, ys, zs, lw=1.5, mutation_scale=10, arrowstyle='-|>', **kwargs):
    arrow = Arrow3D(xs, ys, zs, lw=lw, mutation_scale=mutation_scale, arrowstyle=arrowstyle, **kwargs)
    plt.gca(projection='3d').add_artist(arrow)
