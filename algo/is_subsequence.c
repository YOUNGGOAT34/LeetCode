#include<stdio.h>
#include<stdbool.h>
#include<string.h>

bool isSubsequence(char* s, char* t) {
   int lenS=strlen(s);
   int lenT=strlen(t);

   if(strcmp(s,"")==0) return true;
   if(lenS>lenT) return false;

   int j=0;

   for(int i=0;i<lenT;i++){
        if(s[j]==t[i]){
             if(j==lenS-1) return true;

             j++;
        }

        if(j>lenS) break;
   }

   return false;
}