import os

#in_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Madgraph/201211_mg_dyll/"
in_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Madgraph/210112_mg_dyll/"
run_name = "run_01"
slurm_script_name = "slurm.sh"

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
            "1",
            "4gb",
            "03:00:00",
            "",
            commands,
            )
    worker.sbatch_submit(script_file_name)

if __name__ == "__main__":
    for d in os.listdir(in_dir):
        mass_dir = os.path.join(in_dir,d)
        submit(mass_dir,run_name,slurm_script_name,d)
    
