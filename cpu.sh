#!/bin/bash
#author:litong
#cpu pra convert json
#time:2013/9/13
iostat -c |awk '{if(NR==4) print "{""\"%user\":"$1",","\"%nice\":"$2",","\"%system\":"$3",","\"%iowait\":"$4",","\"%steal\":"$5",","\"%idle\":"$6"}"}'
