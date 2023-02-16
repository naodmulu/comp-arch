<?php

// Constants
define("CACHE_SIZE", 8);
define("MAIN_MEMORY_SIZE", 64);
define("BLOCK_SIZE", 4);

// Variables
$cache = array();
$main_memory = range(0, MAIN_MEMORY_SIZE);
for ($i = 0; $i < CACHE_SIZE; $i++) {
    $cache[$i] = [-1, -1];
}

function visualize_cache()
{
    global $cache;
    echo "Cache Content:<br>";
    for ($i = 0; $i < CACHE_SIZE; $i++) {
        echo "Block $i: ".json_encode($cache[$i])."<br>";
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
    $cache_index = $block_num % CACHE_SIZE;
    if ($cache[$cache_index][0] == $block_num) {
        echo "Hit!<
