class NumberContainers:

    def __init__(self):
        self.data=defaultdict(int)
        self.rev_map=defaultdict(SortedSet) # reverse map,,number->indexes

    def change(self, index: int, number: int) -> None:
        old_number=self.data[index]

        if old_number!=0: 
            self.rev_map[old_number].remove(index)

            if not self.rev_map[old_number]:
                del self.rev_map[old_number]


        self.data[index]=number

        self.rev_map[number].add(index)


    def find(self, number: int) -> int:
            if number in self.rev_map and self.rev_map[number]:
                return self.rev_map[number][0]

            return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)