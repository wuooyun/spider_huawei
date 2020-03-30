import os

'''
Usage: ls.py [options] [path1 [path2 [...pathN]]]

The paths are optional; if nowt given .is used.

Options:
    -h --help   show this help message and exit
    -H --hidden    show hidden files [default:off]
    -m --modified   show last modified date/time [default:off]
    -o ORDER, --order=ORDER
                    order by('name','n','modified','m','size','s')
                    [default:name]
     
'''


###path prase

def ls(path,**):
    os.listdir()
