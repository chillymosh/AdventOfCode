<?php


$lines = file('input.txt', FILE_IGNORE_NEW_LINES);

$cards = [];

foreach ($lines as $i => $line) {

    $line = trim(substr($line, strpos($line, ':') + 1));

    [$winning, $mine] = explode('|', $line);

    $winningNumbers = array_filter(explode(' ', trim($winning)), function ($value) { return $value !== ''; });
    $mineNumbers = array_filter(explode(' ', trim($mine)), function ($value) { return $value !== ''; });

    $cards[$i + 1] = [
        'winning' => $winningNumbers,
        'mine' => $mineNumbers
    ];
}

function calculateTotalPoints($cards, $matches) {
    $total = 0;
    foreach ($matches as $i => $match) {
        if ($match > 0) {
            $total += pow(2, $match - 1);
        }
    }
    return $total;
}

function calculateTotalScratchcards($cards, $matches) {
    $instances = array_fill(1, count($cards), 1);
    foreach ($matches as $i => $match) {
        for ($j = $i + 1; $j <= min(count($cards), $i + $match); $j++) {
            $instances[$j] += $instances[$i];
        }
    }
    return array_sum($instances);
}

$matches = [];
foreach ($cards as $i => $card) {
    $matches[$i] = count(array_intersect($card['winning'], $card['mine']));
}

$p1 = calculateTotalPoints($cards, $matches);
echo $p1 . "\n";

$p2 = calculateTotalScratchcards($cards, $matches);
echo $p2 . "\n";

// Alternate way using Mysty's Python version as a base

$p1_total = 0;
$p2_total = 0;
$thing = array_fill(0, count($lines), 1);

foreach ($lines as $i => $r) {
    list($numbers_s, $winning_s) = explode(" | ", explode(": ", $r)[1]);

    $numbers = array_map('intval', array_filter(explode(" ", $numbers_s), 'ctype_digit'));
    $winning = array_map('intval', array_filter(explode(" ", $winning_s), 'ctype_digit'));
    $matching = array_intersect($numbers, $winning);

    // PART ONE
    $p1_total += count($matching) > 0 ? 2 ** (count($matching) - 1) : 0;

    // PART TWO
    $match_count = count($matching);
    for ($j = 1; $j <= $match_count; $j++) {
        if ($i + $j < count($lines)) {
            $thing[$i + $j] += $thing[$i];
        }
    }
}

$p2_total = array_sum($thing);
echo "PART ONE TOTAL: $p1_total\n";
echo "PART TWO TOTAL: $p2_total\n";

?>  