class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            counts = sorted(Counter(word).items())
            anagrams[tuple(counts)].append(word)
        return list(anagrams.values())

