The effect of regularity, synchrony, and STD on deep cerebellar nuclei in physiological conditions and during downbeat nystagmus
################################################################################################################################
:date: 2015-11-11 16:40:36
:author: Julia Goncharenko
:category: Seminars
:tags: Computational modelling, Cerebellum, Purkinje cells
:slug: the-effect-of-regularity-synchrony-and-std-on-deep-cerebellar-nuclei-in-physiological-conditions-and-during-downbeat-nystagmus
:summary: Julia Goncharenko's journal club session on the effect of regularity, synchrony, and STD on deep cerebellar nuclei in physiological conditions and during downbeat nystagmus.

It was previously believed, that the reason for downbeat nystagmus (DBN, the symptom of CACNA1a gene mutation) is a lack of inhibition, and that it could be alleviated by an increase of the overall firing rate. It is postulated that 4AP (4-aminopyridine, non-selective voltage-dependent K+ channel blocker) enhances Purkinje cell activity in the flocculus and restores inhibition of anterior canal pathways to a normal level [Glasauer 2005]. But this theory has been disproved by electrophysiological experiments on tg/tg mice cerebellum slices showing that therapeutic concentrations of 4-AP do not increase the inhibitory drive of cerebellar Purkinje cells. Therefore, 4-AP restores the severely diminished precision of pacemaking in Purkinje cells of episodic ataxia type two (EA2, channelopathie, affecting the PQ calcium channel-encoding gene,CACNA1A) mutant mice to normal level by prolonging and increasing the action potential after hyperpolarization [Alvin˜a and Khodakhah, 2010]. In other word, the main consequence of tg/tg chanelopathy is an increase of spike irregularity.

The recent electrophysiological findings encouraged German scientists to reconsider their previous findings by investigating the potential
effect of changing the cerebellar output of Purkinje cells (PC, class of GABAergic neurons located in the cerebellum which plays a fundamental role in controlling motor movement) regularity in the vestibular nuclei in a modelling study [Glasauer 2011]. Their first result was that only regularity together with synchrony would have a significant effect on the postsynaptic target neuron. But these results are incompatible with their system-level model, as well as with the current view on the nature of DBN. 

Neither the population level model [Glasauer et al, 2008] nor the conductance-based model of a single neuron [Glasauer et al, 2011] appeared able to explain the electrophysiological findings.

The main assumption is that their model didn't give the correct results due to not taking into an account the effect of short-term depression (STD). In my findings, there is no significant difference in data with the presence or absence of STD. But difference in firing rate with the presence and absence of STD becomes significant for higher noise levels. I assume, that such a small difference in noise levels between wild-type and tg/tg could be explained taking into account the way, how known CV values for wild-type and tg/tg mice were converted to noise. Noise levels were obtained after building a dependency graph of CV form
noise. This dependency is linear, and it is not the case for real cells, because current model is simplified.

**Date:** 13/11/2015 |br|
**Time:** 16:00 |br|
**Location**: LB252

.. |br| raw:: html

    <br />
