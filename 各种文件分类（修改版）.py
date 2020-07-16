print("|---写在前面---|")
print("|---所有目录中最好不要有同名文件---|")
print("|---分类完后请及时关闭pyhon---|\n")

import os
import shutil

temp = []
video = ['.avi', '.mpg', '.mpe', '.mpeg', '.asf', '.wmv', '.mov', '.qt', '.rm', '.mp4', '.flv', '.m4v', '.webm', '.ogv', '.ogg', '.mkv', '.ts', '.tsv']
music = ['.mp3', '.wav', '.wma', '.mpa', '.ram', '.ra', '.aac', '.aif', '.m4a', '.tsa', '.flac']
text = ['.doc', '.pdf', '.ppt', '.pps', '.docx', '.pptx', '.txt', '.pptx', '.xls', '.xlsx']
compress = ['.zip', '.rar', '.arj', '.gz', '.sit', '.sitx', '.sea', '.ace', '.bz2', '.7z']
image = ['.bmp', '.jpg', '.png', '.tif', '.gif', '.pcx', '.tga', '.exi', '.fpx', '.svg', '.psd', '.cdr', '.pcd', '.dxf', '.ufo', '.eps', '.ai', '.raw', '.WMF', '.webp', '.jpeg']

path = input("请输入当前想要实现文件归类的目录路径：")
path = path.replace("\\","\\\\")
#检测各个文件是否已存在

if "视频" not in os.listdir(path):
    os.mkdir(path+"\\"+"视频")
if "文档" not in os.listdir(path):
    os.mkdir(path+"\\"+"文档")
if "音频" not in os.listdir(path):
    os.mkdir(path+"\\"+"音频")
if "图片" not in os.listdir(path):
    os.mkdir(path+"\\"+"图片")
if "压缩文件" not in os.listdir(path):
    os.mkdir(path+"\\"+"压缩文件")
if "其他" not in os.listdir(path):
    os.mkdir(path+"\\"+"其他")
    
for each in os.walk(path):
    for every in each[2]:
        temp.append(each[0]+'\\'+every)

print("正在开始分类...")
for each in temp:
    txt = os.path.splitext(each)[1]
    if txt in video:
        shutil.move(each,path+"\\"+"视频")
    elif txt in music:
        shutil.move(each,path+"\\"+"音频")
    elif txt in text:
        shutil.move(each,path+"\\"+"文档")
    elif txt in compress:
        shutil.move(each,path+"\\"+"压缩文件")
    elif txt in image:
        shutil.move(each,path+"\\"+"图片")
    else:
        shutil.move(each,path+"\\"+"其他")
print("运行成功！")



    
    
    
    
        
