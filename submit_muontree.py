import os,glob

from SLURMWorker.SLURMWorker import SLURMWorker

# ______________________________________________________________________ ||
#input_file_pattern  = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Delphes/201210_mg_dyll/*.root"
#job_name            = "201210_mg_dyll_MuonTreeProducer"
#out_dir             = "/cmsuf/data/store/user/t2/users/klo/MLHEP/MuonTree/201210_mg_dyll/"

input_file_pattern  = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Delphes/210112_mg_dyll/*.root"
job_name            = "210112_mg_dyll_MuonTreeProducer"
out_dir             = "/cmsuf/data/store/user/t2/users/klo/MLHEP/MuonTree/210112_mg_dyll/"

cmssw_dir           = "/blue/avery/kinho.lo/Delphes/CMSSW_10_0_5/src/"
delphes_dir         = "/blue/avery/kinho.lo/Delphes/delphes/"

# ______________________________________________________________________ ||
input_file_list = [f for f in glob.glob(input_file_pattern)]
input_file_list.sort()
n_file = len(input_file_list)
for ijob,f in enumerate(input_file_list):
    each_job_name = job_name+"_"+str(ijob)
    out_file_name = os.path.basename(f)
    commands = "\n".join([
        "cd "+cmssw_dir,
        "eval `scramv1 runtime -sh`",
        "cd "+delphes_dir,
        "root -b -q \'MuonTreeProducer.C(\"{inputFile}\",\"{outputFile}\")\'".format(inputFile=f,outputFile=os.path.join(out_dir,out_file_name)),
        ],)
    script_file_name = os.path.join(out_dir,each_job_name+".cfg")
    worker = SLURMWorker()
    worker.make_sbatch_script(
        script_file_name,
        job_name,
        "kin.ho.lo@cern.ch",
        "1",
        "1gb",
        "01:00:00",
        os.path.join(out_dir,each_job_name),
        commands,
        )
    worker.sbatch_submit(script_file_name)
