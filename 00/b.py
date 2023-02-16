2import sys
import random


class CacheMapping(object):
    cacheSize = 0
    blockSize = 0
    mappingTechnique = 0
    replacementTechnique = 0
    cache = None
    mainMemory = None

    @staticmethod
    def main(args):
        # Allow the user to select the mapping technique
        print("Select the mapping technique: 1. Direct Mapping 2. Associative Mapping")
        CacheMapping.mappingTechnique = input()
        # Allow the user to select the cache size
        print("Enter the cache size (in words): ")
        CacheMapping.cacheSize = int(input())
        # Allow the user to select the block size
        print("Enter the block size (in words): ")
        CacheMapping.blockSize = input()
        CacheMapping.cache = [0] * (CacheMapping.cacheSize)
        CacheMapping.mainMemory = [0] * (1000)
        # Fill main memory with random words
        i = 0
        while i < len(CacheMapping.mainMemory):
            CacheMapping.mainMemory[i] = random.seed()
            i += 1
        # Request a word from the processor
        print("Enter a word to be searched: ")
        word = input()
        if CacheMapping.mappingTechnique == 1:
            # Direct Mapping
            blockNum = int(word / CacheMapping.blockSize)
            offset = word % CacheMapping.blockSize
            cacheIndex = blockNum % CacheMapping.cacheSize
            if CacheMapping.cache[cacheIndex] == word:
                # hit
                print("Word found in cache.")
            else:
                # miss
                CacheMapping.cache[cacheIndex] = CacheMapping.mainMemory[
                    blockNum * CacheMapping.blockSize + offset
                ]
                print("Word not found in cache. Loaded from main memory.")
        elif CacheMapping.mappingTechnique == 2:
            # Associative Mapping
            flag = False
            i = 0
            while i < CacheMapping.cacheSize:
                if CacheMapping.cache[i] == word:
                    # hit
                    flag = True
                    print("Word found in cache.")
                    break
                i += 1
            if not flag:
                # miss
                if CacheMapping.isCacheFull():
                    # Allow the user to select replacement technique
                    print("Select the replacement technique: 1. LRU 2. FIFO")
                    CacheMapping.replacementTechnique = input()
                    if CacheMapping.replacementTechnique == 1:
                        pass
                    else:
                        print("else")
            else:
                # Cache is not full, load word into the cache
                i = 0
                while i < CacheMapping.cacheSize:
                    if CacheMapping.cache[i] == 0:
                        CacheMapping.cache[i] = word
                        break
                    i += 1
            print("Word not found in cache. Loaded from main memory.")

    @staticmethod
    def isCacheFull():
        i = 0
        while i < CacheMapping.cacheSize:
            if CacheMapping.cache[i] == 0:
                return False
            i += 1
        return True


if __name__ == "__main__":
    CacheMapping.main(sys.argv)
