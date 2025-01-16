# Day 12: Hot Springs

## What has to be done

### Ideas for part 1

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

### Ideas for part 2

1. In part 2, we should optimize the process, so as to not generate sequences that are wrong. This should be doable if we manage to implement early stopping.
   - Even with early stopping, this is still too slow. Will have to think about another solution.
2. We should be able to use bits.
   1. Use the length of the string with pipes to obtain the largest number in binary.
   2. Do a `for` loop from it till `0`.
   3. On each iteration you'll have a possibility. Run it through a filter.

The plan of attack then can be as follows:

1. First convert to bits and on each iteration convert to string.
   - This still would not be most efficient (I think), but it serves as a check that the full solution space is covered.
2. Apply bit manipulations instead of converting to string.
   - This still produces a lot of possibilities.
3. Let's try BFS with a list.
   - This yet again seems to be a brute force approach.
4. Maybe we can count the numbers between the largest and the smallest one using again the bit logic.
   - For example, if pattern='?###????????' and num_broken=[3,2,1], then:
   1. Take the length of the patter. => 12
   2. Take the length of the broken groups. => 11101101 => 8
   3. Left-pad pattern to obtain smallest possible number. => 011100001101
   4. Right-pad pattern to obtain highest possible number. => 011101101000
   5. Linearly go through interval and count.
   - Steps 3 and 4 would be tricky. I think the following can work:
     1. Have a function `infer`. It'll take the pattern and `num_broken` and will try to fill in as much as possible groups that may exist.
     2. Apply a minimization and maximization algorithm that will return the smallest and largest possible numbers.

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

### Submit answers for part 2

- [X] Run on input.
  - It will do the job, but it's not as fast as it should.

### Solve using bits and converting them to string

- [X] Make sure using bits still goes through the full space of possibilities.

### Use bit manipulations to check the groups instead of converting to strings

- [X] All tests pass.

### Try BFS with a list

- [ ] All tests pass.

### Submit answer for part 2

- [ ] Run on input.
