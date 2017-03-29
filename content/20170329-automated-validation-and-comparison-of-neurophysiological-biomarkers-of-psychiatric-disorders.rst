Automated validation and comparison of neurophysiological biomarkers of psychiatric disorders
#############################################################################################
:date: 2017-03-29 15:22:49
:author: Christoph Metzner
:category: Seminars
:tags: Computational psychiatry, 
:slug: automated-validation-and-comparison-of-neurophysiological-biomarkers-of-psychiatric-disorders
:summary: Christoph Metzner's journal club session on the automatic validation and comparison of neurophysiological biomarkers of psychiatric disorders.

Research on psychiatric disorders has gradually shifted its focus from complex clinical phenotypes towards the identification of biomarkers and endophenotypic measures. Computational approaches have gained significantly more attention over the last years, and this has led to the emergence of 'Computational Psychiatry' as an independent discipline. Computational modelling of biomarkers promises to more readily shed light on the mechanisms underlying disorders and to facilitate the discovery of novel medications [1].

However, in order to develop a computational model, scientists need to have an in-depth understanding of the current, relevant experimental data, the current state of computational modeling and the state-of-the-art of statistical testing. Based on this knowledge, they have to choose the appropriate criteria with which the model predictions and experimental observations will be compared [2]. In a field where both the number of experimental and computational studies grows rapidly, as is the case for psychiatry, this becomes more and more impracticable. Omar et al. therefore proposed a framework for automated validation of scientific models, SciUnit [3].

Here, we propose to adopt this framework for the computational psychiatry community and to collaboratively build common repositories of experimental observations, computational models, test suites and tools. As a case in point, we have implemented test suites for auditory steady-state response deficits in schizophrenic patients, which are based on observations from several experimental studies [4,5,6], and we demonstrate how existing computational models [6,7] can be validated against these observations and compared against each other. We have included sets of observations from three experimental studies, which concur on most findings but also disagree on some. This allows us to demonstrate the usefulness of our approach in highlighting and clarifying existing, potentially conflicting, experimental data. We have included computational models that not only comprise biophysically detailed as well as abstract models, but that also differ in implementation (native Python vs. Genesis vs NeuroML2), in order to demonstrate the flexibility of the approach. Furthermore, this additionally allows us to showcase the ability of the framework to compare models against each other based on a set of experimental observations. Furthermore, our approach enables us to assess the variability of the produced model output, and therefore the robustness of the findings, by generating a distribution of model instances where certain parameters, such as the precise timing of noise inputs (however, not the strength and type of noise) or the precise connectivity (however, not the underlying distribution of connections) vary, which then are used to produce a distribution of model outputs. This can inform on the robustness of the findings and can also be compared against the variability of experimental observations.

----

1. Siekmeier, P.: Computational modeling of psychiatric illnesses via well-defined neurophysiological and neurocognitive biomarkers. Neuroscience & Biobehavioral Reviews 57: 365-380, 2015.
2. Gerkin, R.C. and Omar, C.: NeuroUnit: Validation Tests for Neuroscience Models. Front. Neuroinform. Conference Abstract: Neuroinformatics 2013. doi: 10.3389/conf.fninf.2013.09.00013
3. Omar, C., Aldrich, J., and Gerkin, R.C.: Collaborative infrastructure for test-driven scientific model validation. In CompanionProceedings of the 36th International Conference on Software Engineering, ACM, 2014.
4. Kwon J.S., O’Donnell B.F., Wallenstein G.V., Greene R.W., Hirayasu Y., Nestor P.G., Hasselmo M.E., Potts G.F., Shenton M.E., and McCarley R.W..: Gamma frequency–range abnormalities to auditory stimulation in schizophrenia. Archives of General Psychiatry, 56(11):1001–1005, 1999.
5. Krishnan, G.P., Hetrick, W.P., Brenner, C.A., Shekhar, A., Steffen, A.N., and O’Donnell, B.F.: Steady state and induced auditory gamma deficits in schizophrenia. Neuroimage, 47(4):1711–1719, 2009.
6. Vierling-Claassen, D., Siekmeier, P., Stufflebeam, S., and Kopell, N.: Modeling GABA alterations in schizophrenia: a link between impaired inhibition and altered gamma and beta range auditory entrainment. Journal of Neurophysiology, 99(5):2656–2671, 2008.
7. Metzner, C., Schweikard, A. and Zurowski, B.: Multi-factorial modeling of impairment of evoked gamma range oscillations in schizophrenia. Frontiers in Computational Neuroscience, 10, 2016. 

**Date:** 31/03/2017 |br|
**Time:** 16:00 |br|
**Location**: LB252

.. |br| raw:: html

    <br />
