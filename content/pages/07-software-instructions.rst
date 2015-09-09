Instructions for simulators
###########################
:status: hidden
:slug: 07-software-instructions

Competitive Learning Application
--------------------------------

#. unzip the file
#. cd into competitivelearning
#. run with "java -cp ./classes application.Launcher"


Hopfield Net simulator
----------------------

#. Save "UHNetSim.zip" file  in your computer and unzip it.
#. Open a console (Select Run and type "cmd") and make sure your current directory is "UHNetSim".
#. Type: java NetSim.
#. Choose "Begin a new network" and click "Next".
#. Enter "Network size" of 100 say and click "Next".
#. Select "Create a new training set" and click "Finish".
#. Check out the toolbar buttons in the three windows by moving the cursor over them.
#. In the "Training Set" window draw a "T" by clicking the cells.
#. In the "Network state" window, train the network.
#. Check all patterns are stable.
#. Corrupt the "T" in the "Network state" window and run one iteration repeatedly and watch as the "T" reemerges.
#. Do the same but this time select "Run to convergence".
#. Add another pattern to the training set and check that it is learnt.
#. Try out some noisy versions of the trained patterns.
#. Add a third pattern and experiment.
#. In the "Training set" window get rid of all your patterns and create 10 random patterns with "Pattern bias" 0.5 (equal number of 1's and -1's).
#. Check if they are learnt.
#. In the "Test Patterns" window, generate a set of test patterns with Hamming Distane of 5, for example.
#. Make a test pattern current network state.
#. Mismatched units are displayed as gray blocks.
#. Run to convergence and compare them again.
#. Do the same test for other test patterns.
#. Try another set of test patterns with different Hamming Distance.
#. Create a new network of size 9 and train it with a pattern.
#. From the "Network state" window display the network's state transition diagram.
#. Select "Attraction" to display the number of states attracted by each attractor state.
#. Click one of the attractors and see which state it is by looking at the "Network state" window.
#. Display a new network dynamic using asynchronous random (replace) update rule.
#. Overload the network and observe the dynamics.
