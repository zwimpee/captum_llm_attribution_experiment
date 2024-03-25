import matplotlib.pyplot as plt
from contextlib import contextmanager

@contextmanager
def redirected_plot_save(file_path, format='png'):
    """
    Context manager that redirects plt.show() to plt.savefig().
    
    Args:
        file_path (str): The path to save the plot file.
        format (str): Format of the saved plot file.
    """
    original_show = plt.show
    def savefig_show(*args, **kwargs):
        plt.savefig(file_path, format=format)
        plt.close()
    plt.show = savefig_show
    try:
        yield
    finally:
        plt.show = original_show


