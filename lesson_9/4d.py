import argparse
import sys
import os
n=-1
TEXT1=''
TEXT2=''
parser = argparse.ArgumentParser(description='DEREVO')
parser.add_argument('values',metavar='VALUES',type=str,help='directory')
parser.add_argument('--folders_only',action='store_true')
parser.add_argument('--include',action='store')
parser.add_argument('--exclude',action='store')
parser.add_argument('--all',action='store_true')
parser.add_argument('--full_name',action='store_true')
args = parser.parse_args()
ar=args.values
for a in os.listdir(ar):
    if args.folders_only is True:
        if os.path.isfile(a)==True:
            continue
    if args.include!=None:
        TEXT1=args.include
    if args.exclude!=None:
        TEXT2=args.exclude
    if TEXT1!='':
        if a.find(TEXT1)==-1:
            continue
    if TEXT2!='':
        if a.find(TEXT2)!=-1:
            continue
    if args.all!=True:
        if a[0]=='.':
            continue
    if args.full_name==True:
       print('├──',os.getcwd(),a)
       arga=ar+'/'+a
       if os.path.isdir(arga)==True:
        n+=1
        for b in os.listdir(arga):
         if args.folders_only is True:
           if os.path.isfile(b)!=True:
             continue
         print('│','         ├──',os.getcwd(),b)
         if os.path.isdir(b)==True:
           arg=arga+'/'+b
           if os.path.isdir(arga)==True:
               for c in os.listdir(arg):
                   print('│','         ├──',os.getcwd(),b)
       n=-1
    else:
     print('├──',a)
     arga=ar+'/'+a
     if os.path.isdir(arga)==True:
       n+=1
       for b in os.listdir(arga):
        if args.folders_only is True:
           if os.path.isfile(b)!=True:
             continue
        print('│','         ├──',b)
        if os.path.isdir(b)==True:
          arg=arga+'/'+b
          if os.path.isdir(arga)==True:
               for c in os.listdir(arg):
                   print('│','         ├──',os.getcwd(),b)
     n=-1
