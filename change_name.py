from Lib import *

def change_name(text):
    text = text.replace('唯', '结')
    text = text.replace('朱莉', '灯里')
    text = text.replace('八重香', '八重花')
    text = text.replace('美空', '美玖')
    return text

oripath = "gt_output/"
newpath = "gt_output_new/"
os.makedirs(newpath, exist_ok=True)

for file in os.listdir(oripath):
    ori = open_json(oripath + file)
    for i in ori:
        i["message"] = change_name(i["message"])
    save_json(newpath + file, ori)


ori = open_json("names.json")
for i in ori:
    ori[i] = change_name(ori[i])
save_json("names_.json", ori)