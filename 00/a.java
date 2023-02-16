import java.util.Scanner;
import java.util.Random;

public class CacheMapping {
    static int cacheSize;
    static int blockSize;
    static int mainMemorySize;
    static int mappingTechnique;
    static String[] cache;
    static String[] mainMemory;
    static Random rand = new Random();
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        // Get user input for cache size, block size, and main memory size
        System.out.print("Enter cache size: ");
        cacheSize = sc.nextInt();
        System.out.print("Enter block size: ");
        blockSize = sc.nextInt();
        System.out.print("Enter main memory size: ");
        mainMemorySize = sc.nextInt();

        // Initialize cache and main memory
        cache = new String[cacheSize];
        mainMemory = new String[mainMemorySize];

        // Fill main memory with random words
        for (int i = 0; i < mainMemorySize; i++) {
            mainMemory[i] = Integer.toString(rand.nextInt(100));
        }

        // Get user input for mapping technique
        System.out.print("Enter mapping technique (1 for direct mapping): ");
        mappingTechnique = sc.nextInt();

        // Get a random word from main memory
        int wordIndex = rand.nextInt(mainMemorySize);
        String requestedWord = mainMemory[wordIndex];

        // Check if the word is in cache
        boolean isInCache = false;
        int cacheIndex = 0;
        for (int i = 0; i < cacheSize; i++) {
            if (cache[i] != null && cache[i].equals(requestedWord)) {
                isInCache = true;
                cacheIndex = i;
                break;
            }
        }

        // If the word is in cache, deliver to processor register
        if (isInCache) {
            System.out.println("Word found in cache at index " + cacheIndex + ". Delivering to processor register.");
        }
        // If the word is not in cache, bring the block containing the word and deliver to processor
        else {
            System.out.println("Word not found in cache. Bringing block from main memory.");
            int blockIndex = wordIndex / blockSize;
            for (int i = blockIndex * blockSize; i < (blockIndex + 1) * blockSize; i++) {
                cache[blockIndex % cacheSize] = mainMemory[i];
            }
            System.out.println("Block delivered to cache at index " + (blockIndex % cacheSize) + ". Delivering requested word to processor register.");
        }
    }
}
