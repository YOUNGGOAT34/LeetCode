#include <stdio.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    
   char *prefix=(char *)malloc(sizeof(char )*(strlen(strs[0]))+1);

   int i=0;
   while(1){
       char current=strs[0][i];

       if(!current) break;
        
        for(int j=0;j<strsSize;j++){
            if(!strs[j][i] || strs[j][i]!=current){
               prefix[i]='\0';
               return prefix;
            }
        }

        prefix[i]=current;
        i++;

   }

   prefix[i]='\0';

   return prefix;
}