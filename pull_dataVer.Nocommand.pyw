from glob import glob
import shutil
import os
from time import sleep
pic = "E:\\Pictures"
clp = "E:\\Clips"
son = "E:\\Music"
total = glob("C:\\*")
def pict(file):
    for f in file:
        if f[-4:] == ".png":
          print(f)
          shutil.copy(src=f, dst=pic)
        elif f[-4:] ==".jpg":
            print(f)
            shutil.copy(src=f, dst=pic)
        elif f[-4:] ==".jfif":
           print(f)
           shutil.copy(src=f, dst=pic)
        elif f[-4:] ==".gif":
            print(f)
            shutil.copy(src=f, dst=pic)
        else:
           try:
              os.chdir(f)
              tet = glob(f+str("\*"))
              if tet == []:
                continue
              else:
                pict(tet)
           except:
             continue

def sound(file):
    for f in file:
        if f[-4:] == ".mp3":
          print(f)
          shutil.copy(src=f, dst=son)
        elif f[-4:] ==".wma":
           print(f)
           shutil.copy(src=f, dst=son)
        elif f[-4:] ==".acc":
           print(f)
           shutil.copy(src=f, dst=son)
        elif f[-4:] ==".m4a":
           print(f)
           shutil.copy(src=f, dst=son)
        elif f[-4:] ==".wav":
           print(f)
           shutil.copy(src=f, dst=son)
        else:
            try:
                os.chdir(f)
                tet = glob(f+str("\*"))
                if tet == []:
                  continue
                else:
                  sound(tet)
            except:
                continue

def Video(file):
    for f in file:
        if f[-4:] == ".avi":
           print(f)
           shutil.copy(src=f, dst=clp)
        elif f[-4:] ==".mp4":
           print(f)
           shutil.copy(src=f, dst=clp)
        elif f[-4:] ==".wmv":
           print(f)
           shutil.copy(src=f, dst=clp)
        elif f[-4:] ==".MPEG":
           print(f)
           shutil.copy(src=f, dst=clp)
        elif f[-4:] ==".MOV":
           print(f)
           shutil.copy(src=f, dst=clp)
        elif f[-4:] ==".dat":
           print(f)
           shutil.copy(src=f, dst=clp)
        elif f[-4:] ==".flv":
           print(f)
           shutil.copy(src=f, dst=clp)
        else:
            try:
                os.chdir(f)
                tet = glob(f+str("\*"))
                if tet == []:
                  continue
                else:
                   Video(tet)
            except:
               continue

def All(file):
   for f in file:
    if f[-4:] == ".png":
        print(f)
        shutil.copy(src=f, dst=pic)
    elif f[-4:] ==".mp4":
        print(f)
        shutil.copy(src=f, dst=clp)
    elif f[-4:] ==".pdf":
        print(f)
        shutil.copy(src=f, dst=pic)
    elif f[-4:] ==".jpg":
        print(f)
        shutil.copy(src=f, dst=pic)
    elif f[-4:] ==".mp3":
        print(f)
        shutil.copy(src=f, dst=son)
    elif f[-4:] ==".jfif":
        print(f)
        shutil.copy(src=f, dst=pic)
    elif f[-4:] ==".gif":
        print(f)
        shutil.copy(src=f, dst=pic)
    else:
        try:
            os.chdir(f)
            tet = glob(f+str("\*"))
            if tet == []:
              continue
            else:
               All(tet)
        except:
            continue

print()
print()
print("""[1]___ Videos and clips (All types).
[2]___ Sound and Musics (All types).
[3]___ Pictures (All types).
[4]___ All. (png,gif,jfif,mp3,mp4,jpg,png,pdf)
""")
print("--------------------------------------------------------------------")
print("Hit Ctrl-C to start if not pressed within 5 seconds,will work automatically")
print()
try:
    for i in range(0,5):
        sleep(1)
    All(total)

except KeyboardInterrupt:
    choose = int(input("Please select a number: "))
    if choose == 1:
       Video(total)
    elif choose == 2:
       sound(total)
    elif choose == 3:
       pict(total)
    elif choose == 4:
       All(total)
    
    


