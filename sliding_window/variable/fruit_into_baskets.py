class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        picked=defaultdict(int)
        max_fruits=0
        starting_tree=0

        for stopping_tree in range(len(fruits)):

            picked[fruits[stopping_tree]]+=1

            while len(picked)>2:
                picked[fruits[starting_tree]]-=1
                if not picked[fruits[starting_tree]]:
                    del picked[fruits[starting_tree]]
                starting_tree+=1

            max_fruits=max(max_fruits,stopping_tree-starting_tree+1)

        return max_fruits

    


            


        