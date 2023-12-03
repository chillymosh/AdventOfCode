<?php
$filename = "input.txt";
$data = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);


function fullNumber($x, $y, &$schematic, &$searched) {
    $y_min = $y;
    $y_max = $y;
    while ($y_min >= 1 && ctype_digit($schematic[$x][$y_min - 1])) {
        $y_min--;
    }
    while ($y_max < count($schematic[$x]) && ctype_digit($schematic[$x][$y_max])) {
        $y_max++;
    }

    $key = $x . "," . $y_min . "," . $y_max;
    if (!in_array($key, $searched)) {
        $searched[] = $key;
        return intval(implode(array_slice($schematic[$x], $y_min, $y_max - $y_min)));
    }
    return 0;
}

function adjacentNumbers($i, $j, &$schematic, &$searched) {
    $numbers = [];
    $directions = [[-1, 0], [-1, -1], [-1, 1], [0, -1], [0, 1], [1, 0], [1, -1], [1, 1]];
    foreach ($directions as $d) {
        $x = $i + $d[0];
        $y = $j + $d[1];
        if ($x >= 0 && $x < count($schematic) && $y >= 0 && $y < count($schematic[$x]) && ctype_digit($schematic[$x][$y])) {
            $number = fullNumber($x, $y, $schematic, $searched);
            if ($number != 0) {
                $numbers[] = $number;
            }
        }
    }
    return $numbers;
}

function findParts(&$schematic) {
    $searched = [];
    $parts = [];
    for ($i = 0; $i < count($schematic); $i++) {
        for ($j = 0; $j < count($schematic[$i]); $j++) {
            if (!ctype_digit($schematic[$i][$j]) && $schematic[$i][$j] != ".") {
                $parts[] = [$schematic[$i][$j], adjacentNumbers($i, $j, $schematic, $searched)];
            }
        }
    }
    return $parts;
}

function p1($parts) {
    $sum = 0;
    foreach ($parts as $part) {
        $sum += array_sum($part[1]);
    }
    return $sum;
}

function p2($parts) {
    $productSum = 0;
    foreach ($parts as $part) {
        if (count($part[1]) == 2) {
            $productSum += array_product($part[1]);
        }
    }
    return $productSum;
}

$schematic = array_map('str_split', $data);
$parts = findParts($schematic);

echo p1($parts) . "\n";
echo p2($parts) . "\n";




function p1_a($data) {
    $ans = 0;
    foreach ($data as $i => $line) {
        preg_match_all('/\d+/', $line, $matches, PREG_OFFSET_CAPTURE);
        foreach ($matches[0] as $m) {
            $idxs = [];
            $start = $m[1] - 1;
            $end = $m[1] + strlen($m[0]);
            array_push($idxs, [$i, $start], [$i, $end]);
            for ($j = $start; $j <= $end; $j++) {
                $idxs[] = [$i - 1, $j];
                $idxs[] = [$i + 1, $j];
            }
            $count = 0;
            foreach ($idxs as $idx) {
                [$a, $b] = $idx;
                if ($a >= 0 && $a < count($data) && $b >= 0 && $b < strlen($data[$a]) && $data[$a][$b] != ".") {
                    $count++;
                }
            }
            if ($count > 0) {
                $ans += intval($m[0]);
            }
        }
    }
    return $ans;
}

function p2_a($data) {
    $adj = [];
    foreach ($data as $i => $line) {
        preg_match_all('/\d+/', $line, $matches, PREG_OFFSET_CAPTURE);
        foreach ($matches[0] as $m) {
            $idxs = [];
            $start = $m[1] - 1;
            $end = $m[1] + strlen($m[0]);
            array_push($idxs, [$i, $start], [$i, $end]);
            for ($j = $start; $j <= $end; $j++) {
                $idxs[] = [$i - 1, $j];
                $idxs[] = [$i + 1, $j];
            }
            foreach ($idxs as $idx) {
                [$a, $b] = $idx;
                if ($a >= 0 && $a < count($data) && $b >= 0 && $b < strlen($data[$a]) && $data[$a][$b] != ".") {
                    $key = $a . ',' . $b;
                    $adj[$key][] = $m[0];
                }
            }
        }
    }
    $sum = 0;
    foreach ($adj as $values) {
        if (count($values) == 2) {
            $sum += intval($values[0]) * intval($values[1]);
        }
    }
    return $sum;
}
echo "</br>";
echo p1_a($data) . "\n";
echo p2_a($data) . "\n";
?>


