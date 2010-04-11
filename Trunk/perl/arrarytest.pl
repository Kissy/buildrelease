
use strict;
use warnings;

my @myarray = (123,"hello", 456, 'guy');

foreach(@myarray)
{
	print "$_ " ;
}
print "\n";
foreach my $item (@myarray)
{
	print "$item " ;
}
print "\n";
for(my $i = 0; $i <scalar(@myarray); $i++)
{
	print "$myarray[$i]" . " ";
}
print "\n";
for(0..($#myarray))
{
	print "$myarray[$_]" . " ";
}
print "\n";

@myarray = (@myarray, 789);
print "@myarray\n" ;
push(@myarray,"gril");
print "@myarray\n" ;
unshift(@myarray, '000');
print "@myarray\n" ;
delete $myarray[1];
print "@myarray\n" ;