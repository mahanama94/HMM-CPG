## Hidden Markov Model for CPG island detection

The repo contains two approaches for identifying CPG islands for a given sequence
implemented using Python.
1. Using HMMLearn library
2. Without HMMLearn

### Requirements

#### Python 3.5 or higher

https://www.python.org/download/releases/3.0/

#### NumPy
A package for scientific computing using python.

``` pip install numpy ```

http://www.numpy.org/

#### HMMLearn 0.2.1
Simple algorithms and models to learn HMMs (Hidden Markov Models) in Python.
Required only for HMMLearn implementation.

``` pip install hmmlearn ```

https://pypi.org/project/hmmlearn/


### Running
1. HMMLearn

``` python cpg_islands_hmm.py ```

2. Non-HMMLearn
``` python cpg_islands.py```

### Issues

#### Upper Limits
The non-hmm version has been tested for sequences greater than
50,000 characters and depending on the probability values and the sequence
its found to falsely detect/predict state due to probability values
approaching 0 (zero). In a similar manner a false identifications
can occur due to overflows due to scaling up mechanism in the code.

The issue has been fixed for the probability values provided in the
repo by multiplying the probability computations by 4 (refer code).
The optimal value can change depending on the sequence used for testing
(The value in code is optimal value for sequence in big.txt)
This issue however generates a warning from HMMLearn library
in the HMMLearn version as ```untimeWarning: divide by zero encountered in log```

