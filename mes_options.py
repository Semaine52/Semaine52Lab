#IPYTHON  INTERACTIVESHELL
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all" 

#IPYTHON DISPLAY
from IPython.display import HTML
    
# PANDAS
import pandas as pd
pd.set_option('display.notebook_repr_html', True)
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 5000)
