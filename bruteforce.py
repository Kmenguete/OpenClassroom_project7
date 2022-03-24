import pandas as pd

# Visualization Imports

import matplotlib.pyplot as plt
import seaborn as sn
import plotly.graph_objs as go
import plotly.offline as py
import plotly.tools as tls
import plotly.express as px
import numpy as np
from tqdm.autonotebook import get_ipython

shares_dataframe1 = pd.read_csv('dataset1_Python+P7.csv')

color = sn.color_palette()

get_ipython().run_line_magic('matplotlib', 'inline')

py.init_notebook_mode(connected=True)
