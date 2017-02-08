#include <stdio.h>
int binarySearch(char **argv, char *searchEntry, int start, int end);

int main(int argc, char **argv) {
    char searchEntry[] = "initiallize";

    printf("enter the search entry:\n");
    scanf("%s", searchEntry);

    printf( "%s is at %d\n", searchEntry, binarySearch(argv, searchEntry, 1, argc-1));
    return 0;
}


int binarySearch(char **argv, char *searchEntry, int start, int end) {
    int mid;
    mid = (int)((start + end) / 2);

    printf("start:%d end:%d mid:%d\n", start, end, mid);
    printf("argv[mid]is %s, searchEntry is %s\n\n", argv[mid], searchEntry);

    if (end >= start) {
            if (strcmp(searchEntry,argv[mid]) == 0) {
                return mid;

            }else if (strcmp(searchEntry,argv[mid]) > 0) {
                printf(">\n");
                return binarySearch(argv, searchEntry, mid+1, end);

            }else if (strcmp(searchEntry,argv[mid]) < 0) {
                printf("<\n");
                return binarySearch(argv, searchEntry, start, mid-1);
            }

        }else {
            return -1;
    }
}
