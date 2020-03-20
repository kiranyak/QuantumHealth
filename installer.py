import os


installs = {
    'notebook': [
        'pip install notebook',
        'pip install jupyter_contrib_nbextensions',
        'jupyter contrib nbextension install --user',
        'jupyter nbextension enable codefolding/main',
        'conda install pywin32'
    ],
    'plotly' : ['pip install plotly'],
    'qiskit' : ['pip install qiskit']
}


for lib in installs:
    try:
        exec("import " +  lib)
        print(lib +" " + "is installed")
    except:
        for p in installs[lib]:
            os.system(p)
