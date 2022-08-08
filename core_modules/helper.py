import settings
import sys
import subprocess
import os
import random
import time
import tarfile
from pprint import pprint

#try installing module requirements

try:
    from pathlib import Path
    import numpy as np
    import cv2
    from PIL import Image
except Exception as e:
    print(f"Excetion has occurred : {e}")
    print(subprocess.check_call(["python", "-m", "pip", "install", "--upgrade", "pip"]))
    print(subprocess.check_call([sys.executable,"-m", "pip", "install", "-r", "requirements.txt"]))
    # print(subprocess.check_call([sys.executable, "-m", "pip", "install", module]))
finally:
    from pathlib import Path
    import numpy as np
    import cv2
    from PIL import Image

data_dir= settings.data_dir


def file_validation(rootdir):
    # face image path validation.
    if not os.path.isdir(rootdir):
        # print(f"\'{rootdir}\' not existed")
        return False
    else:
        # print(f"\'{rootdir}\' is already existed")
        return True
    
    
def unzip_tar(tardir):
    f = tarfile.open(tardir)
    # print(f.getnames())
    f.extractall("./")
    f.close()
    print("done")
    
# unzip_tar(settings.tardir)
    
# file_validation(data_dir)
    
# names_l = os.listdir(data_dir)

def listdirs1(rootdir,debug=False):
    # get subdir best in speed
    start = time.time()
    names_dir = [ os.path.join(rootdir,x) for x in os.listdir(rootdir)
            if os.path.isdir(os.path.join(rootdir,x))]
    end = time.time() - start
    if debug:
        return names_dir,end
    return names_dir


def listdirs2(rootdir,debug=False):
    # get subdir
    start = time.time()
    names_dir = []
        
    for path in Path(rootdir).iterdir():
        if path.is_dir():
            names_dir.append(str(path))
            # print(path)
            
    if debug:
        end = time.time() - start
        return names_dir,end
    return names_dir

def listdirs2_t(rootdir,debug=False):
    # get subdir
    start = time.time()
    names_dir = []
        
    for path in Path(rootdir).iterdir():
        if path.is_dir():
            names_dir.append(str(path))
            # print(path)
    end = time.time() - start

    if debug:
        return names_dir,end
    return names_dir



def listdirs3(rootdir,debug=False):
    # get all subdir in a regression way
    if debug:
        start = time.time()
    names_dir = []
    for it in os.scandir(rootdir):
        if it.is_dir():
            # print(it.path)
            names_dir.append(listdirs2(it.path))
        else:
            names_dir.append(it.path)
    if debug:
        end = time.time() - start
        # print("time :", end)
        return names_dir, end
    return names_dir




def listdirs4(rootdir,debug=False):
    #should use this
    # get all image directories from rootdir        
    start = time.time()
    name_dir = []
    for root, subdirectories, files in os.walk(rootdir):
        for subdirectory in subdirectories:
            subdir = os.path.join(root, subdirectory)
            # print(os.path.join(root, subdirectory))
        for file in files:
            name_dir.append(os.path.join(root, file))
            # print(os.path.join(root, file))
    end = time.time() - start
    if debug:
        return name_dir, end
    return name_dir

def write_as_file(name,txt):
    with open(f"{name}.txt","w") as f:
        f.write(str(txt))
# def logger(name,data):
    


# print(listdirs1(data_dir,True)[1])
# print(listdirs2(data_dir,True)[1])
# print(listdirs3(data_dir,True)[1])

# print(listdirs1(data_dir) == listdirs3(data_dir))


# write_as_file(listdirs2(data_dir))



def test_time(times):
    # testtime1 = []
    testtime2 = []
    testtime3 = []
    
    timer = 0
    for i in range(times):
        # testtime1.append(listdirs1(data_dir,True)[1])
        testtime2.append(listdirs2(data_dir,True)[1])
        testtime3.append(listdirs2_t(data_dir,True)[1])
        timer += 1
        print(timer)
    # pprint(testtime1)
    # print("\n")
    # pprint(testtime2)

    # t1 = np.mean(testtime1)
    t2 = np.mean(testtime2)
    t3 = np.mean(testtime3)
    write_as_file([t2,t3])
    print(" : ",t2," : ",t3)
    




if __name__ == '__main__':
    # pass
    print(listdirs4(data_dir))
    # test_time(10)
    # print("gg")
    # time.sleep(10)
    # print("gg")
    # os.system('shutdown -s -f')





