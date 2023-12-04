#!/usr/bin/perl

use strict;
use warnings;

open my $fh, '<', 'input.txt' or die "Failed to open input.txt: $!";
my @lines = <$fh>;
close $fh;

my %cards;

foreach my $i (0 .. $#lines) {

    my $line = $lines[$i];
    $line =~ s/^Card \s* \d+ : \s* //x;
    my ($winning, $mine) = split /\s*\|\s*/, $line;
    my @winningNumbers = grep { $_ ne '' } split ' ', $winning;
    my @mineNumbers = grep { $_ ne '' } split ' ', $mine;

    $cards{$i + 1} = {
        'winning' => \@winningNumbers,
        'mine' => \@mineNumbers,
    };
}

sub calculateTotalPoints {
    my ($cards, $matches) = @_;
    my $total = 0;
    foreach my $match (values %$matches) {
        $total += 2 ** ($match - 1) if $match > 0;
    }
    return $total;
}

sub calculateTotalScratchcards {
    my ($cards, $matches) = @_;
    my @instances = (1) x (scalar keys %$cards);
    foreach my $i (sort { $a <=> $b } keys %$matches) {
        for (my $j = $i + 1; $j <= $i + $matches->{$i} && $j <= scalar keys %$cards; $j++) {
            $instances[$j] += $instances[$i];
        }
    }
    my $sum = 0;
    $sum += $_ for @instances;
    return $sum;
}

my %matches;
foreach my $i (keys %cards) {
    my %count;
    $count{$_}++ for @{$cards{$i}{winning}};
    $count{$_}++ for @{$cards{$i}{mine}};
    $matches{$i} = grep { $count{$_} == 2 } keys %count;
}

my $p1 = calculateTotalPoints(\%cards, \%matches);
print "$p1\n";

my $p2 = calculateTotalScratchcards(\%cards, \%matches);
print "\n$p2\n";