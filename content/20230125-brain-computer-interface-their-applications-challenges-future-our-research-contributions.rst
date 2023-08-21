Brain-Computer Interface & their Applications, Challenges, Future & Our research contributions
##############################################################################################
:date: 2023-01-25 15:19:27
:author: Yar Muhammad
:category: Seminars
:tags: brain–computer interface (BCI),electroencephalography (EEG), rehabilitation,systematic literature review
:slug: brain-computer-interface-their-applications-challenges-future-our-research-contributions
:summary: Yar Muhammad's Journal Club session where he will talk about a paper "Brain-Computer Interface & their Applications, Challenges, Future & Our research contributions"

This week on Journal Club session Yar Muhammad will talk about some of his work in a presentation entitled "Brain-Computer Interface & their Applications, Challenges, Future & Our research contributions".
The abstract of the presentation could be found below, together with supporting papers.

------------

An electroencephalography (EEG)-based brain–computer interface (BCI) is a
system that provides a pathway between the brain and external devices by
interpreting EEG. EEG-based BCI applications have initially been developed for
medical purposes, with the aim of facilitating the return of patients to normal
life. In addition to the initial aim, EEG-based BCI applications have also
gained increasing significance in the non-medical domain, improving the life of
healthy people, for instance, by making it more efficient, and collaborative
and helping them develop themselves.

There are many challenges in EEG-based BCI development and research as the
cross-subject classification of motor imagery data. Due to the highly
individualized nature of EEG signals, it has been difficult to develop a
cross-subject classification method that achieves sufficiently high accuracy
when predicting the subject’s intention. In 2020, we proposed a multi-branch 2D
convolutional neural network (CNN) that utilizes different hyperparameter
values for each branch and is more flexible to data from different subjects.
Our model, EEGNet Fusion, achieves 84.1% and 83.8% accuracy when tested on the
103-subject eegmmidb dataset for executed and imagined motor actions,
respectively. The model achieved statistically significantly higher results
compared with three state-of-the-art CNN classifiers: EEGNet, ShallowConvNet,
and DeepConvNet. However, the computational cost of the proposed model is up to
four times higher than the model with the lowest computational cost used for
comparison. 

In our recent studies, we improve the model with a 5-branches 2D CNN that
employs several hyperparameters for every branch and this network is more
adaptable to data from various subjects. The proposed model achieved promising
results on three publicly available datasets, the EEG Motor Movement/Imagery,
the BCI Competition IV 2a, and the BCI Competition IV 2b dataset. The eegmmidb
dataset is used for testing for actual and imagined motor activity and our
newly proposed model, EEGNet Fusion V2, achieves 89.6% and 87.8% accuracy,
respectively.

Moreover, the proposed model outperforms on the BCI Competition IV-2a and 2b
datasets with an accuracy of 74.3% and 84.1% for the cross-subject
classifications, respectively. Compared with the EEGNet, ShallowConvNet,
DeepConvNet, and EEGNet Fusion, the proposed model’s accuracy is higher.
However, the proposed model has a bit higher computational cost, i.e., it takes
around 3.5 times more computational time per sample than the EEGNet Fusion.

|

Papers:

- K. Roots, Y. Muhammad, N. Muhammad, `"Fusion Convolutional Neural Network for Cross-Subject EEG Motor Imagery Classification"
  <https://doi.org/10.3390/computers9030072>`__,  2020, Computers, 9, 72
- K. Varbu, N. Muhammad, Y. Muhammad, `"Past, Present, and Future of EEG-Based BCI Applications"
  <https://doi.org/10.3390/s22093331>`__,  2022, Sensors, 22, 3331


**Date:** 2023/01/27 |br|
**Time:** 14:00 |br|
**Location**: online

.. |br| raw:: html

	<br />
