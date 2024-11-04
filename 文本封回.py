import json
from Lib import *
import os
import re
import sys
import shutil

scnpath='scn_json\\'
outpath='scn_json_out\\'

filenames=os.listdir(scnpath)
for i in filenames:
    if 'resx' in i:
        filenames.remove(i)

def chuli(text):
    text = text.replace("%","％")
    return text

namedict = open_json("names_.json")
i=1
for file in filenames:
    percentage = round(i / len(filenames) * 100)
    print(f"\r进度: {i}/{len(filenames)}: ", "▓" * (percentage // 2), end="")
    sys.stdout.flush()

    json_file = open_json(scnpath+file)

    if "scenes" not in json_file:
        continue

    trans_file = open_json("gt_output_new\\"+file)
    
    for scene in json_file["scenes"]:
        if "texts" in scene:
            for text in scene["texts"]:
                #text[0] = namedict.get(text[0], text[0])
                if text[1] != None:
                    yiwen = trans_file.pop(0)["message"]
                    yiwen = chuli(yiwen)
                    if text[1][0][0]:
                        text[1][0][0] = namedict.get(text[1][0][0], text[1][0][0])
                    else:
                        text[1][0][0] = namedict.get(text[0], text[0])
                    text[1][0][1] = yiwen
                    text[1][0][2] = len(yiwen)
                    if len(text[1][0]) > 3:
                        text[1][0][3] = yiwen
                        text[1][0][4] = yiwen

    save_json(outpath + file, json_file)

    os.system(f'PsBuild.exe -p krkr {outpath+file} >nul 2>&1')
    file_=file.replace('.json','')
    os.system(f'ren {file_}.pure.scn.mdf {file_}.scn >nul 2>&1')
    os.system(f'move {file_}.scn scn_trans\\ >nul 2>&1')
    i+=1

