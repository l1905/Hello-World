#!/bin/bash
#author:litong
#disk pra convert json
#time:2013/9/13
iostat -d |awk -vS=2 -vE=6 'NR==3{for(n=S;n<=E;n++)a[n]="\""$n"\":"}NR==4{printf "{"a[S]$S;for(n=S+1;n<=E;n++)printf(","a[n]$n);print "}"}'
