#!/usr/bin/perl
use strict;
use warnings;

sub p1 {
    my ($data) = @_;
    my $ans = 0;
    for (my $i = 0; $i < @$data; $i++) {
        while ($data->[$i] =~ /(\d+)/g) {
            my $num = $1;
            my $start = $-[0] - 1;
            my $end = $+[0];
            my @idxs = ([$i, $start], [$i, $end]);
            push @idxs, map { [$i - 1, $_], [$i + 1, $_] } ($start..$end);

            my $count = 0;
            foreach my $idx (@idxs) {
                my ($a, $b) = @$idx;
                if ($a >= 0 && $a < @$data && $b >= 0 && $b < length($data->[$a]) && substr($data->[$a], $b, 1) ne ".") {
                    $count++;
                }
            }
            $ans += $num if $count > 0;
        }
    }
    return $ans;
}

sub p2 {
    my ($data) = @_;
    my %adj;
    for (my $i = 0; $i < @$data; $i++) {
        while ($data->[$i] =~ /(\d+)/g) {
            my $num = $1;
            my $start = $-[0] - 1;
            my $end = $+[0];
            my @idxs = ([$i, $start], [$i, $end]);
            push @idxs, map { [$i - 1, $_], [$i + 1, $_] } ($start..$end);

            foreach my $idx (@idxs) {
                my ($a, $b) = @$idx;
                if ($a >= 0 && $a < @$data && $b >= 0 && $b < length($data->[$a]) && substr($data->[$a], $b, 1) ne ".") {
                    push @{$adj{"$a,$b"}}, $num;
                }
            }
        }
    }
    my $sum = 0;
    foreach my $key (keys %adj) {
        if (@{$adj{$key}} == 2) {
            $sum += $adj{$key}[0] * $adj{$key}[1];
        }
    }
    return $sum;
}

my $filename = "input.txt";
open my $fh, '<', $filename or die "Could not open file: $!";
chomp(my @data = <$fh>);
close $fh;
print p1(\@data), "\n";
print p2(\@data), "\n";
