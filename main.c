
# include <stdio.h>
# include <string.h>

int main( )
{

	FILE *filePointer ;

	char data[50]
		= "This is sample data";
    gets(data);

	filePointer = fopen("myfile.txt", "w") ;
	if ( filePointer == NULL )
	{
		printf( "File not found" ) ;
	}
	else
	{

		printf("file opened.\n") ;
		if ( strlen ( data) > 0 )
		{

			fputs(data, filePointer) ;
			fputs("\n", filePointer) ;
		}

		fclose(filePointer) ;


	}
	return 0;
}
