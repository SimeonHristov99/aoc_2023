# Day 12: Hot Springs

## What has to be done

In Part 1, the main goal is to create a function that can do the logic for a single line. Then, that function will be applied to every line. We know the length of the target string, so we have an upper limit. We could use that length and the numbers to form all possibilities and then we'll filter using what we already have. My idea is to use a recursive depth-first search with caching.

1. The recursive function can have the following parameters:
   1. The resulting string which initially is empty.
   2. The starting index from which we're checking whether the current string is valid and whether it is a full group.
   3. The current index that we are on.
   4. An iterator to the list with the groups.
   5. An iterator on the list with the springs.
2. Base cases:
   1. If the current index is out of bounds and the list with groups is empty, return `1`.
   2. If the current index is out of bounds and the list is not empty, return `0`.
3. General case:
   1. If the current character is `?` and the current substring is valid and a full group, recurse after adding `.` to the result, calling `next` on the iterator of the list and resetting the index for the substring.
   2. If the current character is `?` and the current substring is valid, recursively add the calls after adding `#` and `.` to the result.
   3. If the current character is `?`, return `0`.
   4. If the current substring is valid and a full group and the next character is not `#` and the current string does not end with `#`, recurse after calling `next` and resetting the index for the substring.
   5. If the current substring is a full group and the next character is `#` and the current string ends with `#`, return `0`.
   6. If the current character is not `?` and the current substring is valid and not a full group, recurse after adding it to the result.

The will be several calls when all the values in the resulting string are `.`. An option to handle these is to compare the hex values of the current elements in the caching dictionary.

The above was my initial idea, but it was really hard to implement it. Instead, we can use a recursive process to generate all possibilities and check every single one of them. The main difference with the above approach is that we're checking the state after generating a candidate and not building the string piece by piece. The steps would be as follows:

1. If we're output of bounds, exit with 1 if the generated string is a working combination, else 0.
2. If the current character we're sitting on is a ?, then count the possibilities when adding . and add them to the possibilities of adding #.

In part 2, we should optimize the process, so as to not generate sequences that are wrong. This should be doable if we manage to implement early stopping.

- I couldn't manage to solve this and had to look up the solution. It turned out to be *really* straightforward:

Both Part 1 and Part 2 share the same logic - recursion:

1. Base cases:
   1. If there are no springs left:
      1. And there are no pipes left, we return `1`. The reason is that we know that there is always going to be at least one consecutive group of broken pipes, i.e. in the list will never be empty. If we have an empty list, that means that we've found at least one such group, so we return `1`.
      2. And there are broken pipes left, we return `0` as that means that we have not fulfilled the pattern.
   2. If there are no pipes left (but the list of springs is not empty):
      1. And there are no broken pipes in the remaining springs, we return `1` since that means that again, at some previous point we have seen at least one consecutive group of broken pipes.
      2. And there are still some pipes in the remaining springs, we return `0` as we cannot account for them.
2. General cases: We now know that there is at one group of broken pipes and at least one pipe. Using recursion we only handle the first group and first pipe. We treat the question mark both as a working and as a broken pipe by including it in both cases:
   1. Treating the first pipe as a working one. If the first pipe is a dot (`.`) (working by definition) or `?` (working by assumption), we just skip over that pipe and continue, i.e. we repeat the recursion starting from the next pipe and do not change the list with broken pipes.
   2. Treating the first pipe as a broken one. If the first pipe is a `#` (broken by definition) or `?` (broken by assumption) that this can be the first group if broken pipes, so we check for that. The conditions for recursing are:
      1. The first pipe is a `#` or `?`.
      2. And there are at least `num_broken[0]` pipes in `pattern`.
      3. And none of the the first `num_broken[0]` pipes are working.
      4. And:
         1. `pattern[num_broken[0]]` is the end of `pattern` (there are no pipes after that).
         2. Or `pattern[num_broken[0]]` is a working pipe (`.`).
    If those conditions are met, then we have the first consecutive group of broken pipes, so we skip over `num_broken[0] + 1` characters in `pattern` and go over to the next group of broken pipes.

Part 2 includes the addition of memoization (i.e. caching). The cache-key is the `pattern` and the `num_broken` lists. If this is present in the cache, we return it, otherwise, we add the resulting value before returning it.

## Part 1

### Create a plan of attack for part 1

- [X] Main steps outlined and vision for the end result is written down.

### Parse input

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

### Make it work for the first example

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

### Make it work for the second example

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

### Make it work for the third example

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

### Make it work for the forth example

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

### Make it work for the fifth example

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

### Make it work for the sixth example

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

### Submit answers for part 1

- [X] Run on input.

## Part 2

### Create a plan of attack for part 2

- [X] Main steps outlined and vision for the end result is written down.

### Alter the process so that processing is faster

- [X] Add a function that checks whether we should continue to generate new sequences.
- [X] Add the `expand` function.
- [X] Make sure processing is fast on the sample.

### Look up solution and add explanation

- [X] Look up and understand.
- [X] Write down an explanation.
- [X] Confirm that it runs on the sample and input.

### Submit answers for part 2

- [X] Submit, commit and push.
