class ProductOfNumbers:

    def __init__(self):
       
        self.products=[]

    def add(self, num: int) -> None:
        if num:

            self.products.append(self.products[-1]*num) if self.products else self.products.append(num)
        else:
            self.products=[]

        

    def getProduct(self, k: int) -> int:
        if len(self.products)<k:
            return 0

        elif k==len(self.products):
            return self.products[-1]

        else :
            return self.products[-1]//self.products[-1-k]
       



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)