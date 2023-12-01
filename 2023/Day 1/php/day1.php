<?php
// This is built on top of Rawoke's attempt. I simply optimised it slightly.

$r1 = $r2 = 0;

$lines = file('input.txt');

function get_num($line)
{
    static $num_lookup = [
        "zero" => "0",
        "one" => "1",
        "two" => "2",
        "three" => "3",
        "four" => "4",
        "five" => "5",
        "six" => "6",
        "seven" => "7",
        "eight" => "8",
        "nine" => "9",
    ];

    $pattern = '/(' . implode("|", array_keys($num_lookup)) . '|' . implode("|", array_values($num_lookup)) . ')/';
    $matches = [];

    if (preg_match_all($pattern, $line, $matches, PREG_OFFSET_CAPTURE)) {
        $firstNum = null;
        $lastNum = null;

        foreach ($matches[0] as $match) {
            $num = isset($num_lookup[$match[0]]) ? $num_lookup[$match[0]] : $match[0];

            if ($firstNum === null) {
                $firstNum = $num;
            }
            $lastNum = $num;
        }

        return $firstNum . $lastNum;
    }

    return "";
}

foreach ($lines as $line) {
    // Part 1
    preg_match_all('/\d/', $line, $matches);
    $digits = $matches[0];

    // Part 2
    if (!empty($digits)) {
        $firstDigit = $digits[0];
        $lastDigit = end($digits);
        $r1 += intval($firstDigit . $lastDigit);
    }

    $num_val = get_num($line);
    $r2 += (int) $num_val;
}

echo "p1: {$r1} p2: {$r2}";
