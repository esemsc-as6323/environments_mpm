import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter
from scipy import misc

__all__ = ['rand_array', 'smooth_image', 'my_mat_solver', 'my_panda_solver']

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def rand_array(shape):
    return np.random.rand(*shape)

def my_mat_solver(A,b):
    return A.inv()*b

def my_panda_solver():
    return pd.Series([1,3,5,np.nan,6,8])
