import seaborn as sns


def update_rc():
    """Run and configure visualization parameters."""
    sns.set(style='ticks',
            font='serif',
            font_scale=1.25,
            rc={'lines.linewidth': 3,
                'lines.markersize': 10,
                'text.usetex': True,
                'text.latex.preamble': '\\usepackage{amsmath}',
                'font.family': 'serif'})
