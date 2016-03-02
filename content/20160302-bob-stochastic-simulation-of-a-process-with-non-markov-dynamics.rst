BoB: stochastic simulation of a process with non-Markov dynamics
################################################################
:date: 2016-03-02 10:19:16
:author: Maria Schilstra
:category: Seminars
:tags: 
:slug: bob-stochastic-simulation-of-a-process-with-non-markov-dynamics
:summary: Maria Schilstra's journal club session on BoB: stochastic simulation of a process with non-Markov dynamics.

Myosin-V is a molecular motor that 'walks' along the ubiquitous actin tracks in cells, and drags membranous vesicles (which can be filled with, for instance, neurotransmitters) to their destination (such as synapses). ATP hydrolysis fuels the motion. The actual stepping, where one leg is swung and put in front of - or occasionally behind - the other, is very fast. However, the intervals between the steps, where both feet are firmly stuck to the track, are much longer, and distributed randomly - at least when observed in vitro. In vivo, where there is no feedback mechanisms that keeps the force on the motor constant, the cargo is connected via an elastic tether, which stretches - and creates extra pull - every time the motor steps forward. The bulky cargo has to move through the highly viscous cytosol, and follows much more slowly. Thus, the pull on the motor decreases in the interval between steps. Importantly, the stepping rate of the motor is dependent on the force it experiences. To simulate this process properly, it is necessary to incorporate the fact that the stepping probability may change a lot in the interval between two steps, and that is what I did when I wrote BoB. The results of this exercise are published `here <http://rsif.royalsocietypublishing.org/content/3/6/153.short>`__ (J. Royal Soc. Interface).

**Date:** 04/03/2016 |br|
**Time:** 16:00 |br|
**Location**: LB252

.. |br| raw:: html

    <br />
