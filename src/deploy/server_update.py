'''Updates Apache server '''

import os

from githandler import Git

src_loc = '/home/juris/stickman/src/site'
target = '/home/www/site'

def copy_files(source,target):
    for thisDir, subDirs, files in os.walk(source):
        for fileNm in files:
            f = open(os.path.join(target, fileNm),'bw')
            for line in open(os.path.join(thisDir, fileNm),'br'):
                f.write(line)
            f.close()

if __name__ == '__main__':
    git = Git(src_loc)
    git.pull()
    copy_files(src_loc, target)


