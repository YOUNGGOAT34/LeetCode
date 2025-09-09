#include<stdio.h>

int maxProfit(int* prices, int pricesSize) {
   int max_profit=0;

   for(int i=0;i<pricesSize;i++){
        
        for(int j=i+1;j<pricesSize;j++){

            int profit=prices[j]-prices[i];
            if(profit>max_profit){
                 max_profit=profit;
            }

        }
   }

   return max_profit;
}