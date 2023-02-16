<?php

// Constants
define("NUM_SETS", 2);
define("ASSOCIATIVITY", 2);
define("MAIN_MEMORY_SIZE", 64);
define("BLOCK_SIZE", 4);

// Variables
$cache = array();
$main_memory = range(0, MAIN_MEMORY_SIZE);
for ($i = 0; $i < NUM_SETS; $i++) {
    $cache[$i] = array();
    for($j = 0; $j < ASSOCIATIVITY; $j++) {
        $cache[$i][$j] = [-1, -1];
    }
}

function visualize_cache()
{
    global $cache;
    echo "Cache Content:<br>";
    for ($i = 0; $i < NUM_SETS; $i++) {
        echo "Set $i:<br>";
        for($j = 0; $j < ASSOCIATIVITY; $j++) {
            echo "Block $j: ".json_encode($cache[$i][$j])."<br>";
        }
    }
}

function generate_random_word()
{
    return rand(0, MAIN_MEMORY_SIZE-1);
}

function check_cache($word)
{
    global $cache;
    $block_num = intdiv($word, BLOCK_SIZE);
    $set_num = $block_num % NUM_SETS;
    for ($i = 0
