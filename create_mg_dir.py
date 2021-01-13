import os
from distutils.dir_util import copy_tree
import numpy as np
import subprocess

template_dir = "mg_dyll_template/"
#out_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Madgraph/201211_mg_dyll/"
out_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Madgraph/210112_mg_dyll/"
n_dir = 99
n_evt = 100000
m_low = 85.
m_high = 95.

for n in np.random.rand(n_dir):
    m = m_low + n * (m_high-m_low)
    mass_dir = os.path.join(out_dir,str(m)+"/")
    print("Copying directory as mass "+str(m))
    copy_tree(template_dir,mass_dir)
    subprocess.call(["sed", "-i", "-e",  's/ZMASS/'+str(m)+'/g', os.path.join(mass_dir,"Cards/param_card.dat")])
    subprocess.call(["sed", "-i", "-e",  's/RUNEVENT/'+str(n_evt)+'/g', os.path.join(mass_dir,"Cards/run_card.dat")])
