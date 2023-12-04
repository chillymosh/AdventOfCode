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

?>  