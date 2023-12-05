#!/usr/bin/perl
use strict;
use warnings;

sub read_file {
    my ($filename) = @_;
    open my $fh, '<', 'input.txt' or die "Cannot open input.txt: $!";
    local $/;
    my $content = <$fh>;
    close $fh;
    return $content;
}

sub parse_numbers {
    my ($line) = @_;
    return grep { $_ ne '' } map { int($_) } split / /, $line;
}

sub process_seed {
    my ($seed, $maps_ref) = @_;
    foreach my $map (@$maps_ref) {
        foreach my $mapping (@$map) {
            my ($dest_start, $src_start, $length) = @$mapping;
            if (defined $src_start && defined $seed && $src_start <= $seed && $seed < $src_start + $length) {
                $seed = $dest_start + ($seed - $src_start);
                last;
            }
        }
    }
    return $seed;
}

my $input_data = read_file("input.txt");
my @lines = split /\n/, $input_data;
my @seeds = parse_numbers((split /: /, shift @lines)[1]);

my @maps;
while (@lines) {
    my $line = shift @lines;
    next if $line !~ / map:/;
    my @map;
    while (@lines && $lines[0] !~ / map:/) {
        push @map, [parse_numbers(shift @lines)];
    }
    push @maps, \@map;
}

my @processed_seeds = map { process_seed($_, \@maps) } @seeds;
my $part1_result = (sort { $a <=> $b } @processed_seeds)[0];

print "Part 1 Result: $part1_result\n";