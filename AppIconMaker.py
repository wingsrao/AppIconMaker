# coding=utf-8
from PIL import Image

fileName = 'chuyin_icon'

sizeArr = [
	#iphone notification 20pt
	{'40':'@2x'},
	{'60':'@3x'},
	#iphone seetings 29pt
	{'29':''},
	{'58':'@2x'},
	{'87':'@3x'},
	#iphone spotlight 40pt
	{'80':'@2x'},
	{'120':'@3x'},
	#iphone app 57pt
	{'57':''},
	{'114':'@2x'},
	#iphone app 60pt
	{'120':'@2x'},
	{'180':'@3x'},
	#app store iOS 1024pt
	{'1024':''},
]

# 打开一个jpg图像文件，注意是当前路径:
# im = Image.open(fileName + '.png')
# 获得图像尺寸:
# w, h = im.size
# print('Original image size: %sx%s' % (w, h))
# im.thumbnail((512,512))
# im.save(fileName + ('_%s.png' % 512), 'png') 

for sizeDict in sizeArr:
	for size,suffix in sizeDict.items():
		im = Image.open(fileName + '.png')
		ww = int(size,10)
		im.thumbnail((ww,ww))
		im.save(fileName + ('_%s%s.png' % (size,suffix)), 'png') 
		# 把缩放后的图像用png(jpeg)格式保存:
		print('Resize image to: %sx%s' % (size,size))




