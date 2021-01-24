# coding=utf-8
import json
f = open("./data/tzc.json", "r", encoding="utf-8")
data=json.loads(f.read()).get("data").get("question_list")
f.close()
for i in range(0,len(data)):
    
    opt = data[i].get("option_list")
    for ii in range(0, len(opt)):
        if (str(opt[ii].get("optionid")) == data[i].get("user_answer_optionid")):
            print(str(i)+"\t"+str(data[i].get("questionid"))+"\t"+data[i].get("question_title")+"\t"+opt[ii].get("title"))
            break