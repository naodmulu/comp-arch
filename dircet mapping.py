# Write a program that implements Cache mapping techniques: Direct Mapping, Fully Associative Mapping, and Set Associative Mapping
# Allow the user to select the mapping technique he/she wants to visualize
# Based on the technique selected, allow to visualize the cache content
#  Generate a random word (requested by the processor) and make sure if it is in cache (hit) or not (miss)
# If hit, deliver to processor register. If miss, bring the word (a block containing the
# requested word) and deliver the word to the processor.
# Cache should always hold a portion of main memory at any given time
# Main memory content may be some randomly generated blocks of words.
# If cache is full, allow the user to make decide which replacement technique to use.(Remember that in direct mapping that is not required)
import random
import math
import time
import sys
import os

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the cache
def print_cache(cache):
    print("Cache:")
    for i in range(len(cache)):
        print("Block", i, ":", cache[i])
    print()

# Function to print the main memory
def print_main_memory(main_memory):
    print("Main Memory:")
    for i in range(len(main_memory)):
        print("Block", i, ":", main_memory[i])
    print()

# Function to print the cache and main memory
def print_cache_and_main_memory(cache, main_memory):
    print_cache(cache)
    print_main_memory(main_memory)

# Function to print the cache, main memory, and the requested word
def print_cache_main_memory_and_requested_word(cache, main_memory, requested_word):
    print("Requested Word:", requested_word)
    print_cache_and_main_memory(cache, main_memory)

# Function to print the cache, main memory, the requested word, and the hit/miss
def print_cache_main_memory_requested_word_and_hit_or_miss(cache, main_memory, requested_word, hit_or_miss):
    print_cache_main_memory_and_requested_word(cache, main_memory, requested_word)
    print(hit_or_miss)

# Function to print the cache, main memory, the requested word, the hit/miss, and the replacement technique
def print_cache_main_memory_requested_word_hit_or_miss_and_replacement_technique(cache, main_memory, requested_word, hit_or_miss, replacement_technique):
    print_cache_main_memory_requested_word_and_hit_or_miss(cache, main_memory, requested_word, hit_or_miss)
    print("Replacement Technique:", replacement_technique)

# Function to print the cache, main memory, the requested word, the hit/miss, the replacement technique, and the replacement block
def print_cache_main_memory_requested_word_hit_or_miss_replacement_technique_and_replacement_block(cache, main_memory, requested_word, hit_or_miss, replacement_technique, replacement_block):
    print_cache_main_memory_requested_word_hit_or_miss_and_replacement_technique(cache, main_memory, requested_word, hit_or_miss, replacement_technique)
    print("Replacement Block:", replacement_block)

# Function to allow the user to select the mapping technique
def select_mapping_technique():
    print("Select the mapping technique you want to visualize:")
    print("1. Direct Mapping")
    print("2. Fully Associative Mapping")
    print("3. Set Associative Mapping")
    mapping_technique = input("Mapping Technique: ")
    if mapping_technique == "1":
        mapping_technique = "Direct Mapping"
    elif mapping_technique == "2":
        mapping_technique = "Fully Associative Mapping"
    elif mapping_technique == "3":
        mapping_technique = "Set Associative Mapping"
    else:
        print("Invalid mapping technique!")
        sys.exit()
    return mapping_technique

# Function to visualize the cache content based on the mapping technique
def visualize_cache_content_based_on_mapping_technique(mapping_technique):
    if mapping_technique == "Direct Mapping":
        visualize_cache_content_based_on_direct_mapping()
    elif mapping_technique == "Fully Associative Mapping":
        visualize_cache_content_based_on_fully_associative_mapping()
    elif mapping_technique == "Set Associative Mapping":
        visualize_cache_content_based_on_set_associative_mapping()
    else:
        print("Invalid mapping technique!")
        sys.exit()

