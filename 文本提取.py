import json
import os
import re

scnpath='scn_json\\'
filenames=os.listdir(scnpath)
for i in filenames:
    if 'resx' in i:
        filenames.remove(i)

def pre_process(text):
    text = re.sub(r"%.*?;", "",text)
    return text


namedict={}
for file in filenames:
    out=[]
    json_file=open(scnpath+file,'r',encoding='utf8')
    json_file=json.load(json_file)

    if "scenes" not in json_file:
        continue
    scenes=json_file["scenes"]

    for scene in scenes:
        if 'texts' in scene:
            for text in scene['texts']:
                dic={}
                if text[0]!=None:
                    dic['name']=text[0]#这里是内部名
                if text[1]!=None:
                    if text[1][0][0] != None:#这里是显示名
                        dic['name']=text[1][0][0]
                    if len(text[1][0])>3:
                        dic['message']=pre_process(text[1][0][3])
                    else:
                        dic['message']=pre_process(text[1][0][1])
                out.append(dic)

        if 'selects' in scene:
            for select in scene['selects']:
                dic={}
                dic['id']=id
                dic['message']=pre_process(select['text'])
                out.append(dic)
                id+=1
    outfile=open('gt_input\\' + file, 'w', encoding='utf8')
    json.dump(out,outfile,ensure_ascii=False,indent=4)

    for i in out:
        if 'name' in i:
            namedict[i['name']]=i['name']

json.dump(namedict,open('namelist.json','w',encoding='utf8'),ensure_ascii=False,indent=4)  
