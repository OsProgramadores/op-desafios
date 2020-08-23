#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <float.h>

#define MAX_SURNAMES	5000
#define MAX_NAMES	1000
#define MAX_NAME_SIZE	30
#define MAX_AREAS	30
#define GLOBAL_INDEX	0


// Global vars.
char nome[MAX_NAME_SIZE];
float salario;
char area[3];
float mean = 0;
int count;

// Array of structs to stores the stats of areas
// Index 0 will be the global one.
struct stats_area{
	char name[MAX_NAME_SIZE];
	unsigned long employees;
	float max_value;
	int max_value_count;
	float min_value;
	int min_value_count;
	double total_value;
	float avg_value;
	char max_name[MAX_NAMES][MAX_NAME_SIZE];
	char min_name[MAX_NAMES][MAX_NAME_SIZE];
}stats[MAX_AREAS];

struct stats_surname{
	char surname[MAX_NAME_SIZE];
	char names[MAX_NAMES][MAX_NAME_SIZE];
	float max_value;
	int max_value_count;
	long count;
}surnames[MAX_SURNAMES];

// Stores the list os surnames. In fact we have onlye 4917 surnames.
char surname_list[MAX_SURNAMES][MAX_NAME_SIZE];

// Stores areas codes in 2 char form 
// where index of area_index means 
// the index of area in stats array.
char area_index[MAX_AREAS][3];

// Returns the index os a area code. 
// If not found add that area code in the array.
int get_area_index(char area[3]){
	int count = 0;
	while(area_index[count][0] != '\0' ){
		if(area[0] == area_index[count][0] && area[1] == area_index[count][1])
			return(count);
		count++;
	}
	area_index[count][0] = area[0];
	area_index[count][1] = area[1];
	return(count);
}

void initialize_vars(){
	for(int i = 0; i < MAX_AREAS; i++){
		stats[i].name[0] = '\0';
		stats[i].employees = 0;
		stats[i].max_value = 0;
		stats[i].max_value_count = 0;
		stats[i].min_value = FLT_MAX;
		stats[i].min_value_count = 0;
		stats[i].total_value = 0;
		stats[i].avg_value = 0;
		area_index[i][0] = '\0';
	}
	for(int i = 0 ; i < MAX_SURNAMES; i++){
		surnames[i].surname[0] = '\0';
		surnames[i].max_value = 0;
		surnames[i].max_value_count = 0;
		surnames[i].count = 0;
		surname_list[i][0] = '\0';
	}
	// Area "00" means global. 
	get_area_index("00");
}

// Print formated results os stats data.
void print_results(){
	int pos = 1;
	unsigned long most_employees = 0;
	unsigned long least_employees = ULONG_MAX;
	char name[2 * MAX_NAME_SIZE + 1] = "\0";
	// Print global stats.
	for(int i = 0 ; i <= stats[0].max_value_count;i++)
		printf("global_max|%s|%.2f\n",stats[0].max_name[i],stats[0].max_value);
	for(int i = 0 ; i <= stats[0].min_value_count;i++)
		printf("global_min|%s|%.2f\n",stats[0].min_name[i],stats[0].min_value);
	printf("global_avg|%.2f\n",stats[0].total_value/stats[0].employees);
	// Print area stats
	while(stats[pos].employees != 0){
		for(int i = 0 ; i <= stats[pos].max_value_count;i++)
			printf("area_max|%s|%s|%.2f\n",stats[pos].name,stats[pos].max_name[i],stats[pos].max_value);
		for(int i = 0 ; i <= stats[pos].min_value_count;i++)
			printf("area_min|%s|%s|%.2f\n",stats[pos].name,stats[pos].min_name[i],stats[pos].min_value);
		printf("area_avg|%s|%.2f\n",stats[pos].name,stats[pos].total_value/stats[pos].employees);
		if(stats[pos].employees > most_employees)
			most_employees = stats[pos].employees;
		if(stats[pos].employees < least_employees)
			least_employees = stats[pos].employees;
		pos++;
	}
	// Print most , least employees.
	pos = 0;
	while(stats[pos].employees != 0){
		if(most_employees == stats[pos].employees)
			printf("most_employees|%s|%ld\n",stats[pos].name,stats[pos].employees);
		pos++;
	}
	pos = 0;
	while(stats[pos].employees != 0){
		if(least_employees == stats[pos].employees)
			printf("least_employees|%s|%ld\n",stats[pos].name,stats[pos].employees);
		pos++;
	}
	// Print surname stats.
	pos = 1;
	while(surnames[pos].count != 0){
		if(surnames[pos].count > 1){
			for(int i = 1 ; i <= surnames[pos].max_value_count;i++)
				printf("last_name_max|%s|%s %s|%.2f\n",surname_list[pos],surnames[pos].names[i],surname_list[pos],surnames[pos].max_value);
		}
		pos++;
	}
}

