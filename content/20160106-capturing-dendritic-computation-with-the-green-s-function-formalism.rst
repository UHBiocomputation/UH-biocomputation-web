Capturing dendritic computation with the Green’s function formalism
###################################################################
:date: 2016-01-06 14:44:56
:author: Willem Wybo
:category: Seminars
:tags: Computational modelling, Human Brain Project, Dendritic computation
:slug: capturing-dendritic-computation-with-the-green-s-function-formalism
:summary: Special journal club session - Willem Wybo from the Human Brain Project at EPFL will speak about his work on enhancing the Green's function formalism to study neuronal integration, dendritic compartmentalization and interactions between synaptic inputs.

Neurons are spatially extended structures with an elaborate dendritic tree that integrates spatio-temporal input patterns. To model this integration, researchers have relied on compartmental simulations of the cable equation, where space is discretized in many equipotential compartments. However, this approach is computationally expensive and obfuscates the interactions among distant synapses .

The Green's function (GF) formalism can potentially solve these issues: it is conceptually simple, as the complicated spatio-temporal interactions are captured in a system of temporal kernels, and provides a simulation paradigm that scales independently of the morphological complexity. However, the computational cost scales quadratically in the number of inputs. Historically, the GF formalism was abandoned because of this reason, along with the fact that it required computationally costly convolutions and the belief that is was restricted to linear membranes.

In this talk, I will show how all aforementioned pitfalls can be circumvented. First, I will outline how the system can be transformed so that it scales linearly in the number of input locations. Second, I will show that convolutions can be re-expressed as simple differential equations. Third, I will discuss the inclusion of non-linear membrane currents and related, how this 'sparsified' GF formalism reduces to the canonically used 2nd order finite difference approximation.

I will also briefly outline how this new simulation algorithm for neurons can be implemented and discuss possible use cases in which computational advantage over the classic methods is expected.

**Date:** 15/01/2016 |br|
**Time:** 16:00 |br|
**Location**: LB252

.. |br| raw:: html

    <br />

