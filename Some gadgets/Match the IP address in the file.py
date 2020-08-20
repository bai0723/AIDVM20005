import re

def find_ip(port):
    f = open('exc.txt','r')
    while True:
        data =""
        for line in f:
            if line == "\n":
                break
            data += line
        if not data:
            return "没有找到该端口"
        obj = re.match(r'\S+',data)
        if port == obj.group():
            pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'#匹配虚拟接口
            pattern1 = r'[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2}|Unknown'
            obj = re.search(pattern1,data)
            if obj:
                return obj.group()


if __name__ == '__main__':
    while True:
        port = input("请输入端口号")
        print(find_ip(port))