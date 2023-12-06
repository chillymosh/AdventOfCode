<?php

function calculateWaysToWin($time, $distance) {
    $sqrtPart = sqrt(pow($time, 2) / 4 - $distance);
    return $time - 2 * intval($time / 2 - $sqrtPart) - 1;
}

function calculateWaysToWinIterative($time, $distance) {
    $waysToWin = 0;
    for ($holdTime = 0; $holdTime < $time; $holdTime++) {
        $travelDistance = $holdTime * ($time - $holdTime);
        if ($travelDistance > $distance) {
            $waysToWin++;
        }
    }
    return $waysToWin;
}

$filename = "input.txt"; 
$content = file_get_contents($filename);
$lines = explode("\n", $content);

// Part 1
$times = array_map('intval', explode(" ", preg_replace('/\s+/', ' ', trim(explode(":", $lines[0])[1]))));
$distances = array_map('intval', explode(" ", preg_replace('/\s+/', ' ', trim(explode(":", $lines[1])[1]))));

$p1 = 1;
for ($i = 0; $i < count($times); $i++) {
    $p1 *= calculateWaysToWin($times[$i], $distances[$i]);
}

echo $p1  . "\n";


// Part 2
$time = intval(implode('', explode(" ", preg_replace('/\s+/', ' ', trim(explode(":", $lines[0])[1])))));
$distance = intval(implode('', explode(" ", preg_replace('/\s+/', ' ', trim(explode(":", $lines[1])[1])))));
$p2 = calculateWaysToWin($time, $distance);

echo $p2 . "\n";

// Part 1 iterative version
$p1_a = 1;
for ($i = 0; $i < count($times); $i++) {
    $p1_a *= calculateWaysToWinIterative($times[$i], $distances[$i]);
}

echo $p1_a . "\n";
?>
