Class-Balanced Loss Based on Effective Number of Samples
#########################################################
:date: 2021-06-02 11:10:58
:author: Minghua Zheng
:category: Seminar
:tags: recognition: detection; categorization; retrieval; computer vision theory; deep learning
:slug: class-balanced-loss-based-on-effective-number-of-samples
:summary: Minghua Zheng's Journal Club session where he will talk about a paper "Class-Balanced Loss Based on Effective Number of Samples"

This week on Journal Club session Minghua Zheng will talk about a paper "Class-Balanced Loss Based on Effective Number of Samples".

------------

With the rapid increase of large-scale, real-world datasets, it
becomes critical to address the problem of longtailed data
distribution (i.e., a few classes account for most of the data, while
most classes are under-represented). Existing solutions typically
adopt class re-balancing strategies such as re-sampling and re-
weighting based on the number of observations for each class. In this
work, we argue that as the number of samples increases, the additional
benefit of a newly added data point will diminish. We introduce a
novel theoretical framework to measure data overlap by associating
with each sample a small neighboring region rather than a single
point. The effective number of samples is defined as the volume of
samples and can be calculated by a simple formula
(1-β^n)/(1-β), where n is the number of samples and β
∈ [0, 1) is a hyperparameter. We design a re-weighting scheme that
uses the effective number of samples for each class to re-balance the
loss, thereby yielding a class-balanced loss. Comprehensive
experiments are conducted on artificially induced long-tailed CIFAR
datasets and large-scale datasets including ImageNet and iNaturalist.
Our results show that when trained with the proposed class-balanced
loss, the network is able to achieve significant performance gains on
long-tailed datasets.

|

Papers:

- Y. Cui, M. Jia, T. Lin, Y. Song, S. Belongie, `"Class-Balanced Loss Based on Effective Number of Samples"
  <https://doi.org/10.1109/CVPR.2019.00949>`__,  2019, 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 9260--9269


**Date:** 2021/06/04 |br|
**Time:** 14:00 |br|
**Location**: online

.. |br| raw:: html

	<br />