// Update global and area stats.
void max_min_avg(int area_id){
	char *sobrenome = surname_list[count];
	stats[area_id].employees ++;
	// Test Max.
	if(salario == stats[area_id].max_value) {
		stats[area_id].max_value_count++;
		sprintf(stats[area_id].max_name[stats[area_id].max_value_count],"%s %s",nome,sobrenome);
	}
	if(salario > stats[area_id].max_value) {
		stats[area_id].max_value = salario;
		stats[area_id].max_value_count = 0;
		sprintf(stats[area_id].max_name[stats[area_id].max_value_count],"%s %s",nome,sobrenome);
	}
	// Test Min.
	if(salario == stats[area_id].min_value) {
		stats[area_id].min_value_count++;
		sprintf(stats[area_id].min_name[stats[area_id].min_value_count],"%s %s",nome,sobrenome);
	}
	if(salario < stats[area_id].min_value) {
		stats[area_id].min_value = salario;
		stats[area_id].min_value_count = 0;
		sprintf(stats[area_id].min_name[stats[area_id].min_value_count],"%s %s",nome,sobrenome);
	}
	// Update average.
	stats[area_id].total_value += salario;
}

// Update surname stats.
void update_surnames(int index){
	if(salario == surnames[index].max_value){
		surnames[index].max_value_count++;
		sprintf(surnames[index].names[surnames[index].max_value_count],"%s",nome);
	}
	if(salario > surnames[index].max_value){
		surnames[index].max_value = salario;
		surnames[index].max_value_count = 1;
		sprintf(surnames[index].names[surnames[index].max_value_count],"%s",nome);
	}
	surnames[index].count ++;
}

// Get and process every json entry in the file 
int process_entries(FILE *fp){
	char buffer[20000] ;
	count = 1;
	char comma;
	int filling_sur_array = -1;
	int buff_size;
	int buff_pos = 0;
	fscanf(fp,"%*[^\[]\[",NULL);
	do{
		fscanf(fp,"%[^}]}%c%n",buffer,&comma,&buff_size);
		buff_pos = 0;
		// Just get the name at each 4917 entries,
		// for others 4916 the name repeats.
		if(count == 4917 || count == 1){ 
			count = 1;
			//get new name
			//buff_pos = 6;
			while(buffer[buff_pos++] != 'e' );
			buff_pos += 3 ;
			sscanf(buffer + buff_pos, "%[^\"]",nome);
			buff_pos = 0;
			if(count == 4917)
				filling_sur_array = 0;
		}
		// Just get surnames for first 4917 entries,
		// after this the surnames starts to repeat.
		if(filling_sur_array){
			while(buffer[buff_pos++] != 'e' );
			buff_pos += 3 ;
			while(buffer[buff_pos++] != ':' );
			buff_pos++;	
			sscanf(buffer + buff_pos, "%[^\"]",surname_list[count]);
		}
		// Search for AREA backwards.
		buff_size -= 2;
		while(buffer[buff_size--] != ':' );
		buff_size += 3;
		area[0] = buffer[buff_size++] ;
		area[1] = buffer[buff_size];
		// Search for salary.
		while(buffer[buff_size--] != 'o' );
		buff_size += 4;
		sscanf(buffer + buff_size, "%f",&salario);	
		// Update the global stat.
		max_min_avg(GLOBAL_INDEX);
		// Update area stats
		max_min_avg(get_area_index(area));
		update_surnames(count);
		count++;
	// While we get a comma after "close bracket" continue 
	}while(comma == ',');
	// Get area strings.
	int ret;
	do{
		fscanf(fp,"%*[^{]",NULL);
		ret = fscanf(fp,"%*[^:]:\"%[^\"]",area);
		fscanf(fp,"%*[^:]:\"%[^\"]",stats[get_area_index(area)].name);
	}while(ret == 1);
}

int main(int argc, char *argv[]){
	FILE *fp;
	if(argc != 2){
		fprintf(stderr, "You must specify the json file\n");
		return(-1);
	}
	fp = fopen(argv[1], "r");
	if(fp == NULL){
		perror("Error opening file ");
		return(-1);
	}
	initialize_vars();	
	process_entries(fp);
	fclose(fp);
	print_results();
	return(0);
}
