#!/usr/bin/perl -w
########################################################
#	PERL ADDITION
# Date: 6/11/2015
# Author: Lee
# Summary: Small addition script with Perl
# Turn this into a perl calculator
#
########################################################

print STDOUT "Enter the first number: ";
$num1 = <STDIN>;
print STDOUT "Enter the second number: ";
$num2 = <STDIN>;
$sum = $num1 + $num2;
print STDOUT "The sum  is: $sum\n";

