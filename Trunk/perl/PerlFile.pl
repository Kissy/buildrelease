#!/usr/bin/perl

# this is a perl introduce example


$var = 15;
package pack1;
$var = 26;
package pack2;
$var = 34;
package pack1;
print ("pack1 : $var\n");
print ("pack2 : $pack2::var\n"); 
print ("main  : $main::var\n");

exit;

