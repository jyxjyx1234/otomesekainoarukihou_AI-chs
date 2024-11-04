import os
import shutil
os.makedirs("patch", exist_ok=True)
for file in os.listdir("scn_trans"):
    src = os.path.join("scn_trans", file)
    dst = os.path.join("patch", file)
    if os.path.isfile(src):
        os.system(f'copy "{src}" "{dst}" >nul 2>&1')
'''
for file in os.listdir("transgrp"):
    src = os.path.join("transgrp", file)
    dst = os.path.join("patch", file)
    if os.path.isfile(src):
        os.system(f'copy "{src}" "{dst}" >nul 2>&1')
'''
os.system("arc_pack xp3 patch release/unencrypted.xp3")
shutil.rmtree("patch")