#commandline2.pl

use strict;
use warnings;

my $usage = <<EOU;
usage : [-a] [-b=num] [-c=str1] [-d=str2]
	-a == a option
	-b == b option
	-c == c option
	-d == d option
EOU

print $usage;

use Getopt::Long;
#use Getopt::Std;
GetOptions("a!", "b=i", "c=s", "d:s");

if(our $opt_a) {print"a option is used!\n";}
if(our $opt_b) {print"b option is used! and the value is $opt_b\n";}
if(our $opt_c) {print"c option is used! and the value is $opt_c\n";}
if(our $opt_d) {print"d option is used! and the value is $opt_d\n";}

#calling
#perl commandline2.pl -a -b=12 -c=foo -d=bar
#output
#usage : [-a] [-b=num] [-c=str1] [-d=str2]
#       -a == a option
#       -b == b option
#       -c == c option
#       -d == d option
#a option is used!
#b option is used! and the value is 12
#c option is used! and the value is foo
#d option is used! and the value is bar