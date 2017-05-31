#coding=gbk

import re, zipfile

if __name__ == '__main__':
    target = '90052'
    z = zipfile.ZipFile('channel.zip')
    while 1:
        target_file = '%s.txt' % target
        print(z.getinfo(target_file).comment.decode('ascii'), end='')
        #这里decode不懂
        f = z.open(target_file)
        match_obj = re.match(r'^Next nothing is (\d+)',f.read().decode('ascii'))
        f.close()
        if match_obj:
            target = match_obj.groups()[0]
        else:
            break
    z.close()
