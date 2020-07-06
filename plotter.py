import numpy as np
import matplotlib.pyplot as plt


def plot(x_y_data, title='', xlabel='x', ylabel='y', xtics=1, filename='.res.png'):
    """
    A simple plotter
    """
    
    plt.scatter(x_y_data[:, 0], x_y_data[:,1])
    # making title
    plt.title(title)
    
    # making labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # making ticks
    xmin = np.min(x_y_data[:, 0])
    xmax = np.max(x_y_data[:, 0])
    all_x_ticks = np.linspace(
        start=xmin,
        stop=xmax,
        num=int((xmax-xmin)/xtics) + 1
    )
    plt.xticks(all_x_ticks)
    plt.savefig(filename)
    plt.show()
