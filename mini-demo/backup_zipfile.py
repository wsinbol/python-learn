import zipfile
import os
import time

# source_dir = [r'D:\wamp64\www\hook',r'D:\wamp64\www\pinyin']
# source_dir = [r'D:\wamp64\www\pinyin\example.php']
source_dir = [r'test.py']

target_dir = './'

# target_file = target_dir + os.sep + time.strftime('%Y%m%d') + '.zip'
'''
target_file = target_dir + os.sep + 'test.zip'

with zipfile.ZipFile(target_file, 'w') as zf:
	for path in source_dir:
		zf.write(path)
'''

# fz = zipfile.ZipFile(target_file, 'w', zipfile.ZIP_DEFLATED)
# for path in source_dir:
# 	fz.write(path)
# fz.close()


with zipfile.ZipFile(target_file, 'r') as zf:
	print(zf.infolist())
	#[<ZipInfo filename='wamp64/www/hook/' filemode='drwxrwxrwx' external_attr=0x10>, <ZipInfo filename='wamp64/www/pinyin/' filemode='drwxrwxrwx' external_attr=0x10>]
	print(zf.getinfo('wamp64/www/hook/'))
	# <ZipInfo filename='wamp64/www/hook/' filemode='drwxrwxrwx' external_attr=0x10>
	print(zf.namelist())
	# ['wamp64/www/hook/', 'wamp64/www/pinyin/']
	
# Can't include folder, only files
with zipfile.ZipFile(target_file) as zf:
	with zf.open('test.py') as f:
		print(f.read())

with zipfile.ZipFile('test.zip', 'r') as zf:
	zf.extractall()
