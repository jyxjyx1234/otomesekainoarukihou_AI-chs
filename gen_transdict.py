from gen_transdict_LIB import *

a = transdict()

#a.addname(jp_name=[],chs_name=[],sex="",role="",other="",reverse=False)

a.addname(jp_name=["片桐 ユイ"],chs_name=["片桐 唯"],sex="man",role="",other="",reverse=False)
a.addname(jp_name=["姬乃 アカリ"],chs_name=["姬乃 朱莉"],sex="woman",role="",other="",reverse=False)
a.addname(jp_name=["藤堂 リン"],chs_name=["藤堂 凛"],sex="woman",role="",other="",reverse=False)
a.addname(jp_name=["片桐 ヤエカ"],chs_name=["片桐 八重香"],sex="woman",role="sister of ユイ",other="",reverse=False)
a.addname(jp_name=["守屋 ミク"],chs_name=["守屋 美空"],sex="woman",role="",other="",reverse=False)
a.addname(jp_name=["佐伯 ルリコ"],chs_name=["佐伯 琉璃子"],sex="woman",role="",other="",reverse=False)
a.addname(jp_name=["本多 マユミ"],chs_name=["本多 真由美"],sex="woman",role="teacher",other="",reverse=False)
a.addname(jp_name=["ユミちゃん"],chs_name=["由美酱"],sex="woman",role="nickname of 真由美",other="",reverse=False)
a.addname(jp_name=["水野 ダイチ"],chs_name=["水野 戴奇"],sex="woman",role="",other="",reverse=False)
a.addname(jp_name=["姬乃 サキ"],chs_name=["姬乃 萨奇"],sex="woman",role="mother of アカリ",other="",reverse=False)
a.addname(jp_name=["リネット"],chs_name=["蕾妮特"],sex="",role="",other="",reverse=False)
a.addname(jp_name=["カピバラ"],chs_name=["卡皮瓦拉"],sex="",role="",other="",reverse=False)
a.addname(jp_name=["シレイ"],chs_name=["希瑞"],sex="",role="",other="",reverse=False)
a.addname(jp_name=["ユイト"],chs_name=["唯人"],sex="man",role="",other="",reverse=False)
a.addname(jp_name=["佐伯 カナエ"],chs_name=["佐伯 加奈"],sex="woman",role="",other="",reverse=False)



a.gen_dict()
a.savetxt("项目GPT字典.txt")
a.savejson("temp.json")

n = open_json("temp.json")
nd = open_json("namedict.json")
for i in nd:
    if i in n:
        nd[i] = n[i]
    nd[i] = nd[i].replace("浄化委員", "净化委员").replace("浄化委員", "净化委员").replace("達", "们").replace("員", "员").replace("隊", "队").replace("議", "议")
    if "＆" in nd[i]:
        _ = nd[i].split("＆")
        _ = [n.get(__,__) for __ in _]
        nd[i] = "＆".join(_)
save_json("namedict.json",nd)
