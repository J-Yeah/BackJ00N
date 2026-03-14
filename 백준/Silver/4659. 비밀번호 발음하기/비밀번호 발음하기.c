#include <stdio.h>
#include <string.h>

int main() {
    char word[20];
    int exist, count_i,count_j, acc, cnt; 
    
    while (1){
        exist = count_i = count_j = cnt = 0;
        acc = 1;
        scanf("%s", word);
        if (strcmp(word, "end")==0) return 0;
        for (int i=0;i<strlen(word);i++){
            if (word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u'){
                exist = 1;
                count_i ++;
                count_j = 0;
            }
            else {
                count_i = 0;
                count_j ++;;
            }
            if (count_i>=3 || count_j>=3){
                cnt = 0;
                break;
            }
            else cnt = 1;
            
            if (word[i]==word[i+1]){
                if (word[i]!='e' && word[i]!='o') acc=0;
            }
        }
        if (acc && exist && cnt) printf("<%s> is acceptable.\n", word);
        else printf("<%s> is not acceptable.\n", word);
    }
}