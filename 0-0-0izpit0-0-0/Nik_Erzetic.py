from functools import lru_cache

# Tretja naloga

def pobeg_iz_mocvirja(swamp):
    l = len(swamp)

    @lru_cache(maxsize=None)
    def aux(energy, k):
        bonus = swamp[k]
        times = []
        if energy + bonus > l-k:
            return 1
        else:
            for i in range(1, energy+bonus+1):
                times.append(aux(energy-i, k+i))
            return 1 + min(times)
    
    return aux(0, 0)

test3 = pobeg_iz_mocvirja(50 * [10])