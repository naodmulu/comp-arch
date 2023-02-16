<?php

// Constants
define("CACHE_SIZE", 4);
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
    for ($i = 0; $i < CACHE_SIZE; $i++) {
        if ($cache[$i][0] == $block_num) {
            echo "Hit!<br>";
            return $i;
        }
    }
    echo "Miss!<br>";
    return -1;
}

function bring_block($block_num)
{
    global $main_memory;
    $start_index = $block_num * BLOCK_SIZE;
    $end_index = $start_index + BLOCK_SIZE;
    return array_slice($main_memory, $start_index, $end_index);
}

function deliver_word($word)
{
    global $cache;
    $index = check_cache($word);
    if ($index == -1) {
        $block_num = intdiv($word, BLOCK_SIZE);
        echo "Cache is full. Select a replacement technique (FIFO, LRU, Random): ";
        $replacement = readline();
        if ($replacement == "FIFO") {
            $index = 0;
        } else if ($replacement == "LRU") {
            $index = CACHE_SIZE-1;
        } else if ($replacement == "Random") {
            $index = rand(0, CACHE_SIZE-1);
        } else {
            echo "Invalid replacement technique selected.";
            exit();
        }
        $block = bring_block($block_num);
        $cache[$index] = [$block_num, $block];
    }
    return $cache[$index][1][$word % BLOCK_SIZE];
}

// Main program
if (PHP_SAPI === 'cli') {
    echo "Select the mapping technique (associative): ";
    $technique = readline();
    if ($technique != "ass
