#!/usr/bin/env perl

use 5.010;

my $current_file = $ARGV;

while (my $line = <>) {
    if ($current_file ne $ARGV) {
        say "\nReading File: $ARGV";
        $current_file = $ARGV;
    }
    print($line);
}
