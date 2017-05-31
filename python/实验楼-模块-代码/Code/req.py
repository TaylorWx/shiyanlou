#!/usr/bin/env python3

import os

import os.path

import requests

def download(url):
    '''从指定的url中下载文件并报存在当前的目录
     :arg url:要在下载的文件的url
    '''
    req = requests.get(url)

    #首先我们检查是否存在文件
 
    if req.status_code == 404:

        print('No such file fouond at %s' % url)

        return

    else:
        
        filename = url.split('/')[-1]

    with open(filename, 'wb') as fobj:

        fobj.write(req.content)

    print('Download over.')

if __name__ == '__main__':

    url = input('enter a url:')

    download(url)
