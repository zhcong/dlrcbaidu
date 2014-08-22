#coding=UTF-8
'''
This is a simple scirpt. you can download lyric form baidu.com. The lyric belong
to www.baidu.com. You can use this scirpt anywhere. This scirpt is follow the BSD License. And this is my email: 
1011.0011@163.com. 2014/2/20
'''
import sys
import os
import os.path
import re
import urllib
import urllib2


#到百度mp3查找歌词并返回lrc地址
#get the url of lyric from music.baidu.com
def get_url(name):
	open_url = "http://music.baidu.com/search/lrc?key="+urllib.quote(name)
	htmlpaper = urllib2.urlopen(open_url).read()
	htmlurl = re.search('down-lrc-btn.{.*}',htmlpaper)
	if htmlurl:
		return 'http://music.baidu.com'+htmlurl.group().split("'")[3]
	else:
		print name+'查找失败！'
		return False

#列出文件夹的歌曲名称
#list the name of your music file
def find_file(path):
	file_list=os.listdir(path)
	a=[]
	for i in file_list:
		if(os.path.isfile(path+'/'+i)):
			a.append(i.split('.')[0])
	return a

#创建存放歌词的文件夹，在文件
#create a folder to save your lyric file
def make_dir(path):
	try:
		os.makedirs(path+"/lrc")
	except:
		print path+'lrc'+'目录重复','，请删除'
#根据地址下载lrc文件
#download the lyric file
def download(url,name,path):
	print '正在下载'+name+'，请耐心等候。。'
	urllib.urlretrieve(url,path+'/'+name+'.lrc')
	print '下载'+name+'完成'
	print " "
#main function
def function():
	path=raw_input('请输入歌曲所在目录:\n')
	make_dir(path)
	print '创建lrc文件夹成功！'
	filelist = find_file(path)
	for i in filelist:
		if(i!=''):
			url=get_url(i)
			download(url,i,path+'/lrc')

	print '''=================================================
	所有下载完毕'''


if __name__ == "__main__":
	function();

