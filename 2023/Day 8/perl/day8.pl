#!/usr/bin/perl
use strict;
use warnings;
use List::Util qw(reduce);
use Math::BigInt;

sub create_paths {
    my @lines = @_;
    my %paths;
    foreach my $line (@lines) {
        my ($k, $l, $r) = $line =~ /[1-9A-Z]+/g;
        $paths{$k} = {"L" => $l, "R" => $r};
    }
    return %paths;
}
sub gcd {
    my ($a, $b) = @_;
    return $b == 0 ? $a : gcd($b, $a % $b);
}

sub lcm {
    my ($a, $b) = @_;
    return ($a * $b) / gcd($a, $b);
}

sub part1 {
    my ($paths, $dirs) = @_;
    my $pos = "AAA";
    my $solution = 0;
    while ($pos ne "ZZZ") {
        my $dir = $dirs->[$solution++ % scalar @$dirs];
        $pos = $paths->{$pos}{$dir};
    }
    return $solution;
}

sub part2 {
   my ($paths, $dirs) = @_;
    my @keys = grep { length($_) >= 3 && substr($_, 2, 1) eq "A" } keys %$paths;
    my @values = map {
        my $pos = $_;
        my $i = 0;
        while (substr($pos, 2, 1) ne "Z") {
            my $dir = $dirs->[$i++ % scalar @$dirs];
            $pos = $paths->{$pos}{$dir};
        }
        $i;
    } @keys;
    return reduce { lcm(Math::BigInt->new($a), Math::BigInt->new($b)) } 1, @values;
}

my $filename = "input.txt";
open my $fh, '<', $filename or die "Could not open file: $!";
chomp(my @data = <$fh>);
close $fh;
my @dirs = split //, $data[0]; 
my %paths = create_paths(@data[2..$#data]);
my $p1 = part1(\%paths, \@dirs);
my $p2 = part2(\%paths, \@dirs);
print "$p1\n";
print "$p2\n";