An Evolutionary Ensemble Learning for Diagnosing COVID-19 via Cough Signals
############################################################################
:date: 2023-03-01 15:44:29
:author: Mohammad Tayarani-Najaran
:category: Seminars
:tags: COVID-19,Evolutionary algorithms,Optimizatio
:slug: an-evolutionary-ensemble-learning-for-diagnosing-covid-19-via-cough-signals
:summary: Mohammad Tayarani-Najaran's Journal Club session where he will talk about a paper "An Evolutionary Ensemble Learning for Diagnosing COVID-19 via Cough Signals"

This week on Journal Club session Mohammad Tayarani-Najaran will talk about his paper "An Evolutionary Ensemble Learning for Diagnosing COVID-19 via Cough Signals".

------------

Objective The spread of the COVID-19 disease has caused great concern around the world and
detecting the positive cases is crucial in curbing the pandemic. One of the symptoms of
the disease is the dry cough it causes. It has previously been shown that cough signals
can be used to identify a variety of diseases including tuberculosis, asthma, etc. In this
paper, we proposed an algorithm to diagnose via cough signals the COVID-19 disease.
Methods The proposed algorithm is an ensemble scheme that consists of a number of base
learners, where each base learner uses a different feature extractor method, including
statistical approaches and convolutional neural networks (CNN) for automatic feature
extraction. Features are extracted from the raw signal and some transforms performed it,
including Fourier, wavelet, Hilbert-Huang, and short-term Fourier transforms. The outputs
of these base-learners are aggregated via a weighted voting scheme, with the weights
optimised via an evolutionary paradigm. This paper also proposes a memetic algorithm for
training the CNNs in the base-learners, which combines the speed of gradient descent (GD)
algorithms and global search space coverage of the evolutionary algorithms. Results
Experiments were performed on the proposed algorithm and different rival algorithms which
included a number of CNN architectures in the literature and generic machine learning
algorithms. The results suggested that the proposed algorithm achieves better performance
compared to the existing algorithms in diagnosing COVID-19 via cough signals. Conclusion
This research showed that COVID-19 could be diagnosed via cough signals and CNNs could be
employed to process these signals and it may be further improved by the optimization of
CNN architecture.

|

Papers:

- M. Najaran, `"An Evolutionary Ensemble Learning for Diagnosing COVID-19 via Cough Signals"
  <https://doi.org/10.1016/j.imed.2023.01.001>`__, 2023, Intelligent Medicine.


**Date:**  2023/03/03 |br|
**Time:** 14:00 |br|
**Location**: online

.. |br| raw:: html

	<br />
