from tqdm import tqdm
import os
import re


def vid_extn():
    print("\n\t"+"-"*25)
    print("\tExtension of video files")
    print("\t"+"-"*25)
    print("\t1. mkv")
    print("\t2. mp4")
    print("\t3. avi")
    print("\t4. else")
    while 1>0:
        num = int(input("\n\tEnter extension (1-4): "))
        print("\t"+"-"*25)
        if num in[1,2,3,4]:
            break
        else: print("\t"+'chosen number is incorrect')
    
    
    if num==4:
        num=str(input("Enter the extension of video file(ex: .mp4): "))
    else: 
        num=['.mkv','.mp4','.avi'][num-1]
    return num

def sub_extn():
    print("\n\t"+"-"*25)
    print("\tExtension of subtitle files")
    print("\t"+"-"*25)
    print("\t1. srt")
    print("\t2. ass")
    print("\t3. txt")
    print("\t4. else")
    while 1>0:
        num = int(input("\n\tEnter extension (1-4): "))
        print("\t"+"-"*25)
        if num in[1,2,3,4]:
            break
        else: print("\t"+'chosen number is incorrect')
    
    
    if num==4:
        num=str(input("Enter the extension of video file(ex: .mp4): "))
    else: 
        num=['.srt','.ass','.txt'][num-1]
    return num


dir = str(input("\n Full path to video directory(example: E:\media\Shows\...): "))

vid_format = vid_extn()
sub_format = sub_extn()
vid=[]
sub=[]

for name in os.listdir(dir):
    if name[-4:]==vid_format:
        vid.append(name[:-4])
    elif name[-4:]==sub_format:
        sub.append(name[:-4])


eps_num=[]
sub_eps_num=[]

for eps in vid:
    eps_num.append(re.sub('\D', '', re.sub('.....p', '', eps)).lstrip("0"))

for eps in sub:
    sub_eps_num.append(re.sub('\D', '', re.sub('.....p', '', eps)).lstrip("0"))

if len(vid) != len(sub):
    print("number of videos: ",len(vid))
    print("number of subtitles: ",len(sub))
    # if len(vid)>=len(sub):
    #     max=len(vid)
    # else: max=len(sub)

rename=0   

for i in tqdm(range(len(vid))):
    for X in range(len(sub)):
        if eps_num[i] == sub_eps_num[X] :
            os.rename(os.path.join(dir,sub[X]+".ass"),os.path.join(dir,vid[i]+".ass"))
            rename+=1
            break
        elif X == len(sub)-1:
            print(" \n epside num ",i,"has no sub")
print(rename)
