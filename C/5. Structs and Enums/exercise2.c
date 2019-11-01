// Small Triangles, Large Triangles "https://www.hackerrank.com/challenges/small-triangles-large-triangles/problem"

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


typedef struct triangle {
	int a;
	int b;
	int c;
} triangle;


void sort_by_area(triangle* tr, int n) {
    // Creating a array s to store the volumes p to help calculate the volumes
    float s[n], p;
    // temp1 to store intermediary values for sorting volume
    int temp1;
    // to store the new temporary sorted array list of sides
    triangle temp2[n];

	// Calculate the volume of triangles and store in s
    for (int i=0; i<n; i++) {
        p = (tr[i].a + tr[i].b + tr[i].c) / 2.0;
        // sqrt kinda messes things up so removing that
        s[i] = (p * (p - tr[i].a) * (p - tr[i].b) * (p - tr[i].c));
    }

    // Bubble Sort
    for (int i=0; i<n; i++) {
        for (int j=0; j<n-i-1; j++) {
            if (s[j] > s[j+1]) {
                // Sorting the volumes of s
                temp1 = s[j];
                s[j] = s[j+1];
                s[j+1] = temp1;

                // Using those indexes to sorting the triangle list
                temp2[j] = tr[j];
                tr[j] = tr[j+1];
                tr[j+1] = temp2[j];
            }
        }
    }
}


int main() {
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
    free(tr);
	return 0;
}
