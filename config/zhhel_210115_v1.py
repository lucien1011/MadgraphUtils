from utils.ObjDict import ObjDict

param_dict = ObjDict(
        template_dir = "mg_zh_hel_template",
        out_mg_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Madgraph/210115_mg_zhhel/",
        n_dir = 5,
        n_evt = 1000,
        param_low = 0.,
        param_high = 0.2,
        param_name = 'CWWCOUPLING',

        mg_run_name = "run_01",
        mg_slurm_script_name = "slurm.sh",
        
        out_delphes_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Delphes/210115_mg_zhhel/",
        cmssw_dir = "/blue/avery/kinho.lo/Delphes/CMSSW_10_0_5/src/",
        delphes_dir = "/blue/avery/kinho.lo/Delphes/delphes/",
        delphes_job_name = "210115_mg_zhhel_delphes"

        )
