import java.util.*;

public class CacheMapping {
    static int cacheSize;
    static int blockSize;
    static int mappingType;
    static int replacementType;
    static Map<Integer, Block> cache;
    static int blockCounter = 0;
    static int ageCounter = 0;
    static Deque<Integer> FIFO_deque = new LinkedList<>();
    static Map<Integer, Integer> LRU_map = new HashMap<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the cache size: ");
        cacheSize = sc.nextInt();
        System.out.println("Enter the block size: ");
        blockSize = sc.nextInt();
        System.out.println("Select the mapping technique: ");
        System.out.println("1. Direct mapping");
        System.out.println("2. Set associative mapping");
        mappingType = sc.nextInt();
        if (mappingType == 2) {
            System.out.println("Select the replacement technique: ");
            System.out.println("1. FIFO");
            System.out.println("2. LRU");
            replacementType = sc.nextInt();
        }
        cache = new HashMap<Integer, Block>();
        while (true) {
            System.out.println("Enter a word to request: ");
            int word = sc.nextInt();
            int blockNum = getBlockNum(word);
            if (cache.containsKey(blockNum)) {
                System.out.println("Cache hit! Word found in block " + blockNum);
                if (mappingType == 2) {
                    if (replacementType == 1) {
                        updateFIFO(blockNum);
                    } else if (replacementType == 2) {
                        updateLRU(blockNum);
                    }
                }
            } else {
                System.out.println("Cache miss! Word not found in cache.");
                if (cache.size() == cacheSize) {
                    if (mappingType == 1) {
                        int oldestBlock = getOldestBlock();
                        cache.remove(oldestBlock);
                    } else if (mappingType == 2) {
                        int replacedBlock = getReplacedBlock();
                        cache.remove(replacedBlock);
                    }
                }
                Block newBlock = getBlockFromMemory(blockNum);
                cache.put(blockNum, newBlock);
                if (mappingType == 2) {
                    if (replacementType == 1) {
                        updateFIFO(blockNum);
                    } else if (replacementType == 2) {
                        updateLRU(blockNum);
                    }
                }
            }
            System.out.println("Cache content: " + cache.toString());
        }
    }

    public static int getBlockNum(int word) {
        return word / blockSize;
    }

    public static Block getBlockFromMemory(int blockNum) {
        // This is where you would retrieve the block from main memory
        return new Block(blockNum);
    }

    public static int getOldestBlock() {
        int oldestBlock =
cache.entrySet().iterator().next().getKey();
for (Map.Entry<Integer, Block> entry : cache.entrySet()) {
if (entry.getValue().getAge() > cache.get(oldestBlock).getAge()) {
oldestBlock = entry.getKey();
}
}
return oldestBlock;
}
public static int getReplacedBlock() {
    int replacedBlock = 0;
    if (replacementType == 1) {
        replacedBlock = FIFO_deque.pop();
        FIFO_deque.add(replacedBlock);
    } else if (replacementType == 2) {
        replacedBlock = getLRU();
    }
    return replacedBlock;
}

public static int getLRU() {
    int lruBlock = 0;
    int min = Integer.MAX_VALUE;
    for (Map.Entry<Integer, Integer> entry : LRU_map.entrySet()) {
        if (entry.getValue() < min) {
            min = entry.getValue();
            lruBlock = entry.getKey();
        }
    }
    return lruBlock;
}

public static void updateFIFO(int blockNum) {
    FIFO_deque.add(blockNum);
}

public static void updateLRU(int blockNum) {
    if(LRU_map.containsKey(blockNum)) {
        LRU_map.put(blockNum, ageCounter++);
    }else {
        LRU_map.put(blockNum, ageCounter++);
    }
}
}

class Block {
int blockNum;
int age;
public Block(int blockNum) {
    this.blockNum = blockNum;
    this.age = CacheMapping.blockCounter++;
}

public int getAge() {
    return this.age;
}

public String toString() {
    return "Block " + blockNum;
}
}
