<?php
$input_data = file_get_contents("input.txt");
$sections = explode("\n\n", trim($input_data));
$data = [];

foreach ($sections as $section) {
    $lines = explode("\n", $section);
    $header = explode(":", $lines[0]);
    $map_name = $header[0];
    if (strpos($header[0], "seeds") !== false) {
        $data["seeds"] = array_map('intval', explode(" ", trim($header[1])));
    } else {
        $values = [];
        for ($i = 1; $i < count($lines); $i++) {
            $values[] = array_map('intval', explode(" ", $lines[$i]));
        }
        $data[$map_name] = $values;
    }
}

function part_1($seed, $data) {
    foreach ($data as $map_name => $map_values) {
        if ($map_name !== "seeds") {
            foreach ($map_values as $value) {
                list($dest_start, $src_start, $length) = $value;
                if ($src_start <= $seed && $seed < $src_start + $length) {
                    $offset = $seed - $src_start;
                    $seed = $dest_start + $offset;
                    break;
                }
            }
        }
    }
    return $seed;
}

function part_2($data) {
    $seeds = $data["seeds"];
    $ranges = [];
    for ($i = 0; $i < count($seeds); $i += 2) {
        $ranges[] = [$seeds[$i], $seeds[$i + 1] + $seeds[$i] - 1];
    }

    foreach ($data as $map_name => $map_values) {
        if ($map_name !== "seeds") {
            $nums = [];
            $overlaps = $ranges;
            foreach ($map_values as $value) {
                $new_overlaps = [];
                foreach ($overlaps as $overlap) {
                    $overlap_start = max($value[1], $overlap[0]);
                    $overlap_end = min($value[1] + $value[2] - 1, $overlap[1]);
                    if ($overlap_start <= $overlap_end) {
                        $nums[] = [$overlap_start + $value[0] - $value[1], $overlap_end + $value[0] - $value[1]];
                        if ($overlap[0] < $overlap_start) {
                            $new_overlaps[] = [$overlap[0], $overlap_start - 1];
                        }
                        if ($overlap[1] > $overlap_end) {
                            $new_overlaps[] = [$overlap_end + 1, $overlap[1]];
                        }
                    } else {
                        $new_overlaps[] = $overlap;
                    }
                }
                $overlaps = $new_overlaps;
            }
            $ranges = array_merge($overlaps, $nums);
        }
    }
    return min(array_column($ranges, 0));
}

$p1_seeds = array_map(function ($seed) use ($data) {
    return part_1($seed, $data);
}, $data["seeds"]);

$p1 = min($p1_seeds);
echo "Part 1: $p1\n";
$p2 = part_2($data);
echo "Part 2: $p2\n";
