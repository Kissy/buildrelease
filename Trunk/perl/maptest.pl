
use strict;
use warnings;

my %myhash = ('k1',100,'k2',200);
# my %myhash = (k1=>100,k2=>200);
print %myhash ;
print "\n";
$myhash{'k3'} = 300;
$myhash{'k4'} = 400;
print %myhash ;
print "\n";

foreach my $key (keys %myhash)
{
	print $key . " indexes ".$myhash{$key}."\n";
}
foreach my $value (values %myhash)
{
	print $value ."\n";
}
while((my $key, my $value)= each(%myhash))
{
	print "$key indexes $value \n"
}

if(exists $myhash{'k1'}) {print "k1 is exist\n";}

delete $myhash{'k1'};
print %myhash ;
print "\n" ;


