from typing import List



def get_damage(vc, i):
    if i not in vc.keys():
        return 0
    return i*vc[i]


def get_score(vc, i):
    score = get_damage(vc, i)
    score -= get_damage(vc, i-1)
    score -= get_damage(vc, i+1)
    score -= get_damage(vc, i-2)
    score -= get_damage(vc, i+2)
    return score

    

def mask(vc,i):
    vc.pop(i-1,None)
    vc.pop(i-2,None)
    vc.pop(i+1,None)
    vc.pop(i+2,None)




def maximumTotalDamage(power: List[int]) -> int:
    """
    A magician has various spells.
    
    You are given an array `power`, where each element represents the damage of a
    spell. Multiple spells can have the same damage value.
    
    It is a known fact that if a magician decides to cast a spell with a damage of
    `power[i]`, they **cannot** cast any spell with a damage of `power[i] - 2`,
    `power[i] - 1`, `power[i] + 1`, or `power[i] + 2`.
    
    Each spell can be cast **only once**.
    
    Return the **maximum** possible _total damage_ that a magician can cast.    
    
    **Constraints:**
    
      * `1 <= power.length <= 10 ^ 5`
      * `1 <= power[i] <= 10 ^ 9`
    """
    vals = list(set(power))
    val_counts = {val : power.count(val) for val in vals}
    val_scores = {val : get_score(val_counts, val) for val, count in val_counts.items()}
    selected_vals = []
    while True:
        if len (val_scores.keys()) ==0:
            break
        max_key = max(val_scores, key=val_scores.get)
        selected_vals.append(max_key)
        val_scores.pop(max_key)
        mask(val_scores,max_key)
    total = sum([get_damage(val_counts, val) for val in selected_vals])
    return total

