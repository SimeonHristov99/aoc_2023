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

- [ ] Add failing tests.

- [ ] Make tests pass.
- [ ] Look at the code you've written and try to identify any edge cases that are not tested.
- [ ] `pre-push` hook passes.
- [ ] Commit all changes.

### Make it work for the second example

- [ ] Add failing tests.
- [ ] Make tests pass.
- [ ] Look at the code you've written and try to identify any edge cases that are not tested.
- [ ] `pre-push` hook passes.
- [ ] Commit all changes.

### Make it work for the third example

- [ ] Add failing tests.
- [ ] Make tests pass.
- [ ] Look at the code you've written and try to identify any edge cases that are not tested.
- [ ] `pre-push` hook passes.
- [ ] Commit all changes.

### Make it work for the forth example

- [ ] Add failing tests.
- [ ] Make tests pass.
- [ ] Look at the code you've written and try to identify any edge cases that are not tested.
- [ ] `pre-push` hook passes.
- [ ] Commit all changes.

### Make it work for the fifth example

- [ ] Add failing tests.
- [ ] Make tests pass.
- [ ] Look at the code you've written and try to identify any edge cases that are not tested.
- [ ] `pre-push` hook passes.
- [ ] Commit all changes.

### Make it work for the sixth example

- [ ] Add failing tests.
- [ ] Make tests pass.
- [ ] Look at the code you've written and try to identify any edge cases that are not tested.
- [ ] `pre-push` hook passes.
- [ ] Commit all changes.

### Submit answers for part 1

- [ ] Run on input.

## Part 2

### Create a plan of attack for part 2

- [ ] Main steps outlined and vision for the end result is written down.

### Submit answers for part 2

- [ ] Run on input.
