#!/usr/bin/perl -W

use strict;

sub Add
{
  my @nums = @_;
  my $sum = 0;
  foreach my $num (@nums)
  {
    $sum += $num;
  }
  return $sum ;
}

sub Multiply
{
	my @nums = @_;
	my $sum = 1;
	$sum *= $_ for @nums;
	return $sum;
}
sub ToSentence
{
	my @words = @_;
	return (join(" ",@words));
}

sub Hello
{
	print "hello world!";
}

sub Main
{
	my ($caltype, @nums) = @_;
	if ($caltype eq "Add") 
	{
		print (Add(@nums));
	}
	elsif($caltype eq "Multiply")
	{
		print (Multiply(@nums));
	}
	elsif($caltype eq "ToSentence")
	{
		print(ToSentence(@nums));
	}
	else
	{
		Hello();
	};	
	
}

Main(@ARGV);

# Multiply 10 20 30
# Add 10 20 30 40 50
# ToSentence hello how are you !
# 
