""" 
        Author: Abdelrhman Elruby
        github: github.com/abdelrhmanelruby

"""

import os
import re


def vid_extn():
    print("\n\t"+"-"*25)
    print("\tExtension of video files")
    print("\t"+"-"*25)
    print("\t1. mkv | mp4 | avi")
    print("\t2. else")
    while 1>0:
        extn = int(input("\n\tEnter extension (1-2): "))
        print("\t"+"-"*25)
        if extn in[1,2]:
            break
        else: print('\tchosen number is incorrect')
    
    if extn==2:
        extn=str(input("\n\tEnter the extension of video file(ex: .mp4): "))
    return extn

def sub_extn():
    print("\n\t"+"-"*25)
    print("\tExtension of subtitle files")
    print("\t"+"-"*25)
    print("\t1. srt | ass | txt | sub")
    print("\t2. else")
    while 1>0:
        extn = int(input("\n\tEnter extension (1-2): "))
        print("\t"+"-"*25)
        if extn in[1,2]:
            break
        else: print('\tchosen number is incorrect')
    
    
    if extn==2:
        extn=str(input("\n\tEnter the extension of subtitle file(ex: .srt): "))
    return extn

print("\n\t"+"*"*60)
print("\n\tMake sure subtiles and videos are in the same diractory.")
print("\n\t"+"*"*60)

dir = str(input("\n\tFull path to video directory(example: E:\media\Shows\...): "))

vid_format = vid_extn()
sub_format = sub_extn()
vid=[]
sub=[]

for name in os.listdir(dir):
    if vid_format==1:
        if name.endswith('.mp4') or name.endswith('.mkv') or name.endswith('.avi'):
            vid.append(name)
    elif name.endswith(vid_format):
            vid.append(name)

    if sub_format==1:
        if name.endswith('.srt') or name.endswith('.ass') or name.endswith('.txt') or name.endswith('.sub'):
            sub.append(name)
    elif name.endswith(sub_format):
            sub.append(name)

if not vid:
    raise SystemExit("\tNo video files were found with the selected extension")
if not sub:
    raise SystemExit("\tNo subtile files were found with the selected extension")

def get_num(sorce):
    num=[]
    for eps in sorce:
        for n in [6,5,4,3,2,1]:
            try:
                eps=re.findall('e'+'[0-9]'*n,eps.lower())[0] 
                break
            except:
                if n != 1:
                    continue
                else: pass
            eps=re.sub('[0-9][0-9][0-9][0-9]p', '', eps.lower()) #1080p
            eps=re.sub('[0-9][0-9][0-9]p', '', eps) #720p
            eps=re.sub('[0-9][0-9]bit', '', eps) #10bit
            eps=re.sub('[0-9]bit', '', eps) #8bit
            eps=re.sub('x[0-9][0-9][0-9]', '', eps) #X265
            eps=re.sub('s[0-9][0-9]', '', eps) #s05
            eps=re.sub('s[0-9]', '', eps) #s5
            eps=re.sub('av1', '', eps) #AV1
            eps=re.sub('[0-9]ch', '', eps) #2ch
            eps=re.sub('DDP[0-9].[0-9]', '', eps) #DDP5.1
            eps=re.sub('ion[0-9][0-9]', '', eps) #ION10
            eps=re.sub('20[0-9][0-9]', '', eps) #2019
            eps=re.sub('19[0-9][0-9]', '', eps) #1999
            eps=re.sub('hdr[0-9][0-9]', '', eps) #hdr
        num.append(re.sub('\D', '', eps).lstrip("0"))
    return num

eps_num=get_num(vid)
sub_eps_num=get_num(sub)

if len(vid) != len(sub):
    print('\t')
    print("\t!!!!! number of videos: ",len(vid)+"!!!!!")
    print("\t!!!!! number of subtitles: ",len(sub)+"!!!!!",'\n')
    print("\t"+"*"*25+'\n')
    

rename=0   
miss_sub=[]
print(sub_eps_num)
print(eps_num)

for i in range(len(vid)):
    for X in range(len(sub)):
        if eps_num[i] == sub_eps_num[X] :
            os.rename(os.path.join(dir,sub[X]),os.path.join(dir,vid[i][:-4]+sub[X][-4:]))
            rename+=1
            break
        elif X == len(sub)-1:
            print("\t!!!!! episode number",eps_num[i],"has no subtitle."+"!!!!!")
            miss_sub.append(vid[i])

if len(vid) != rename:
    print("\n\t"+"*"*25+'\n')
print('\t{0}'.format(rename),"episodes have been renamed successfully.\n")
print("\t"+"*"*25+'\n')

def rem_sub():
    miss_vid=[]
    for X in range(len(sub)):
        for i in range(len(vid)):
            if eps_num[i] == sub_eps_num[X] :
                break
            elif i == len(vid)-1:
                miss_vid.append(sub[X])
    return miss_vid


if rename != len(vid) or rename != len(sub):
    show_rem=input('\tshow the remaining video and subtitle files?(Y|N)')
    
    if show_rem.lower() == 'y':
        miss_vid=rem_sub()
        
        if (len(miss_vid)>=1):
            print('\n\t'+"*"*7+'Subtitles Without Video'+"*"*7+'\n')
            for i in miss_vid:
                print("\t"+i)
        if (len(miss_sub)>=1):
            print('\n\t'+"*"*7+'Videos Without Subtitle'+"*"*7+'\n')
            for i in miss_sub:
                print("\t"+i)

input('\n\tPress Enter to Quit...')
