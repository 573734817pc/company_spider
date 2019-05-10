from spiderLib import Main
#澎湃新闻
# #定义爬取的url
url_pengpai = 'https://www.thepaper.cn/load_index.jsp?nodeids=25434,25436,25433,25438,25435,25437,27234,25485,25432,37978,&topCids=,3420378,3419837,3418451&pageidx='
#定义爬取规则1
rule1_pengpai = '<img.*?src="(.*?)".*?>.*?<h2>.*?href="(.*?)".*?>(.*?)</a>.*?</h2>.*?<p>(.*?)</p>.*?<div class="pdtt_trbs">.*?<a.*?>(.*?)</a>.*?<span>(.*?)</span>'
#定义爬取规则2
rule2_pengpai = '<div class="news_about">.*?</p>.*?<p>.*?([\d-]+\s+[\d:]+).*?<span>'
#定义pageid
pageid_pengpai = 1
#调用Main类中的Main方法
obj = Main.Main(url_pengpai, rule1_pengpai, rule2_pengpai, pageid_pengpai)
obj.main_pengpai()

# 中国经济网
# #定义爬取的url
# url = 'http://finance.ce.cn/rolling/index.shtml'
# # 定义爬取规则1
# rule1 = '<td height="28".*?href="(.*?)".*?\[(.*?)\].*?</td>'
# #定义爬取规则2
# rule2 = '<h1 id="articleTitle">(.*?)</h1>.*?<span id="articleSource">来源：(.*?)</span>.*?<div class="content" id="articleText">.*?><p.*?>(.*?)</p>'
# #定义pageid
# pageid = 2
# #调用Main类中的Main方法
# obj = Main.Main(url, rule1, rule2, pageid)
# obj.main_zgjj()

#中国科技网
#定义爬取的url
# url = 'http://www.stdaily.com/cxzg80/kejizixun/kejizixun'
# # 定义爬取规则1
# rule1 = '<dl>.*?<h3>.*?>(.*?)</a>.*?<dd>.*?<p>(.*?)</p>.*?"sp_1">(.*?)</span>'
# #定义爬取规则2
# rule2 = ''
# #定义pageid
# pageid = 3
# #调用Main类中的Main方法
# obj = Main.Main(url, rule1, rule2, pageid)
# obj.main_zgkj()

#人民网
#定义爬取的url
# url = 'http://finance.people.com.cn/GB/70846/index.html'
# # 定义爬取规则1
# rule1 = "<li>.*?<a href='(.*?)'.*?>.*?</li>"
# #定义爬取规则2
# rule2 = 'text_title">.*?<h1>(.*?)</h1>.*?"fl">.*?([\d]+).*?([\d]+).*?([\d]+).*?([\d]+).*?([\d]+).*?"_blank">(.*?)</a>.*?<div class="box_pic"></div>(.*?)<div class="box_pic"></div>'
# #定义pageid
# pageid = 4
# #调用Main类中的Main方法
# obj = Main.Main(url, rule1, rule2, pageid)
# obj.main_rmw()
