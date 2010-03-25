
use strict;
use warnings;

my $result = add(10,20,30);
print $result;

sub add
{
#	our($first,$second)= @_;
#	return $first + $second;
	print $#_ + 1;
	print "\n";
    return $_[0] + $_[$#_];
}