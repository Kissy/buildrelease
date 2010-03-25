use strict;
use warnings;

my $usage = <<EOU;
usage : [-a] [-bnum] [-cstr1] [-dstr2]
	-a == a option
	-b == b option
	-c == c option
	-d == d option
EOU

print $usage;

my $a = 0;
my $b = 0;
my $c = 0;
my $d = 0;

foreach my $arg (@ARGV)
{
	if ($arg =~/^-a$/i){$a = 1;}
	elsif ($arg =~/^-b(.*)$/i) {$b = $1;}
	elsif ($arg =~/^-c(.*)$/i) {$c = $1;}
	elsif ($arg =~/^-d(.*)$/i) {$d = $1;}
}

if($a) {print"a option is used!\n";}
if($b) {print"b option is used! and the value is $b\n";}
if($c) {print"c option is used! and the value is $c\n";}
if($d) {print"d option is used! and the value is $d\n";}

#calling
#perl commandline3.pl -a -b12 -cfoo -dbar
#output
#usage : [-a] [-bnum] [-cstr1] [-dstr2]
#       -a == a option
#       -b == b option
#       -c == c option
#       -d == d option
#a option is used!
#b option is used! and the value is 12
#c option is used! and the value is foo
#d option is used! and the value is bar