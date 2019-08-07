import os
import time

source_dir = [r'D:\wamp64\www\hook',r'D:\wamp64\www\pinyin']

target_dir = './'

target_path = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S')

if not os.path.exists(target_path):
	os.mkdir(target_path)

target_filename = time.strftime('%H%M%S')

comment = input('Enter a comment:')

if len(comment) == 0:
	final_file = target_path + os.sep + target_filename + '.zip'
else:
	final_file = target_path + os.sep + target_filename + '_' + comment.replace(' ','_') + '.zip'

zip_command = 'zip -r {0} {1}'.format(final_file, ' ' .join(source_dir))

if os.system(zip_command) == 0:
	print('Done')
else:
	print('Failed')
