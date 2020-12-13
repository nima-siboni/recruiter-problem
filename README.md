# recruiter-problem

The recuiter problem (also known as the marriage problem, the sultan's dowry problem, the fussy suitor problem, and secretary problem) is a problem that demonstrates a scenario involving optimal stopping theory.

The basic version of the problemn can be stated as follows [[1]](https://en.wikipedia.org/wiki/Secretary_problem): 

* There is a single position to fill.
* There are n applicants for the position, and the value of n is known.
* The applicants, if seen altogether, can be ranked from best to worst unambiguously.
* The applicants are interviewed sequentially in random order, with each order being equally likely.
* Immediately after an interview, the interviewed applicant is either accepted or rejected, and the decision is irrevocable.
* The decision to accept or reject an applicant can be based only on the relative ranks of the applicants interviewed so far.
* The objective of the general solution is to have the highest probability of selecting the best applicant of the whole group. This is the same as maximizing the expected payoff, with payoff defined to be one for the best applicant and zero otherwise.
* A candidate is defined as an applicant who, when interviewed, is better than all the applicants interviewed previously. Skip is used to mean "reject immediately after the interview". Since the objective in the problem is to select the single best applicant, only candidates will be considered for acceptance. The "candidate" in this context corresponds to the concept of record in permutation.

## Optimal stopping point and 1/e law

The optimal strategy for the recruitment problem is a stopping rule: here, the first n candidates are rejected, and after that the candidate who is better than the previous candidates is chosen. Intuitively, one can understand this strategy as explained here: at the beginning the recruiter does not know about the quality of the possible candidates, i.e. it does not know what is the score of a "good" candidate, and what is the score of a "bad" candidate. This problem can be elevated by interviewing more and more candidates; exploring more candidates lead to better understanding of what scores are available in the market. So to gain information about the score distribution of the candidates, the recruiter should interview as many candidates as it can (which means rejecting as many candidates as it can, in our problem). Although many rejections leads to good understanding of market, unfortunately it does not leave many candidates to choose from. In other words, if you reject most of the candidates, you have a good idea of what is a good candidate, but not many candidates are left for you to choose from. 


In this project a python code is developed to find the optimal stopping point (stopping point refers to how many applicant are rejected immediately). The method used here is simple Monte-Carlo method.
## results 


## requirements
```
python3
numpy 
matplotlib
```

## running the code
The script is executed with
```
python3 MC.py
```
and produces a graph which shows the probability for finding the best candidate based on the stopping point. 

The key inputs (hard-coded!) are:
```
N_CANDIDATES -- number of candidates that we expect for this job, and
N_HIRINGS -- number hiring trials to find the probabilities (ideally should be infinite).
``` 
Other inputs are:
```
CHOOSING_METHOD -- which can be 'max' or 'mean'. 
It refers to the method with which information is obtained from the data before the stopping point.

DISTRIBUTION -- which can be 'uniform', 'normal', 'pareto'.
It refers to the distribution of the candidates.
```

Here is an example for a hiring process where the expected number of applicants are 
```
N_HIRINGS = 5_000
N_CANDIDATES = 20
CHOOSING_METHOD = 'max'
DISTRIBUTION = 'random'
```

![](results.png)
