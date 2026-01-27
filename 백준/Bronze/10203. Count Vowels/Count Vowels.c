#include <stdio.h>

int main() {
    int n;
    char word[100];
    scanf("%d", &n);
    for (int i=0;i<n;i++){
        int total=0;
        scanf("%s", word);
        for (int i=0;word[i]!='\0';i++){
        if (word[i]=='a' || word[i]=='e' || word[i]=='o' || word[i]=='i' || word[i]=='u') {total++;}
        }
        printf("The number of vowels in %s is %d.\n", word, total);
    }
    return 0;
}