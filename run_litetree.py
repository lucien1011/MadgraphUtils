import os,glob,sys

from SLURMWorker.SLURMWorker import SLURMWorker

from utils.ObjDict import read_from_file_python2
from utils.mkdir_p import mkdir_p

cfg = read_from_file_python2(sys.argv[1])
# ______________________________________________________________________ ||
input_file_pattern  = os.path.join(cfg.param_dict.out_delphes_dir,"*.root")
job_name            = cfg.param_dict.litetree_job_name 
out_dir             = cfg.param_dict.out_litetree_dir

cmssw_dir           = cfg.param_dict.cmssw_dir
delphes_dir         = cfg.param_dict.delphes_dir

script_name         = "LiteTreeProducer.C"

# ______________________________________________________________________ ||
input_file_list = [f for f in glob.glob(input_file_pattern)]
input_file_list.sort()
n_file = len(input_file_list)
mkdir_p(out_dir)
commands_list = [
    "cd "+cmssw_dir,
    "eval `scramv1 runtime -sh`",
    "cd "+delphes_dir,
    ]
for ijob,f in enumerate(input_file_list):
    out_file_name = os.path.basename(f)
    commands_list.append("root -b -q \'"+script_name+"(\"{inputFile}\",\"{outputFile}\")\'".format(inputFile=f,outputFile=os.path.join(out_dir,out_file_name)))
    
script_file_name = os.path.join(out_dir,job_name+".sh")
worker = SLURMWorker()
worker.make_sh_script(
    script_file_name,
    job_name,
    "\n".join(commands_list),
    )
#worker.sbatch_submit(script_file_name)
