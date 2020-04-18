import matplotlib.pyplot as plt

def draw_beam_axis(z_min=-25000, z_max=25000, color='black', **kwargs):
    plt.gca(projection='3d').plot([0, 0], [0, 0], [z_min, z_max], color=color, **kwargs)
