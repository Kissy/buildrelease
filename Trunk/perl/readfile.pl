
use strict;
use warnings;

sub open_display_file
{
  # the filename should be passed in as a parameter
  my $filename = shift;
  # open file to the handle <FILE>
  open(FILE, $filename) || die "Could not read from $filename, program halting.";
  # read the first line, and chomp off the newline
  chomp(my $firstline = <FILE>);
  print $firstline;
  # read other into array
  my @other = <FILE>;
  print @other;
  close FILE;  
}

# a test to show how to call my function
&open_display_file('test.txt');