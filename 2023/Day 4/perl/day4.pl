#!/usr/bin/perl

use strict;
use warnings;
use List::Util qw(min);

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
    foreach my $i (keys %$matches) {
        if ($matches->{$i} > 0) {
            $total += 2 ** ($matches->{$i} - 1);
        }
    }
    return $total;
}


my %matches;
foreach my $i (keys %cards) {
    my @winning = @{$cards{$i}->{'winning'}};
    my @mine = @{$cards{$i}->{'mine'}};
    my %intersection;
    @intersection{@winning} = ();
    my @common = grep { exists $intersection{$_} } @mine;
    $matches{$i} = scalar(@common);
}

my $p1 = calculateTotalPoints(\%cards, \%matches);
print "$p1\n";



