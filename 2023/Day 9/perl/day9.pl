#!/usr/bin/perl
use strict;
use warnings;
use List::Util qw(sum);

sub differences {
    my @seq = @_;
    return map { $seq[$_ + 1] - $seq[$_] } 0 .. $#seq - 1;
}

sub build_sequences {
    my @seq = @_;
    if (@seq == grep { $_ == 0 } @seq) {
        return ([@seq]);
    } else {
        return ([@seq], build_sequences(differences(@seq)));
    }
}

sub solve_sequence {
    my @seq = @_;
    my @sequences = build_sequences(@seq);
    return sum(map { $_->[-1] } @sequences);
}

sub solve_from_file {
    my ($filename) = @_;
    my $p1 = 0;
    my $p2 = 0;

    open my $fh, '<', $filename or die "Cannot open file: $!";
    while (my $line = <$fh>) {
        chomp $line;
        my @numbers = split / /, $line;
        $p1 += solve_sequence(@numbers);
        $p2 += solve_sequence(reverse @numbers);
    }
    close $fh;

    return ($p1, $p2);
}

my ($p1, $p2) = solve_from_file("input.txt");
print "Part One Result: $p1\n";
print "Part Two Result: $p2\n";



# Streamlined Version

sub solve_sequence_a {
    my @seq = @_;
    my @sequences = ([@seq]);

    while (my @last_seq = @{$sequences[-1]}) {
        last if @last_seq == grep { $_ == 0 } @last_seq;
        push @sequences, [map { $last_seq[$_ + 1] - $last_seq[$_] } 0 .. $#last_seq - 1];
    }

    return sum(map { $_->[-1] } @sequences);
}

sub solve_from_file_a {
    my ($filename) = @_;
    open my $fh, '<', $filename or die "Cannot open file: $!";
    my ($p1, $p2) = (0, 0);

    while (my $line = <$fh>) {
        chomp $line;
        my @numbers = split / /, $line;
        $p1 += solve_sequence_a(@numbers);
        $p2 += solve_sequence_a(reverse @numbers);
    }
    close $fh;

    return ($p1, $p2);
}

# Example usage
my ($p1a, $p2a) = solve_from_file_a("input.txt");
print "Part One Result: $p1a\n";
print "Part Two Result: $p2a\n";
