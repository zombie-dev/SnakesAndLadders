#!/usr/bin/env perl

use 5.010;
use IO::All;

for my $file ( map { io( $_ )->open } @ARGV ) {
    say "\nReading File: " . $file->filename;
    
    print $file->getline until $file->eof;
}
