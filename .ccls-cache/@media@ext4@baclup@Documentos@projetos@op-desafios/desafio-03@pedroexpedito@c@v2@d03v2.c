// Com ajuda do Frederico Pissara


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <libgen.h>

static int isPalindrome( char * );

int main( int argc, char *argv[] )
{
  if ( argc != 2 )
  {
    fprintf( stderr, "Usage: %s <string>\n"
                     "Where <string> is an arbitrary size string.\n\n",
      basename( *argv ) );
    return EXIT_FAILURE;
  }

  argv++;

  printf( "A string \"%s\" %sé um palíndromo.\n",
    *argv, isPalindrome( *argv ) ? "" : "não " );

  return EXIT_SUCCESS;
}

int isPalindrome( char *p )
{
  size_t size;
  char *q;

  size = strlen( p );

  // Condição especial: strings vazias NÃO são
  // palíndromos. Altere a condição para `size < 2`,
  // se você pretende que strings com apenas 1 caracter
  // não sejam consideradas como palindromos.
  if ( ! size )
    return 0;

  // q aponta para o último caracter da string.
  q = p + size - 1;

  while ( p < q )
    if ( *p++ != *q-- )
      return 0;

  return 1;
}
