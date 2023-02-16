import math

class CacheMapping:
    cacheSize = 0
    blockSize = 0
    mappingType = 0
    replacementType = 0
    cache = None
    blockCounter = 0
    ageCounter = 0
    FIFO_deque = []
    LRU_map = {}

    @staticmethod
    def main(args):
        
        print("Enter the cache size: ")
        CacheMapping.cacheSize = input()
        print("Enter the block size: ")
        CacheMapping.blockSize = input()
        print("Select the mapping technique: ")
        print("1. Direct mapping")
        print("2. Set associative mapping")
        CacheMapping.mappingType = input()
        if CacheMapping.mappingType == 2:
            print("Select the replacement technique: ")
            print("1. FIFO")
            print("2. LRU")
            CacheMapping.replacementType = input()
        CacheMapping.cache = {}
        while True:
            print("Enter a word to request: ")
            word = input()
            blockNum = CacheMapping.getBlockNum(word)
            if blockNum in CacheMapping.cache.keys():
                print("Cache hit! Word found in block " + str(blockNum))
                if CacheMapping.mappingType == 2:
                    if CacheMapping.replacementType == 1:
                        CacheMapping.updateFIFO(blockNum)
                    elif CacheMapping.replacementType == 2:
                        CacheMapping.updateLRU(blockNum)
            else:
                print("Cache miss! Word not found in cache.")
                if len(CacheMapping.cache) == CacheMapping.cacheSize:
                    if CacheMapping.mappingType == 1:
                        oldestBlock = CacheMapping.getOldestBlock()
                        CacheMapping.cache.pop(oldestBlock)
                    elif CacheMapping.mappingType == 2:
                        replacedBlock = CacheMapping.getReplacedBlock()
                        CacheMapping.cache.pop(replacedBlock)
                newBlock = CacheMapping.getBlockFromMemory(blockNum)
                CacheMapping.cache[blockNum] = newBlock
                if CacheMapping.mappingType == 2:
                    if CacheMapping.replacementType == 1:
                        CacheMapping.updateFIFO(blockNum)
                    elif CacheMapping.replacementType == 2:
                        CacheMapping.updateLRU(blockNum)
            print("Cache content: " + str(CacheMapping.cache))

    @staticmethod
    def getBlockNum(word):
        return math.trunc(word / float(CacheMapping.blockSize))

    @staticmethod
    def getBlockFromMemory(blockNum):
        # This is where you would retrieve the block from main memory
        return Block(blockNum)

    @staticmethod
    def getOldestBlock():
        oldestBlock = CacheMapping.cache.entrySet().iterator().next().getKey()
        for entry in CacheMapping.cache.entrySet():
            if entry.getValue().getAge() > CacheMapping.cache[oldestBlock].getAge():
                oldestBlock = entry.getKey()
        return oldestBlock
    @staticmethod
    def getReplacedBlock():
        replacedBlock = 0
        if CacheMapping.replacementType == 1:
            replacedBlock = CacheMapping.FIFO_deque.pop()
            CacheMapping.FIFO_deque.add(replacedBlock)
        elif CacheMapping.replacementType == 2:
            replacedBlock = CacheMapping.getLRU()
        return replacedBlock

    @staticmethod
    def getLRU():
        lruBlock = 0
        min = Integer.MAX_VALUE
        for entry in CacheMapping.LRU_map.entrySet():
            if entry.getValue() < min:
                min = entry.getValue()
                lruBlock = entry.getKey()
        return lruBlock

    @staticmethod
    def updateFIFO(blockNum):
        CacheMapping.FIFO_deque.add(blockNum)

    @staticmethod
    def updateLRU(blockNum):
        if blockNum in CacheMapping.LRU_map.keys():

            CacheMapping.LRU_map[blockNum] = CacheMapping.ageCounter
            CacheMapping.ageCounter += 1
        else:
            CacheMapping.LRU_map[blockNum] = CacheMapping.ageCounter
            CacheMapping.ageCounter += 1

class Block(object) :
    blockNum = 0
    age = 0
    def __init__(self, blockNum) :
        self.blockNum = blockNum
        self.age = CacheMapping.blockCounter +12 1
    def  getAge(self) :
        return self.age
    def  toString(self) :
        return "Block " + str(self.blockNum)        

def main():
    CacheMapping.main([])

if __name__ == "__main__":
    main()
