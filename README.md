# find_my_number
---
### Manage virtual env
#### Create a venv
```
make create-venv
```
#### update a venv
```
make update-venv
```
#### Run the solution
```
make run
```
---
### Details about the solution
We can think of this problem as a matrix board (with dimensions as m X n) with left-lowest (0, n-1) and right-lowest(m-1, n-1) cells as invalid - i.e. knight moves shall not yield those two cells.
We need to check boundary conditions as well (including the two cells above) i.e. the knight move shall not go beyond the matrix dimensions i.e. row should be confined between 0 and m-1 while col should be between 0 and n-1

We will define printable format of the matrix by defining respective string function. 
The init function has flexibility to take an empty matrix with no values but just the dimensions (i.e. last param as None).
We are also checking the provided dimensions and input matrix data and then raising error if there is inconsitency.

The next knight move is random selection from possible moves from that point. This may lead to coming back to the same point more than once in the sequence. We can constrain it by maintaining a hash in future implementations where repeat can be constrained to 0 or some random value less than length of the sequence.

We can use a random series as input in main.py to generate the sequences. Currently we are using (0, 0).
It can be further extended to take a "key" as input and then find the index of it and then proceed with next step.
We have raised exceptions, in case, a negative or out of range value is used.

The requirements file for venv is empty since we do not need any extra libraries for this task.
We are using logging with info. For prod, we can have error et al as well with proper details in a well-defined structure - which can later be utilized by some ELK setup

---

### All about testing this solution
We are using unittest here since we need to use what comes with standard Python setup therefore not using nose2 or pytest.
We can add regression testing as well in next iteration. 
To define and run the test cases, we execute the test script as below
```
make test
```
