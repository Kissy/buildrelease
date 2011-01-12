
BEGIN {
    $scriptDir = $0;
    $scriptDir =~ s:\\:/:g;
    $scriptDir =~ s,/?[^/]+$,,;
    $scriptDir = "." if ($scriptDir eq "");
    unshift(@INC, $scriptDir);
    print @INC;
}

use strict;

#require "c:\\perl\\pmodule1.pl";
require "pmodule1.pl";
use pmodule2;

Hello1();
Hello2();

print "I am caller!\n";

1;



