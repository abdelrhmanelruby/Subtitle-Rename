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
        num=str(input("Enter the extension of subtitle file(ex: .mp4): "))
    else: 
        num=['.srt','.ass','.txt'][num-1]
    return num

print("\n\t"+"*"*60)
print("\n\t Make sure subtiles and videos are in the same diractory.")
print("\n\t"+"*"*60)

dir = str(input("\n\t Full path to video directory(example: E:\media\Shows\...): "))

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
    for n in [6,5,4,3,2,1]:
        try:
            eps=re.findall('e'+'[0-9]'*n,eps.lower())[0]
            break
        except:
            pass
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
    eps_num.append(re.sub('\D', '', eps).lstrip("0"))

for eps in sub:
    for n in [6,5,4,3,2,1]:
        try:
            eps=re.findall('e'+'[0-9]'*n,eps.lower())[0]
            break
        except:
            pass
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
    sub_eps_num.append(re.sub('\D', '', eps).lstrip("0"))

if len(vid) != len(sub):
    print('\t')
    print("\t!!!!! number of videos: ",len(vid))
    print("\t!!!!! number of subtitles: ",len(sub),'\n')
    print("\t"+"*"*25+'\n')
    

rename=0   
miss_sub=[]
for i in range(len(vid)):
    for X in range(len(sub)):
        if eps_num[i] == sub_eps_num[X] :
            os.rename(os.path.join(dir,sub[X]+sub_format),os.path.join(dir,vid[i]+sub_format))
            rename+=1
            break
        elif X == len(sub)-1:
            print("\t!!!!! episode number",eps_num[i],"has no subtitle.")
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
