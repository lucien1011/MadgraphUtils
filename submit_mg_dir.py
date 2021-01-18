import os,sys

from utils.ObjDict import read_from_file_python2

cfg = read_from_file_python2(sys.argv[1])
in_dir = cfg.param_dict.out_mg_dir
run_name = cfg.param_dict.mg_run_name
slurm_script_name = cfg.param_dict.mg_slurm_script_name

def submit(work_dir,run_name,slurm_script_name,job_name,):
    from SLURMWorker.SLURMWorker import SLURMWorker
    
    commands = """
cd {work_dir}
source setup.sh
./bin/generate_events {run_name} -f
cd Events/{run_name}
gzip -d tag_1_pythia_events.hep.gz
    """.format(
            work_dir=work_dir,
            run_name=run_name,
            )
    
    script_file_name = os.path.join(work_dir,slurm_script_name)
    
    worker = SLURMWorker()
    worker.make_sbatch_script(
            script_file_name,
            job_name,
            "kin.ho.lo@cern.ch",
            "4",
            "4gb",
            "06:00:00",
            os.path.join(work_dir,job_name),
            commands,
            )
    worker.sbatch_submit(script_file_name)

if __name__ == "__main__":
    for d in os.listdir(in_dir):
        mass_dir = os.path.join(in_dir,d)
        submit(mass_dir,run_name,slurm_script_name,d)
    
