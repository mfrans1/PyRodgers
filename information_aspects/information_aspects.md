# Chapter 2: Information Aspects

Inverse problems can be deceptively tricky, often being ill-conditioned, ill-posed, and often non-linear. To gain appreciation of these nuances, we need to first understand the density and characteristics of information in signals. 

## 2.1 Formal Statement of the Problem

Inverse problems are a question of setting up and solving a set of linear (or non-linear) equations, in the present of experimental error in its parameters. 

To examine the information content of the indirect measurement, we consider the measurements to be assembled into a *measurement vector*, namely $\vec{y}$. The measurement vector $\vec{y}$ and the *state vector* of unknowns $\vec{x}$ are related through this set of equations, usually through the relation of some forward model (which may or may not be linear), modulated by some measurement error $\epsilon$

$$
\vec{y} = \mathbf{F}(\vec{x}) + \epsilon
$$

To construct a forward model we must of course know how the measuring device works, and understand how the measurement relates to the variable we retrieve. 

A forward model could be as simple as the Planck function, relating the temperature of an object to the radiation it emits.

### Weighting Function Matrix

For the purpose of examing the information content of a measurement, it is most convenient to consider a linear problem. A linearization of a forward about some reference state $\vec{x_0}$ can be adequate for this purpose, provided the forward model is linear within the error bounds of the retrieval. 

$$
\vec{y} - \mathbf{F}(\vec{x_0}) = \frac{\partial\mathbf{F}(\vec{x})}{\partial\vec{x}}(\vec{x} - \vec{x_0}) + \epsilon = \mathbf{K}(\vec{x} - \vec{x_0}) + \epsilon
$$

This defines the weighting function matrix $\mathbf{K}$, which may not be square. Each element of $\mathbf{K}$ is the partial derivative of the forward model element with respect to the state vector element.

### Vector Spaces

The concept of linear vector spaces is useful in the context of lineaer equations. 

The *state space* or the model space is a vector space of dimension $n$, within which each conceivable state is represented by a point, or equivalently a vector from the origin to that point. 

The *measurement space* (or data space) is a vector space of dimension $m$ in which every conceivable measurement is likewise represented by a point or a vector. 

Consequently, we can consider measurement to be a mapping from the state space to the measurement space, and the inverse problem to be a mapping from the measurement space onto the state space. 

This makes the weighting function matrix $\mathbf{K}$ to be $(m \times n)$ and represents the forward mapping from state to measurement space (with error $\epsilon$). 

*The mapping if fuzzy, to an extent determined by the error measurement statistics*

Imagine a case in which a state space is defined in two dimensions. If three measurements are made, corresponding to three vectors $\vec{k_1}$, $\vec{k_2}$ and $\vec{k_3}$, the measurements $\vec{y_1}$, $\vec{y_2}$ and $\vec{y_3}$ are the orthogonal projections of $\vec{x}$ onto $\vec{k}$'s. Trivially the measurement is overconstrained.
![](./data/state_v_measurement.png)
In this example the measurement space is three dimensional, but the state space maps onto a subspace of the measurement space (a 2D plane), as one measurement is always a function of the other two. In the absence of measurement error, there will be points in the measurment space that fall out of the subspace (observe diagram). There correspond to impossible state vectors. 