# Function to visualize the cache content based on direct mapping
def visualize_cache_content_based_on_direct_mapping():
    # Initialize the cache and main memory
    cache = []
    main_memory = []
    # Initialize the cache size
    cache_size = 0
    # Initialize the block size
    block_size = 0
    # Initialize the number of blocks in the cache
    number_of_blocks_in_cache = 0
    # Initialize the number of blocks in main memory
    number_of_blocks_in_main_memory = 0
    # Initialize the number of words in a block
    number_of_words_in_a_block = 0
    # Initialize the number of words in the cache
    number_of_words_in_cache = 0
    # Initialize the number of words in main memory
    number_of_words_in_main_memory = 0
    # Initialize the number of bits in the tag
    number_of_bits_in_tag = 0
    # Initialize the number of bits in the index
    number_of_bits_in_index = 0
    # Initialize the number of bits in the offset
    number_of_bits_in_offset = 0
    # Initialize the number of bits in the word
    number_of_bits_in_word = 0
    # Initialize the number of bits in the block
    number_of_bits_in_block = 0
    # Initialize the number of bits in the cache
    number_of_bits_in_cache = 0
    # Initialize the number of bits in main memory
    number_of_bits_in_main_memory = 0
    # Initialize the number of bits in the address
    number_of_bits_in_address = 0
    # Initialize the replacement technique
    replacement_technique = ""
    # Initialize the replacement block
    replacement_block = 0
    # Initialize the requested word
    requested_word = 0
    # Initialize the hit/miss
    hit_or_miss = ""
    # Initialize the number of hits
    number_of_hits = 0
    # Initialize the number of misses
    number_of_misses = 0
    # Initialize the number of requests
    number_of_requests = 0
    # Initialize the hit ratio
    hit_ratio = 0
    # Initialize the miss ratio
    miss_ratio = 0
    # Initialize the number of bits in the tag, index, offset, and word
    number_of_bits_in_tag = 0
    number_of_bits_in_index = 0
    number_of_bits_in_offset = 0

    # Get the cache size
    cache_size = get_cache_size()
    # Get the block size
    block_size = get_block_size()
    # Get the number of blocks in the cache
    number_of_blocks_in_cache = get_number_of_blocks_in_cache(cache_size, block_size)

    # Get the number of bits in the tag, index, offset, and word
    number_of_bits_in_tag = get_number_of_bits_in_tag()
    number_of_bits_in_index = get_number_of_bits_in_index(number_of_blocks_in_cache)
    number_of_bits_in_offset = get_number_of_bits_in_offset(block_size)
    number_of_bits_in_word = get_number_of_bits_in_word()
    # Get the number of bits in the block
    number_of_bits_in_block = get_number_of_bits_in_block(number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word)
    # Get the number of bits in the cache
    number_of_bits_in_cache = get_number_of_bits_in_cache(number_of_blocks_in_cache, number_of_bits_in_block)
    # Get the number of bits in main memory
    number_of_bits_in_main_memory = get_number_of_bits_in_main_memory(number_of_bits_in_cache)

    # Initialize the cache
    cache = initialize_cache(number_of_blocks_in_cache, number_of_bits_in_block)
    # Initialize the main memory
    main_memory = initialize_main_memory(number_of_bits_in_main_memory)

    # Get the replacement technique
    replacement_technique = get_replacement_technique()

    # Get the number of requests
    number_of_requests = get_number_of_requests()

    # Loop through the number of requests
    for i in range(number_of_requests):
        # Get the requested word
        requested_word = get_requested_word()
        # Get the hit/miss
        hit_or_miss = get_hit_or_miss(cache, requested_word, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word)
        # Get the replacement block
        replacement_block = get_replacement_block(cache, requested_word, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word, replacement_technique)
        # Update the cache
        update_cache(cache, requested_word, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word, replacement_block)
        # Update the main memory
        update_main_memory(main_memory, requested_word, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word, replacement_block)
        # Update the number of hits
        number_of_hits = update_number_of_hits(number_of_hits, hit_or_miss)
        # Update the number of misses
        number_of_misses = update_number_of_misses(number_of_misses, hit_or_miss)
        # Calculate the hit ratio
        hit_ratio = calculate_hit_ratio(number_of_hits, number_of_requests
    number_of_bits_in_word = get_number_of_bits_in_word()
# Function to visualize the cache content based on associativity
def visualize_cache_content_based_on_associativity(cache, number_of_blocks_in_cache, number_of_bits_in_block, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word):
    # Loop through the number of blocks in the cache
    for i in range(number_of_blocks_in_cache):
        # Loop through the number of bits in the block
        for j in range(number_of_bits_in_block):
            # Print the cache content
            print(cache[i][j], end=" ")
        # Print a newline
        print()
    # Print a newline
    print()
# Function to visualize the main memory content based on associativity
def visualize_main_memory_content_based_on_associativity(main_memory, number_of_bits_in_main_memory, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word):
    # Loop through the number of bits in main memory
    for i in range(number_of_bits_in_main_memory):
        # Print the main memory content
        print(main_memory[i], end=" ")
    # Print a newline
    print()
    # Print a newline
    print()
# Function to visualize the cache content based on set-associarive
def visualize_cache_content_based_on_set_associative(cache, number_of_blocks_in_cache, number_of_bits_in_block, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word):
    # Loop through the number of blocks in the cache
    for i in range(number_of_blocks_in_cache):
        # Loop through the number of bits in the block
        for j in range(number_of_bits_in_block):
            # Print the cache content
            print(cache[i][j], end=" ")
        # Print a newline
        print()
    # Print a newline
    print()
# Function to visualize the main memory content based on set-associative
def visualize_main_memory_content_based_on_set_associative(main_memory, number_of_bits_in_main_memory, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word):
    # Loop through the number of bits in main memory
    for i in range(number_of_bits_in_main_memory):
        # Print the main memory content
        print(main_memory[i], end=" ")
    # Print a newline
    print()
    # Print a newline
    print()
# Function to visualize the cache content based on direct-mapped
def visualize_cache_content_based_on_direct_mapped(cache, number_of_blocks_in_cache, number_of_bits_in_block, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word):
    # Loop through the number of blocks in the cache
    for i in range(number_of_blocks_in_cache):
        # Loop through the number of bits in the block
        for j in range(number_of_bits_in_block):
            # Print the cache content
            print(cache[i][j], end=" ")
        # Print a newline
        print()
    # Print a newline
    print()
# Function to interconnect all the functions
def main():
    # Get the number of bits in the cache
    number_of_bits_in_cache = get_number_of_bits_in_cache()
    # Get the number of bits in the block
    number_of_bits_in_block = get_number_of_bits_in_block()
    # Get the number of bits in the tag
    number_of_bits_in_tag = get_number_of_bits_in_tag(number_of_bits_in_cache, number_of_bits_in_block)
    # Get the number of bits in the index
    number_of_bits_in_index = get_number_of_bits_in_index(number_of_bits_in_cache, number_of_bits_in_block)
    # Get the number of bits in the offset
    number_of_bits_in_offset = get_number_of_bits_in_offset(number_of_bits_in_block)
    # Get the number of bits in the word
    number_of_bits_in_word = get_number_of_bits_in_word()
    # Get the number of blocks in the cache
    number_of_blocks_in_cache = get_number_of_blocks_in_cache(number_of_bits_in_cache, number_of_bits_in_block)
    # Get the number of bits in main memory
    number_of_bits_in_main_memory = get_number_of_bits_in_main_memory(number_of_bits_in_cache)

    # Initialize the cache
    cache = initialize_cache(number_of_blocks_in_cache, number_of_bits_in_block)
    # Initialize the main memory
    main_memory = initialize_main_memory(number_of_bits_in_main_memory)

    # Get the replacement technique
    replacement_technique = get_replacement_technique()

    # Get the number of requests
    number_of_requests = get_number_of_requests()

    # Loop through the number of requests
    for i in range(number_of_requests):
        # Get the requested word
        requested_word = get_requested_word()
        # Get the hit/miss
        hit_or_miss = get_hit_or_miss(cache, requested_word, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word)
        # Get the replacement block
        replacement_block = get_replacement_block(cache, requested_word, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word, replacement_technique)
        # Update the cache
        update_cache(cache, requested_word, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word, replacement_block)
        # Update the main memory
        update_main_memory(main_memory, requested_word, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word, replacement_block)
        # Visualize the cache content based on associativity
        visualize_cache_content_based_on_associativity(cache, number_of_blocks_in_cache, number_of_bits_in_block, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word)
        # Visualize the main memory content based on associativity
        visualize_main_memory_content_based_on_associativity(main_memory, number_of_bits_in_main_memory, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word)
        # Visualize the cache content based on set-associarive
        visualize_cache_content_based_on_set_associative(cache, number_of_blocks_in_cache, number_of_bits_in_block, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word)
        # Visualize the main memory content based on set-associarive
        visualize_main_memory_content_based_on_set_associative(main_memory, number_of_bits_in_main_memory, number_of_bits_in_tag, number_of_bits_in_index, number_of_bits_in_offset, number_of_bits_in_word)
# Call the main function
main()
