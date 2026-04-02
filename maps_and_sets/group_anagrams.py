class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        groups=defaultdict(list)

        for word in strs:
            count=[0]*26

            for c in word:
                count[ord(c)-ord('a')]+=1

            count=tuple(count)

            groups[count].append(word)

        return list(groups.values())