#include <stdio.h>
#include <stdlib.h>
//#define DEBUG

int solution[64][2];
int startx = 0 , starty = 0 ;
int board_size = 8;
int use_warns = 1;
int table2[1][1] = { 0 }; // table with all position in  X , Y form
int** table = NULL;
long steps = 0;
int  max_step = 0; //step in solution finder
char moves[8][2] = {	{ 2, 1}, // possible moves
			{ 1, 2},
			{-1, 2},
			{-2, 1},
			{-2,-1},
			{-1,-2},
			{ 1,-2},
			{ 2,-1}

};
int alloc_table(  int rows, int columns  ){

	table  = (int **)malloc(rows * sizeof(int*));
	if(table == NULL ) exit(2);
	for(int i = 0 ; i < rows; i ++){
		table[i] = (int *)malloc(columns * sizeof(int));
		if(table[i] == NULL) exit(2);
	}
	for(int i = 0 ; i < rows; i ++){
		for(int j = 0 ; j < columns; j ++){
			table[i][j] = 0;
		}
	}
	return(0);
}
int rec(int n) { // recursion learning test
	int t_n = n;
	if (t_n > 0) return(t_n-1);
	return(0);

}
int mmoves(int x, int y) { // max lefting moves for a position
	int nmoves = 0;
	int tx, ty;
	for (int i = 0; i < 8; i++) {
		tx = x + moves[i][0];
		ty = y + moves[i][1];
		if (tx >= 0 && tx < board_size && ty >= 0 && ty < board_size) // inside borders
			if (table[tx][ty] == 0) {
				nmoves++;
			}
	}
	return(nmoves);
}
int warnsdorff(int x, int y, int pos) { // return the index of moves[]
	int mmoves_table[8];
	int min_table[8] = { 8,8,8,8,8,8,8,8 };
	int min_index = 0;
	if(use_warns == 0) return(pos);
	for (int i = 0; i < 8; i++) {
		mmoves_table[i] = mmoves(x + moves[i][0], y + moves[i][1]);
	}
	//	printf("\nmoves_table");
	//	for(int i = 0;i <8 ; i++) printf("%d ",mmoves_table[i]);
	for (int i = 0; i <= pos; i++) {
		for (int j = 0; j < 8; j++) {
			if (mmoves_table[j] <= min_table[i]) {
				min_table[i] = mmoves_table[j];
				min_index = j;
			}
		}
		mmoves_table[min_index] = 8;
	}
	//	printf("\nMin_table:");
	//	for(int i = 0 ; i <= pos;i ++) printf("%d ", min_table[i]);
	//	return(min_table[pos]);
	return(min_index);
}
void initialize_table() {
	for (int i = 0; i < board_size; i++)
		for (int j = 0; j < board_size; j++)
			table[i][j] = 8;
}
void print_table() {
	printf("KNIGHT'S TOUR SOLVER \n");
	printf("TABLE\n");
	for (int i = board_size - 1; i >= 0; i--) {
		printf("\n%*d ", 3, i + 1);
		for (int j = 0; j < board_size; j++) {
			if (table[j][i] != 0)	printf("%*d ", 3, table[j][i]);
			else printf("    ");
		}
	}
	//	printf("\n      a   b   c   d   e   f   g   h\n");
	printf("\n      "); for (int i = 0; i < board_size; i++) printf("%c   ", i + 'a');
}
int next(int x, int y, int step) { // return the next posssible move as moves[] index
	int tx, ty, tstep; //local x,y
	tstep = step;
	steps ++;
#ifdef DEBUG
	system("clear");
	print_table();
	if (step > max_step) max_step = step;
	printf("\n\nMax Steps: %d\n", max_step - 1);
	printf("Step: %d\n", step - 1);
	printf("Total test steps: %d\n",steps);
#endif
	for (int i = 0; i < 10000000; i++);

	
	for (int i = 0; i < 8; i++) {
		tx = x + moves[warnsdorff(x, y, i)][0];
		ty = y + moves[warnsdorff(x, y, i)][1];
		if (tx >= 0 && tx < board_size && ty >= 0 && ty < board_size) // inside borders
			if (table[tx][ty] == 0) {
				table[tx][ty] = tstep;
				if (next(tx, ty, tstep + 1)) table[tx][ty] = 0;
				else{
					solution[step-1][0] = tx + 'a';
					solution[step-1][1] = ty + '1';
				       	return(0);
				}
			}
		
//	if ((tstep > (board_size * board_size)&&(x == startx)&&(y == starty))) {
	if ((tstep > (board_size * board_size))) {
		//print_table();
		return(0);
	}

	}
	
	return(1); // no sucess
}



int main(int argc, char* argv[]) {
	//printf("KNIGHT'S TOUR SOLVER \n");
	for(int i = 1 ; i < argc; i ++){
		if(argv[i][0] != '-') argv[i][1] = 'h'; //Error: call Help menu 
		switch(argv[i][1]){
			case 'h':
			fprintf(stderr, "%s OPTS\n"
				"-h 	: help\n"
				"-w 1	: use warnsdorff(default = 1)\n"
				"-s xxx	: board size\n"
				"-p a1	: initial position(dafault = a1\n"
			      ,argv[0]);
			return(0);	
		break;
			case 'w':
			use_warns = atoi(argv[i+1]) ;
			i++;
		break;
			case 's':
			board_size = atoi(argv[i + 1]);
			i++;
		break;		
			case 'p':
			startx = argv[i + 1][0] - 'a';
			argv[i + 1][0] = '0';
			starty = atoi(argv[i + 1]) - 1;// index chess begins in 1 , index array begins in 0
			i++;
		break;
		}
	}
	if(alloc_table(board_size,board_size) == -1 ){
			fprintf(stderr,"Malloc Error\n");
			return(-1);
	}

	//	exit(0);
	//	initialize_table();
	table[startx][starty] = 1;
	//next(x, y, 2);
	//print_table();
	//	printf("\nWarnsdorff index: %d", warnsdorff(x,y,1));
	solution[0][0] = startx + 'a';
	solution[0][1] = starty + '1';
	if(next(startx, starty, 2)==0){
		for(int i = 0 ; i < 64; i++) printf("%c%c\n",solution[i][0],solution[i][1]);
		return(0);
	}
	printf(" ### Solution not found ###");
	return(1);

}
