
use strict;
use warnings;

print "@ARGV\n";
my $numArgs = $#ARGV + 1;
my $num_args = scalar(@ARGV);

print "thanks, you gave me $numArgs command-line arguments.\n";

foreach my $argnum (0 .. $#ARGV) 
{
   print "$ARGV[$argnum]\n";

}




