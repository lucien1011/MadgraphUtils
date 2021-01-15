import os,sys
from distutils.dir_util import copy_tree
import numpy as np
import subprocess

from utils.ObjDict import read_from_file_python2

cfg = read_from_file_python2(sys.argv[1])
for key in cfg.param_dict:
    exec(key+" = cfg.param_dict."+key)

for n in np.random.rand(n_dir):
    param = param_low + n * (param_high-param_low)
    param_dir = os.path.join(out_mg_dir,str(param)+"/")
    print("Copying directory as param "+str(param))
    copy_tree(template_dir,param_dir)
    subprocess.call(["sed", "-i", "-e",  's/'+param_name+'/'+str(param)+'/g', os.path.join(param_dir,"Cards/param_card.dat")])
    subprocess.call(["sed", "-i", "-e",  's/RUNEVENT/'+str(n_evt)+'/g', os.path.join(param_dir,"Cards/run_card.dat")])
