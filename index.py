
# import sys
# from IPython.terminal.ipapp import launch_new_instance
# from socket import gethostname
# import warnings
# import os


# warnings.filterwarnings("ignore", module = "zmq.*")
# sys.argv.append("notebook")
# sys.argv.append("--IPKernelApp.pylab='inline'")
# sys.argv.append("--NotebookApp.ip=" + gethostname())
# sys.argv.append("--NotebookApp.open_browser=True")
# sys.argv.append("--NotebookApp.file_to_run="+ "plotter.ipynb")
# launch_new_instance()


import os
from socket import gethostname

cmds  = 'jupyter notebook ' 
cmds += '--NotebookApp.ip='  + gethostname()+ " "
cmds += "--NotebookApp.open_browser=True " 
cmds += "--NotebookApp.file_to_run=" + "plotter.ipynb"

os.system(cmds)
