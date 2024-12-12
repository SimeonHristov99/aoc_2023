# Day 11: Cosmic Expansion

## What has to be done

Try to solve part 1 naively by doing the steps as they are outlined in the task:

1. Expand the universe.
2. Get all the points.
3. Find the Manhattan distance between them (I think it should be equivalent).

For part 2, the brute force approach cannot be used. We can utilize the already written code and rewrite the logic for the expansion so that it becomes parametrized. Idea:

1. Parse the input.
2. Get the coordinates of the initial points.
3. Change the behavior of the `expand` function:
   1. It should take a list of coordinates, a parameter with the coefficient of expansion, a list with the indices of the empty rows and a list with the indices of the empty columns.
   2. It should return a list of the coordinates in the expanded universe.
   3. Having the indices of the empty rows and columns, one approach to go forward would be to sort the coordinates and increase the corresponding ones after the index of the empty row/column.

A question might arise *Why didn't you make it like that (i.e. parametrized and optimal) in the first place?*. The answer is that that would have been over-engineering. We don't want it. We follow the principle of addressing the problem at hand. Only when there is a need to change something to fulfil another goal, we do the change and account for it.

## Part 1

### Create a plan of attack

- [X] Main steps outlined and vision for the end result is written down.

### Expand the input after parsing

#### Parse the input

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

#### Expand the universe

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

### Get all the galaxies as coordinates

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Test that the function `main` reports the number of galaxies found in each input.
- [X] Commit all changes.

### Calculate the Manhattan distance between them

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

### Working part 1

#### Count each pair once

- [X] Add failing tests.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

#### Take the sum of the lengths

- [X] Make tests for the function `part1` fail by adding the requirement for the sum of the lengths.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

#### Submit answers

- [X] Run on input.
- [X] In case brute force is not enough, brainstorm next steps:
  - Calculate the Manhattan distance between counting how many special cells.
  - Brute force worked.

## Part 2

### Create a plan of attack for part 2

- [X] Main steps outlined and vision for the end result is written down.

### Parametrize expand

- [X] Make tests fail.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

### Move the common logic for parts 1 and 2 into a new function and test it with different levels of expansion

- [X] Make tests fail.
- [X] Make tests pass.
- [X] Look at the code you've written and try to identify any edge cases that are not tested.
- [X] `pre-push` hook passes.
- [X] Commit all changes.

### Submit answers for part 2

- [ ] Run on input.
