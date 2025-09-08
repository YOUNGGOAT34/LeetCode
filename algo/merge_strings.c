#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * mergeAlternately(char * word1, char * word2){
   int w1_len=strlen(word1);
   int w2_len=strlen(word2);
   /* 
       a, will point to the current character of word1
       b, will point to the current character of word2
       c will be the index of str
   */
   int a=0,c=0,b=0;

   char *str=(char *)malloc(w1_len+w2_len+1);
   if(!str) return NULL;
   int curr_word=1;

   while(a<w1_len && b<w2_len){
        if(curr_word==1){
            str[c++]=word1[a++];
            curr_word=2;
        }else{
             
             str[c++]=word2[b++];
             curr_word=1;
        }
   }

   while(a<w1_len){
       str[c++]=word1[a++];
   }
  
    while(b<w2_len){
       str[c++]=word2[b++];
   }


  str[c]='\0';
    
   return str;
}