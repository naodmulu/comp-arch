import random


class CacheMapping(object):
    cacheSize = int()
    blockSize = int()
    mainMemorySize = int()
    mappingTechnique = int()
    cache = []
    mainMemory = []

    @classmethod
    def main(cls, args):
        cacheSize = int(input("Enter cache size: "))
        blockSize = int(input("Enter block size: "))
        mainMemorySize = int(input("Enter main memory size: "))
        #  Initialize cache and main memory
        cache = [0] * (cacheSize)
        mainMemory = [0] * (mainMemorySize)
        for i in range(len(mainMemory)):
            #  Get user input for cache size, block size, and main memory size
            mainMemory[i] = random.randrange(100)

        #  Get user input for mapping technique
        mappingTechnique = int(
            input(
                "Enter mapping technique (1 for direct mapping, 2 for associative mapping, 3 for set associative mapping):"
            )
        )
        #  Get a random word from main memory
        wordIndex = random.randrange(mainMemorySize)
        requestedWord = mainMemory[wordIndex]
        #  Check if the word is in cache
        isInCache = False
        cacheIndex = 0
        

        for i in range(cacheSize):
            if cache[i] != None and cache[i] == requestedWord:
                isInCache = True
                cacheIndex = i
                break
        #  If the word is in cache, deliver to processor register
        if isInCache:
            print(
                "Word found in cache at index "
                + cacheIndex
                + ". Delivering to processor register."
            )
        else:
            #  If the word is not in cache, bring the block containing the word and deliver to processor
            print("Word not found in cache. Bringing block from main memory.")
            blockIndex = wordIndex // blockSize
            i = blockIndex * blockSize
            while i < (blockIndex + 1) * blockSize:
                
                cache[blockIndex % cacheSize] = mainMemory[i]
                i += 1
            print(
                f"Block delivered to cache at index {blockIndex % cacheSize} . Delivering requested word to processor register."
            )


# main function
if __name__ == "__main__":
    import sys

    CacheMapping.main(sys.argv)
