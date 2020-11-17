# liquid-haskell

You can read more on what this program do [here](https://osprogramadores.com/desafios/d05/)

## How to install

You will need to install [stack](https://docs.haskellstack.org/en/stable/README/#how-to-install) and [Z3](https://github.com/Z3Prover/z3).

After that, just run `stack build` to build and `stack run <filepath>` to run.

## About LiquidHaskell

> LiquidHaskell (LH) refines Haskell's types with logical predicates that let you enforce critical properties at compile time.
> - [Official site](https://ucsd-progsys.github.io/liquidhaskell-blog/)

## What LH proves about this project?

### Termination

LH ensures that this program always halts. Of course, LH cannot prove this for all programs, since it would contradict the [Halting Problem](https://en.wikipedia.org/wiki/Halting_problem), but for this program in particular it can be proved.

### Less partial functions

Haskell has notable partial functions that can cause runtime errors, like division by zero and the `head` function, that take the first element of the list. If the list is empty, you will get an exception. LH ensures, for example, that division by zero never happens and that `head` always receive nonempty lists. For example

	let employees = -- receive employees from user
	let first = head employees
	print first

will not be checked, since a user can pass an empty list.

### Sort preserves length

If you use `sortBy` to sort a list with `n` items, then you will receive a list with `n` items.

### Group of non-empty list returns non-empty list

If you use `groupBy` to group a non-empty list, you will receive a list with at least one item.

------------

**Disclaimer:** Malformed JSON has deliberately not been checked for performance reasons. Therefore it can cause a runtime error.
