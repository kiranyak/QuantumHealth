import os
import importlib

os.system("conda install pywin32")
installs = {
    'notebook': ['pip install notebook'],
    'plotly' : ['pip install plotly'],
    'qiskit' : ['pip install qiskit'],
    'ipywidgets': ['pip install ipywidgets']
}



for lib in installs:
    spec = importlib.util.find_spec(lib)
    if(spec is None):
        for p in installs[lib]:
            os.system(p)

os.system("pip install jupyter_contrib_nbextensions")
os.system("jupyter contrib nbextension install --user")
os.system("jupyter nbextension enable codefolding/main")
os.system("jupyter nbextension enable toc2/main")
os.system("jupyter nbextension enable runtools/main")
os.system("jupyter nbextension enable execute_time/ExecuteTime")