from typing import List

def maximumEnergy(energy: List[int], k: int) -> int:
    """
    In a mystic dungeon, `n` magicians are standing in a line. Each magician has
    an attribute that gives you energy. Some magicians can give you negative
    energy, which means taking energy from you.
    
    You have been cursed in such a way that after absorbing energy from magician
    `i`, you will be instantly transported to magician `(i + k)`. This process
    will be repeated until you reach the magician where `(i + k)` does not exist.
    
    In other words, you will choose a starting point and then teleport with `k`
    jumps until you reach the end of the magicians' sequence, **absorbing all the
    energy** during the journey.
    
    You are given an array `energy` and an integer `k`. Return the **maximum**
    possible energy you can gain.
    
    **Constraints:**
    
      * `1 <= energy.length <= 10 ^ 5`
      * `-1000 <= energy[i] <= 1000`
      * `1 <= k <= energy.length - 1`
    """
    max_energy = None
    for i in range(len(energy)):
        collected_energy = 0
        index = i
        while True:
            if index >= len(energy):
                break
            collected_energy += energy[index]
            index+=k
        if max_energy is None or collected_energy > max_energy:
            max_energy = collected_energy 
    return max_energy
