/* 
*	Program: Assignment 2, replcat.c
*	Date: 2/17/2015
*	Author: Lee Nardo
*   Instructor: Ekstrand
*	Lecture: UNIX Programming
*/

/* LIBRARIES */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

// SET BUFFER SIZE
#define BUFFER_SIZE 1024

/* MAIN */
int main (int argc, const char * argv[])
{
	/* VARIABLES */
	char buffer[BUFFER_SIZE]; // BUFFER
	int length /* diff */;

	// FIND DIFFERENCES AND SIZE
	if (argv[1] > argv[2]) {
		length = strlen(argv[1]);
		//diff = strlen(argv[2]) - strlen(argv[1]);
		//printf("%d\n", diff);
	} else {
		length = strlen(argv[2]);
		//diff = strlen(argv[1]) - strlen(argv[2]);
		//printf("%d\n", diff);
	}


	// CHECK FOR FILE AT END OF COMMAND
	if (argc == 3) {
		/* READ STANDARD INPUT */
		while (fgets(buffer, BUFFER_SIZE, stdin)) {
			char * buf0 = strstr(buffer, argv[1]);
			if (buf0 != NULL) {
				// MEMORY COPY
				//memmove(buffer, argv[2], diff);
				// REPLACEMENT
				buf0 = strncpy(buf0, argv[2], length);

			}
			// print back output to display
			fputs(buffer, stdout);
		}
		if (feof(stdin)) {
			return 0;
		} else {
			perror(argv[0]);
			return 1;
		}
	// OPEN FILE STREAM
	} else {
		int i;
		for (i = 3; i < argc; i++) {
			/* OPEN FILE STREAM */
			FILE *fin = fopen(argv[i], "r+"); /* open row 3 4 */
			while (fgets(buffer, BUFFER_SIZE, fin) != NULL) {
				// get pointer to search string
				char * buf = strstr(buffer, argv[1]);
				if (buf != NULL) {
					// REPLACEMENT
					buf = strncpy(buf, argv[2], length);
				}
				// print out buffer
				printf("%s", buffer);
			}

			/* CLOSE FILE STREAM */
			fclose(fin);
		}
	}

	return 0;
}