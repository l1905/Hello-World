#!/bin/bash
#author:litong
#memory pra convert json
#time:2013/9/13
vmstat |awk -vS=3 -vE=5 'NR==2{for(n=S;n<=E;n++)a[n]="\""$n"\":"}NR==3{printf "{"a[S]$S;for(n=S+1;n<=E;n++)printf(","a[n]$n);print "}"}'
