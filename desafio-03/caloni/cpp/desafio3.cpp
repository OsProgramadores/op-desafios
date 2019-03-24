#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

typedef unsigned long long int LongInteger;


bool is_palindrome(LongInteger number)
{
    string snumber = to_string(number);
    for( auto begin = snumber.begin(), end = snumber.end() - 1; begin != end; ++begin, --end )
    {
        if( *begin != *end )
            return false;
    }
    return true;
}


int main()
{
    LongInteger begin, end;
    cout << "type two numbers separated by space and hit enter: ";
    cin >> begin >> end;
    cout << "the palindromes between " << begin << " and " << end << " are:\n";
    for( LongInteger i = min(begin, end); i < max(begin, end); ++i )
        if( is_palindrome(i) )
            cout << i << endl;
    if( is_palindrome(max(begin, end)) )
        cout << end << endl;
}

