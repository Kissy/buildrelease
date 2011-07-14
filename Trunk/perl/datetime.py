#!/usr/bin/perl
use strict;
use warnings;
use POSIX qw(strftime);

# seconds from 1970.01.01 00:00:00
my $ti = time();
print $ti;
print "\n";
print strftime("%Y-%m-%d %H:%M:%S\n", localtime($ti));
#1310623469
#2011-07-14 14:03:58

my $t = localtime();
print $t;
print "\n";
#Thu Jul 14 12:25:16 2011

my ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst)=localtime();
print $year;
print "\n";
#111

print strftime("%Y-%m-%d %H:%M:%S\n", localtime());
#2011-07-14 12:26:01