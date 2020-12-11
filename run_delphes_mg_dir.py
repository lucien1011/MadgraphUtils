import os,glob,subprocess

# do cmsenv first

in_pattern = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Madgraph/201210_mg_dyll/*/Events/run_01/tag_1_pythia_events.hep"
delphes_dir = "/blue/avery/kinho.lo/Delphes/delphes/"
out_dir = "/cmsuf/data/store/user/t2/users/klo/MLHEP/Delphes/201210_mg_dyll/"

for f in glob.glob(in_pattern):
    mass_str = f.split("/")[-4]
    subprocess.call([
            os.path.join(delphes_dir,"DelphesSTDHEP"),
            os.path.join(delphes_dir,"cards/delphes_card_CMS.tcl"),
            os.path.join(out_dir,mass_str+".root"),
            f,
            ])
