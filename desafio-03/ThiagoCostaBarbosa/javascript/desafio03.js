function palindrome(max, min = 1)
{
  let array = [];
  max = parseInt(max);
  min = parseInt(min);

  //check the type of parameters
  if (typeof max != 'number' ||
      typeof max != 'number')
  {
    return [];
  }
  //go through interval
  for (min; min <= max; min++)
  {
    //check if it's palindrome
    if (min == min.toString()
                  .split('')
                  .reverse()
                  .join(''))
    {
      //add palindrome number to array of palindromes
      array.push(min);
    }
  }
  return array;
}

palindrome(3010, 3000).forEach( i => { console.log(i) });
