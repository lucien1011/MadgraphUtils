from utils.ObjDict import ObjDict

param_dict = ObjDict(
        template_dir = "mg_zh_hel_template",
        out_mg_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Madgraph/210115_mg_zhhel/",
        n_dir = 1,
        n_evt = 1000,
        param_low = 0.,
        param_high = 0.2,
        param_name = 'CWWCOUPLING',
        
        out_delphes_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Delphes/210115_mg_zhhel/",

        )
