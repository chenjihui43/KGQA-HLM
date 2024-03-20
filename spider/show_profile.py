import json

with open('/Users/chenjihui/Desktop/PycharmProjects/KGQA_HLM/spider/json/data.json', encoding='utf-8') as f:
    data = json.load(f)


def get_profile(name):
    s = ''
    for i in data[name]:
        st = "<dt class = \"basicInfo-item name\" >" + str(i) + " \
        <dd class = \"basicInfo-item value\" >" + str(data[name][i]) + "</dd >"
        s += st
    return s


def test():
    s = get_profile("林黛玉")
    print(s)


if __name__ == '__main__':
    test()
