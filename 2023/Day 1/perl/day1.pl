#!/usr/bin/perl

use strict;
use warnings;

my %num_words_to_digits = (
    'zero'  => 0,
    'one'   => 1,
    'two'   => 2,
    'three' => 3,
    'four'  => 4,
    'five'  => 5,
    'six'   => 6,
    'seven' => 7,
    'eight' => 8,
    'nine'  => 9
);

sub main {
    open my $fh, '<', 'input.txt'
      or die "Could not open file: $!";
    my ( $r1_total, $r2_total ) = ( 0, 0 );

    while ( my $line = < $fh > ) {
        chomp $line;

        # Part 1
        my @digits = $line = ~/(\d)/g;
        $r1_total += sum_first_last(@digits) if @digits;

        # Part 2
        $line = replace_number_words( $line, \%num_words_to_digits );
        @digits = $line = ~/(\d)/g;
        $r2_total += sum_first_last(@digits) if @digits;

    }
    print "p1: $r1_total, p2: $r2_total\n";
    close $fh;
}

sub sum_first_last {
    my @nums = @_;
    return $nums[0] . ( $nums[-1] // $nums[0] );
}

sub replace_number_words {
    my $line = shift;

    my $pattern = join( "|", keys %num_words_to_digits, values %num_words_to_digits );
    my @matches = $line = ~/($pattern)/g;

    if (@matches) {
        my $firstNum =
          defined $num_words_to_digits{ $matches[0] }
          ? $num_words_to_digits{ $matches[0] }
          : $matches[0];
        my $lastNum =
          defined $num_words_to_digits{ $matches[-1] }
          ? $num_words_to_digits{ $matches[-1] }
          : $matches[-1];

        return $firstNum . $lastNum;
    }

    return "";
}

main();
