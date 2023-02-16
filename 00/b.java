import java.util.Scanner;
import java.util.Random;

public class CacheMapping {
  static int cacheSize = 0;
  static int blockSize = 0;
  static int mappingTechnique = 0;
  static int replacementTechnique = 0;
  static int[] cache;
  static int[] mainMemory;

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    Random rand = new Random();

    // Allow the user to select the mapping technique
    System.out.println("Select the mapping technique: 1. Direct Mapping 2. Associative Mapping");
    mappingTechnique = input.nextInt();

    // Allow the user to select the cache size
    System.out.println("Enter the cache size (in words): ");
    cacheSize = input.nextInt();

    // Allow the user to select the block size
    System.out.println("Enter the block size (in words): ");
    blockSize = input.nextInt();

    cache = new int[cacheSize];
    mainMemory = new int[1000];

    // Fill main memory with random words
    for (int i = 0; i < mainMemory.length; i++) {
      mainMemory[i] = rand.nextInt();
    }

    // Request a word from the processor
    System.out.println("Enter a word to be searched: ");
    int word = input.nextInt();

    if (mappingTechnique == 1) {
      // Direct Mapping
      int blockNum = word / blockSize;
      int offset = word % blockSize;
      int cacheIndex = blockNum % cacheSize;

      if (cache[cacheIndex] == word) {
        // hit
        System.out.println("Word found in cache.");
      } else {
        // miss
        cache[cacheIndex] = mainMemory[blockNum * blockSize + offset];
        System.out.println("Word not found in cache. Loaded from main memory.");
      }
    } else if (mappingTechnique == 2) {
      // Associative Mapping
      boolean flag = false;
      for (int i = 0; i < cacheSize; i++) {
        if (cache[i] == word) {
          // hit
          flag = true;
          System.out.println("Word found in cache.");
          break;
        }
      }
      if (!flag) {
        // miss
        if (isCacheFull()) {
          // Allow the user to select replacement technique
          System.out.println("Select the replacement technique: 1. LRU 2. FIFO");
          replacementTechnique = input.nextInt();
          if (replacementTechnique == 1) {
            // LRU
            // Implementation of LRU technique
          } else {
            // FIFO
            // Implementation of FIFO technique
          }
        } else {
          // Cache is not full, load word into the cache
          for (int i = 0; i < cacheSize; i++) {
            if (cache[i] == 0) {
              cache[i] = word;
              break;
            }
          }
        }
        System.out.println("Word not found in cache. Loaded from main memory.");
     
      }
    }
  }

  public static boolean isCacheFull() {
    for (int i = 0; i < cacheSize; i++) {
      if (cache[i] == 0) {
        return false;
      }
    }
    return true;
  }
}
