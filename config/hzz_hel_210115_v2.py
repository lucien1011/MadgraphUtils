from utils.ObjDict import ObjDict

param_dict = ObjDict(
        template_dir = "mg_hzz_hel_template",
        out_mg_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Madgraph/210115_mg_hzz_hel_v2/",
        n_dir = 100,
        n_evt = 100000,
        param_low = 0.,
        param_high = 0.2,
        param_name = 'CWWCOUPLING',

        mg_run_name = "run_01",
        mg_slurm_script_name = "slurm.sh",
        mg_job_name = "210115_mg_hzz_hel_delphes",
        
        out_delphes_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Delphes/210115_mg_hzz_hel_v2/",
        cmssw_dir = "/blue/avery/kinho.lo/Delphes/CMSSW_10_0_5/src/",
        delphes_dir = "/blue/avery/kinho.lo/Delphes/delphes/",
        delphes_job_name = "210115_mg_hzz_hel_delphes",

        out_litetree_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/LiteTree/210115_mg_hzz_hel_v2/",
        litetree_job_name = "210115_mg_hzz_hel_LiteTree",

        )
