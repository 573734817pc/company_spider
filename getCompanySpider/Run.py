from spiderLib import Main

url = 'https://www.banban.cn/gupiao/list_sh.html'
get_rule = '<li>.*?<a href="/gupiao/\d.*?">([\u4e00-\u9fa5]+).*?</a>'
obj = Main.Main(url, get_rule)
res = obj.main()
str_res = ",".join(res)

f = open('../companyName.txt', 'w')
f.write(str_res)
f.close()

