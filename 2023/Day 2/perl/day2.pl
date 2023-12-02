#!/usr/bin/perl
use strict;
use warnings;

sub day2 {
    my ($data, $cube_limits) = @_;
    my $sum_of_possible_game_ids = 0;
    my $total_power = 0;

    foreach my $game (@$data) {
        my ($game_id_str, $rounds_info) = split /: /, $game;
        my @game_id_parts = split / /, $game_id_str;
        my $game_id = pop @game_id_parts;

        my @rounds = split /; /, $rounds_info;
        my %max_cubes = (red => 0, green => 0, blue => 0);
        my $possible = 1;

        foreach my $round (@rounds) {
            my @scores = split /, /, $round;
            my %round_counts = (red => 0, green => 0, blue => 0);

            foreach my $score (@scores) {
                my ($value, $colour) = split / /, $score;
                $round_counts{$colour} = $value;
                $max_cubes{$colour} = $max_cubes{$colour} > $round_counts{$colour} ? $max_cubes{$colour} : $round_counts{$colour};
            }
        }

        foreach my $colour (keys %max_cubes) {
            if ($max_cubes{$colour} > $cube_limits->{$colour}) {
                $possible = 0;
                last;
            }
        }

        $sum_of_possible_game_ids += $game_id if $possible;

        $total_power += $max_cubes{red} * $max_cubes{green} * $max_cubes{blue};
    }

    return ($sum_of_possible_game_ids, $total_power);
}


sub main {
    my $filename = "input.txt";
    open my $fh, '<', $filename or die "Could not open file: $!";
    chomp(my @data = <$fh>);
    close $fh;
    my $cube_limits = { red => 12, green => 13, blue => 14 };

    my ($sum_of_ids, $sum_of_powers) = day2(\@data, $cube_limits);
    print "Sum of IDs: $sum_of_ids, Total Power: $sum_of_powers\n";
}

main();