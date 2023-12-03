<?php

function day2($data, $cube_limits) {
    $sum_of_possible_game_ids = 0;
    $total_power = 0;

    foreach ($data as $game) {
        list($game_id_str, $rounds_info) = explode(": ", $game);
        $game_id_parts = explode(" ", $game_id_str);
        $game_id = intval(end($game_id_parts));

        $rounds = explode("; ", $rounds_info);
        $max_cubes = array("red" => 0, "green" => 0, "blue" => 0);
        $possible = true;

        foreach ($rounds as $round) {
            $scores = explode(", ", $round);
            $round_counts = array("red" => 0, "green" => 0, "blue" => 0);

            foreach ($scores as $score) {
                list($value, $colour) = explode(" ", $score);
                $round_counts[$colour] = intval($value);
                $max_cubes[$colour] = max($max_cubes[$colour], $round_counts[$colour]);
            }
        }

        // Check if the game is possible
        foreach ($max_cubes as $colour => $count) {
            if ($count > $cube_limits[$colour]) {
                $possible = false;
                break;
            }
        }

        // Part 1
        if ($possible) {
            $sum_of_possible_game_ids += $game_id;
        }

        // Part 2: Calculate total power regardless of whether the game is possible
        $total_power += $max_cubes["red"] * $max_cubes["green"] * $max_cubes["blue"];
    }

    return array($sum_of_possible_game_ids, $total_power);
}

$filename = "input.txt";
$data = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
$cube_limits = array("red" => 12, "green" => 13, "blue" => 14);

list($sum_of_ids, $sum_of_powers) = day2($data, $cube_limits);
echo "Sum of IDs: $sum_of_ids, Total Power: $sum_of_powers";
?>