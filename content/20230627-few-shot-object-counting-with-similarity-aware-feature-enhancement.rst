Few-shot Object Counting with Similarity-Aware Feature Enhancement
###################################################################
:date: 2023-06-27 16:26:27
:author: Minghua Zheng
:category: Seminars
:tags: Algorithms: Image recognition and understanding (object detection, and algorithms (including transfer, and un-supervised learning), Benchmark testing, categorization, Computer vision, Finite element analysis, Focusing, formulations, Image recognition, low-shot, Machine learning architectures, segmentation), self-, semi-, Target recognition, Trainin
:slug: few-shot-object-counting-with-similarity-aware-feature-enhancement
:summary: Minghua Zheng's Journal Club session where he will talk about the paper "Few-shot Object Counting with Similarity-Aware Feature Enhancement".

On this week's Journal Club session, Minghua Zheng will talk about the paper entitled "Few-shot Object Counting with Similarity-Aware Feature Enhancement".

------------

This work studies the problem of few-shot object counting, which counts the number of
exemplar objects (i.e., described by one or several support images) occurring in the query
image. The major challenge lies in that the target objects can be densely packed in the
query image, making it hard to recognize every single one. To tackle the obstacle, we
propose a novel learning block, equipped with a similarity comparison module and a feature
enhancement module. Concretely, given a support image and a query image, we first derive a
score map by comparing their projected features at every spatial position. The score maps
regarding all support images are collected together and normalized across both the
exemplar dimension and the spatial dimensions, producing a reliable similarity map. We
then enhance the query feature with the support features by employing the developed point-
wise similarities as the weighting coefficients. Such a design encourages the model to
inspect the query image by focusing more on the regions akin to the support images,
leading to much clearer boundaries between different objects. Extensive experiments on
various benchmarks and training setups suggest that we surpass the state-of-the-art
methods by a sufficiently large margin. For instance, on a recent large-scale FSC-147
dataset, we surpass the state-of-the-art method by improving the mean absolute error from
22.08 to 14.32 (35\%↑). Code has been released in https://github.com/zhiyuanyou/SAFECount.

|

Papers:

- Z. You, K. Yang, W. Luo, X. Lu, L. Cui, X. Le, `"Few-shot Object Counting with Similarity-Aware Feature Enhancement"
  <https://doi.org/10.1109/WACV56688.2023.00625>`__, 2023, 6304--6313


**Date:**  2023/06/30 |br|
**Time:** 14:00 |br|
**Location**: 2J124 & online

.. |br| raw:: html

	<br />
