#!/usr/bin/perl
use strict;
use warnings;

sub calculate_ways_to_win {
    my ($time, $distance) = @_;
    my $sqrt_part = sqrt(($time ** 2) / 4 - $distance);
    return $time - 2 * int($time / 2 - $sqrt_part) - 1;
}

my $filename = "input.txt"; 
open(my $fh, '<', $filename) or die "Could not open file '$filename' $!";
my @lines = <$fh>;
close($fh);

(my $time_line = $lines[0]) =~ s/Time:\s+//;
(my $distance_line = $lines[1]) =~ s/Distance:\s+//;
my @times = split(/\s+/, $time_line);
my @distances = split(/\s+/, $distance_line);

my $p1 = 1;
for (my $i = 0; $i < scalar @times; $i++) {
    $p1 *= calculate_ways_to_win($times[$i], $distances[$i]);
}

my $concatenated_time = join('', @times);
my $concatenated_distance = join('', @distances);

my $p2 = calculate_ways_to_win($concatenated_time, $concatenated_distance);

print "Part 1 Result: $p1\n";
print "Part 2 Result: $p2\n";
