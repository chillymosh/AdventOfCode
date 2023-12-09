<?php

function differences($seq) {
    $diffs = [];
    for ($i = 0; $i < count($seq) - 1; $i++) {
        $diffs[] = $seq[$i + 1] - $seq[$i];
    }
    return $diffs;
}

function buildSequences($seq) {
    $sequences = [$seq];
    while (!allZeros(end($sequences))) {
        $sequences[] = differences(end($sequences));
    }
    return $sequences;
}

function allZeros($seq) {
    foreach ($seq as $num) {
        if ($num !== 0) return false;
    }
    return true;
}

function solveSequence($seq) {
    $sequences = buildSequences($seq);
    return array_sum(array_map(fn($s) => end($s), $sequences));
}

function solveFromFile($filename) {
    $lines = file($filename, FILE_IGNORE_NEW_LINES);
    $partOneSum = array_sum(array_map(fn($line) => solveSequence(array_map('intval', explode(' ', $line))), $lines));
    $partTwoSum = array_sum(array_map(fn($line) => solveSequence(array_reverse(array_map('intval', explode(' ', $line)))), $lines));
    return [$partOneSum, $partTwoSum];
}

[$p1, $p2] = solveFromFile("input.txt");
echo "Part One Result: $p1<br>Part Two Result: $p2<br>";



// Smaller version
function solveSequenceA($seq) {
    $sequences = [$seq];

    while (end($sequences)) {
        $lastSeq = end($sequences);
        if (count(array_unique($lastSeq)) === 1 && end($lastSeq) === 0) break;
        $newSeq = [];
        for ($i = 0; $i < count($lastSeq) - 1; $i++) {
            $newSeq[] = $lastSeq[$i + 1] - $lastSeq[$i];
        }
        $sequences[] = $newSeq;
    }

    return array_sum(array_map(fn($s) => end($s), $sequences));
}

function solveFromFileA($filename) {
    $lines = file($filename, FILE_IGNORE_NEW_LINES);
    $partOneSum = array_sum(array_map(fn($line) => solveSequenceA(array_map('intval', explode(' ', $line))), $lines));
    $partTwoSum = array_sum(array_map(fn($line) => solveSequenceA(array_reverse(array_map('intval', explode(' ', $line)))), $lines));
    return [$partOneSum, $partTwoSum];
}

[$p1, $p2] = solveFromFileA("input.txt");
echo "Part One Result: $p1<br>Part Two Result: $p2<br>";
?>
