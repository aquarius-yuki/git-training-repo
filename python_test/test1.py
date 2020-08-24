import sys

#実行中のpythonのバージョンを表示する
major = sys.version_info.major

if major < 3:
    print('Python2')  
else:
    print('Python3')

