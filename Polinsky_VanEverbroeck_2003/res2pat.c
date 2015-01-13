#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

float semvector [3] [3] = {
{1, 0, 0},
{0, 1, 0},
{0, 0, 1},
}; 

int distf(void);
int findint(char *);

char title[90], date[90], undef[90], pats[90], ins[90], outs[90];
char line[120], dit[120];
int pat, in, out, i, j, k, l;
float dist, bestdist, temp;
int bestpointer;
float raw[80];
FILE *f1;

main (int argc, char *argv[])  {

char *p;
int i, j, k;

if ((f1 = fopen(argv[1], "r" )) == NULL) {
	printf("\nERROR: Cannot open file.\n");
	exit(0);
}

fgets(title, 81, f1);
fgets(date, 81, f1);
fgets(undef, 81, f1);
fgets(pats, 81, f1);
fgets(ins, 81, f1);
fgets(outs, 81, f1);
fgets(undef, 81, f1);
fgets(undef, 81, f1);
fgets(undef, 81, f1);

printf("SNNS pattern definition file V1.4\n");
printf("%s\n\n", date);
printf("%s", pats);
printf("%s", ins);
printf("%s\n", outs);

pat = findint(pats);
in = findint(ins);
out = findint(outs);

for (i=0 ; i<pat; i++) {

	// comment line
	fgets(line, 81, f1);
	printf("%s", line);
	
	// input lines
	for (j=0 ; j<in; j++) {
		fscanf(f1, "%s", dit);
		printf("%s ", dit);
	}
	printf("\n");
	
	// output lines
	for (k=0; k<out; k++) {
		// for (l=0; l<3; l++) {
			fscanf(f1, "%f", &raw[k]);
		// }
	}
	distf();
	printf("\n");
	fgets(line, 10, f1);
}

} // end main()	

/* This section computes Euclidean calculation of error */
int distf(void) {
int i,j,k;
bestdist = 100000.0;
bestpointer = 0;

for (j=0; j<3; j++) {
	dist = 0.0;

	for (k=0; k<3; k++) {
	      temp = semvector[j][k] - raw[k];
	      dist += temp * temp ;
	}

	// dist = sqrt(dist);       
	if (dist < bestdist) {
		// printf("---> %d : %f \n", j, dist);
		bestdist = dist;
		bestpointer = j;
	}
}
	
// now print it out
for ( k=0; k<3; k++) {
	// printf("%3.1f ", semvector[bestpointer][k]);
	printf("%d ", (int) semvector[bestpointer][k]);
}

} // end distf


/* get the number which is in a char line */
int findint(char * text) {
int i = 0;
int j = 0;

while (text[i] != '\0') {
	if (isdigit(text[i])) {
		text[j] = text[i];
		j++;
	} else {
	}
	i++;
}

text[j] = '\0';
i = atoi(text);

return(i);

} // end findint()
