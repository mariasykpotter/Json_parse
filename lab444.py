import json


def func():
    f = open("kisc1.json", "r", encoding="utf-8")
    info = json.load(f)
    code = input()
    section = list(filter(lambda x: x["sectionCode"] == code, info["sections"]))
    dic = {}
    n = 0
    dic[code] = section[0]["sectionName"]
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    dic1 = {}
    for el in section:
        k = el["sectionName"]
        for e in el["groups"]:
            c = e["groupName"]
            lst5.append(c)
            dic3 = {"number of groupCode": len(el["groups"]), "groupName": lst5, "classes and groups": dic1}
            if n == 0:
                lst3.append(dic3)
            dic[k] = lst3
            p = e["classes"]
            lst4.append(len(p))
            dic1["number of classes"] = lst4
            lst1 = [a for a in range(len(e["classes"]))]
            for j in p:
                lst2.append(len(j["categories"]))
            for h in lst4:
                dic1["number of categories  of group" + str(len(lst4))] = lst2[:h]
            n += 1
        return dic


def save_file(dic):
    f1 = open("info.json", "w", encoding="utf-8")
    json.dump(dic, f1, ensure_ascii=False)


if __name__ == "__main__":
    save_file(func())
