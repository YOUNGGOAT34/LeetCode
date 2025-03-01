class Solution:
     def findLongestCommonSubsequence(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        # Build the DP table for LCS
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Reconstruct the LCS from the DP table
        longestCommonSubsequence = []
        i, j = len1, len2
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                longestCommonSubsequence.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        
        # Reverse to get the correct order
        longestCommonSubsequence.reverse()
        return ''.join(longestCommonSubsequence)
    
     def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        ans = []
        longestCommonSubsequence = self.findLongestCommonSubsequence(str1, str2)
        
        p1, p2 = 0, 0
        for c in longestCommonSubsequence:
            # Add all non-LCS characters from str1
            while p1 < len(str1) and str1[p1] != c:
                ans.append(str1[p1])
                p1 += 1
            # Add all non-LCS characters from str2
            while p2 < len(str2) and str2[p2] != c:
                ans.append(str2[p2])
                p2 += 1
            # Add the LCS character
            ans.append(c)
            p1 += 1
            p2 += 1
        
        # Add remaining characters from str1 and str2
        ans.append(str1[p1:])
        ans.append(str2[p2:])
        return ''.join(ans)

        