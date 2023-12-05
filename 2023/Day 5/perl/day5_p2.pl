#!/usr/bin/perl
use strict;
use warnings;
use List::Util qw(min max pairs);

# Open the input file
open my $fh, '<', 'input.txt' or die "Cannot open input.txt: $!";
local $/ = '';
my @chunks = <$fh>;
chomp @chunks;
close $fh;

# Parse input data
my $seeds = shift @chunks;
$seeds =~ s/^seeds:\s+//;
my @seedsRanges = pairs split /\s+/, $seeds;
my @seedsRangesCopy = @seedsRanges;

my @maps;
foreach my $map (@chunks) {
    my @lines = split /\n/, $map;
    shift @lines;
    my @list = map { [split /\s+/] } @lines;
    push @maps, \@list;
}

my $ranges = \@seedsRangesCopy;
foreach my $map (@maps) {
    my @nextRanges;
    foreach my $mapping (@$map) {
        my ($dest, $src, $len) = @$mapping;
        my @nopeRanges;
        foreach my $range (@$ranges) {
            my ($pos, $plen) = @$range;
            if ($pos + $plen < $src) {
                push @nopeRanges, $range;
            } elsif ($pos >= $src + $len) {
                push @nopeRanges, $range;
            } else {
                my $start = max($pos, $src);
                my $end = min($pos + $plen, $src + $len);
                my $newPos = $dest + $start - $src;
                my $newLen = $end - $start;
                push @nextRanges, [$newPos, $newLen];
                if ($pos < $src) {
                    push @nopeRanges, [$pos, $src - $pos];
                }
                if ($pos + $plen > $src + $len) {
                    push @nopeRanges, [$src + $len, $pos + $plen - $src - $len];
                }
            }
        }
        $ranges = \@nopeRanges;
    }
    push @$ranges, @nextRanges;
}

my $part2_result = min map { $_->[0] } @$ranges;
print "Part 2 Result: $part2_result\n";
