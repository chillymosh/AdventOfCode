#!/usr/bin/env perl
# I thought this version was cool so copying for reference
use v5.26;
use strict;
use warnings;

my %seeds = <> =~ /(\d+)/g;
my @seed_values = sort { $a <=> $b } keys %seeds;
my @seed_ranges = map { [ $_, $_ + $seeds{$_} - 1 ] } @seed_values;

<>; <>;

my @rules;

while (<>) {
        if (my ($off, $start, $len) = /(\d+)/g) {
                push @rules, [ $start, $start + $len - 1, $off - $start ];
        } else {
                do_rule_block(@rules);
                @rules = ();
                <>;
        }
}

do_rule_block(@rules);
say "Part 2 Result: " . $seed_ranges[0][0];

sub do_rule_block
{
        my @rules = sort { $a->[0] <=> $b->[0] } @_;
        my ($r_start, $r_end, $r_offset) = @{ shift @rules };
        my ($s_start, $s_end)            = @{ shift @seed_ranges };

        my @new_seed_ranges;

        while (1) {
                if ($s_start > $r_end) {
                        last if not @rules;
                        ($r_start, $r_end, $r_offset) = @{ shift @rules };
                } elsif ($s_end < $r_start) {
                        push @new_seed_ranges, [ $s_start, $s_end ];
                        last if not @seed_ranges;
                        ($s_start, $s_end) = @{ shift @seed_ranges };
                } elsif ($s_start < $r_start) {
                        push @new_seed_ranges, [ $s_start, $r_start-1 ];
                        $s_start = $r_start;
                } elsif ($s_end > $r_end) {
                        unshift @seed_ranges, [ $r_end+1, $s_end ];
                        $s_end = $r_end;
                } else {
                        push @new_seed_ranges, [ $s_start + $r_offset, $s_end + $r_offset ];
                        last if not @seed_ranges;
                        ($s_start, $s_end) = @{ shift @seed_ranges };
                }
        }

        @seed_ranges = sort { $a->[0] <=> $b->[0] } @seed_ranges, @new_seed_ranges;
}
