import os,sys
from distutils.dir_util import copy_tree
import numpy as np
import subprocess

from utils.ObjDict import read_from_file_python2
from utils.mkdir_p import mkdir_p

cfg = read_from_file_python2(sys.argv[1])
for key in cfg.param_dict:
    exec(key+" = cfg.param_dict."+key)

mkdir_p(out_mg_dir)
for _ in range(n_dir):
    
    n = np.random.rand()
    param = param_low + n * (param_high-param_low)
    seed = np.random.randint(seed_low,seed_high)
    
    out_dir = os.path.join(out_mg_dir,"_".join([str(param),str(seed)])+"/")
    
    print("Copying directory as param, seed "+str(param),str(seed))

    copy_tree(template_dir,out_dir)
    subprocess.call(["sed", "-i", "-e",  's/'+param_name+'/'+str(param)+'/g', os.path.join(out_dir,"Cards/param_card.dat")])
    subprocess.call(["sed", "-i", "-e",  's/'+seed_name+'/'+str(seed)+'/g', os.path.join(out_dir,"Cards/run_card.dat")])
    subprocess.call(["sed", "-i", "-e",  's/RUNEVENT/'+str(n_evt)+'/g', os.path.join(out_dir,"Cards/run_card.dat")])
