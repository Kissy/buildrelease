awk 'BEGIN {print "start..."} {tot+=$2} END {print "totoal is:" tot; print "END..."}' scores.txt

