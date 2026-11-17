# Bayes' Theorem

A lot of Rodgers 2000 relies on Bayesian inference, and the communication of two random variables (the state and measurement space). It's pretty important, therefore, to have an understanding of Bayes' Theorem beyond the basics. Rodgers gives a breakdown, these are those notes. 

Probability density is a scalar-valued function, in our case a a function of the state vector or the measurement vector. 

$P(\vec{x})$ is the prior probability distribution function of the state vector $\vec{x}$. This means the quantity $P(\vec{x})d\vec{x}$ is the probability before the measurement that $\vec{x}$ lies in the multidimensional volume $(\vec{x}, \vec{x} + d\vec{x})$, expressing quantitatively our knowledge of $\vec{x}$ before the measurement is mad. It is normalized such that $\int P(\vec{x})d\vec{x}=1$. 

$P(\vec{y})$ is the prior probability distribution function of the measurement, with a similar meaning as $P(\vec{x})$. This is the probability distribution function of the measurement *before it is made*.

$P(\vec{x},\vec{y})$ is the joint distribution of vectors $\vec{x}$ and $\vec{y}$. Meaning that $P(\vec{x},\vec{y})d\vec{x}d\vec{y}$ is the probability that $\vec{x}$ lies in $(\vec{x}, \vec{x} + d\vec{x})$ **and** $\vec{y}$ lies in $(\vec{y}, \vec{y} + d\vec{y})$.

$P(\vec{y}|\vec{x})$ is the conditional probability of $\vec{y}$ given $\vec{x}$, meaning that $P(\vec{y}|\vec{x})d\vec{y}$ is the probability that $\vec{y}$ lies in $(\vec{y}, \vec{y} + d\vec{y})$ for a given $\vec{x}$.

Inversely, $P(\vec{x}|\vec{y})$ is the opposite, the state given a measurement. Note that this is the question we try to ask in inverse problems regarding the atmosphere (typically). 
