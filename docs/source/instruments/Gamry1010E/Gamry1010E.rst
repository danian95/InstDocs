Gamry 1010E Potentiostat/Galvanostat
====================================

There are two Interface 1010E potentiostats in the chemistry department.
In order to run bipotentiostatic measurements, they need to be
interfaced to one another. See Dr. McCurry for details.

-  `Gamry Application
   Notes <https://www.gamry.com/application-notes/>`__

.. contents:: :local:

Procedures
----------

Voltammetry
~~~~~~~~~~~

Most voltammetric measurements make use of a device called a
potentiostat, which is capable of applying a controlled potential to a
working electrode and measuring the current that passes as a result of
electron transfer to solution species of interest. The potentiostat
contains many internal circuits that allow it to function in this
capacity. The circuits generate and measure potentials and currents.

CV
^^

1. Once desired solutions are prepared, fill the electrochemical cell
   (shot glass) ~ 3/4th full with the blank, add the small stirbar, &
   place on the silver shelf. Slide the shelf under the covering with
   holes for the electrodes and turn on the magnetic stirring. (black
   switch to the right of the cell)
2. Remove all oxygen from solution by bubbling nitrogen gas through the
   electrochemical cell for 3-5 minutes -**NOTE**: make sure the
   nitrogen gas is causing the solution to bubble quite rapidly, but not
   enough to spill any solution
3. While the solution is bubbling, power on the Gamry Potentiostat. The
   switch is in the back, kind of on the bottom right if you are looking
   at the front of the machine.
4. Go to Experiment > Physical Electrochem > Cyclic Voltammetry
5. Set the desired parameters:

   -  Test ID: The name of the experiment.

-  Set the scan parameters as follows: - Initial E (V): 0.8 - Scan Limit
   1 (V): -0.12 - Scan Limit 2 (V): 0.8 - Final E (V): 0.8 - all the
   previous scan parameters are vs Eref

   -  Output file: The name of the file created.
   -  Electrode Area: Will give current (*i*) if the area is set to 1.
      It will give current density (*j*) if the actual area is provided.
   -  Set scan limits: The range of voltages that will be scanned.
   -  Scan Rate: The speed at which scans are done. (20mV/s)
   -  Step Size: The distance in between which measurements are taken.
      (2mV)
   -  Cycles: How many times each point is measured (1 Cycle)
   -  Max Current: Maximum current allowed (To start, set to auto)
   -  Eq Time: Time potentiostat waits before measurement (set to 0
      normally, but 10s is recommended)
   -  1/E Range Mode: Fixed
   -  Expected max V: Maximum voltage anticipated (10V)
   -  Sampling mode: Set to noise reject
   -  All tick boxes should be unchecked

6.  Once bubbling is completed (the instructions say purge with nitrogen
    for 10 minutes, but 3 should suffice… it’s a small “toothpick
    holder”) remove the tube from the solution, but leave it blowing
    nitrogen gas over the solution with minimal ripples so no oxygen
    gets back in.
7.  Insert the electrodes and connect the alligator clips in the
    following order:

    -  Counter electrode: Always connect the “sensor” clip closest to
       the electrode
    -  Reference electrode
    -  Working electrode: Always connect the “sensor” clip closest to
       the electrode

8.  Ensure the electrodes are not touching. The cell is small and the
    clips can slide as the wires settle.
9.  Turn off the magnetic stirring. This will create waves in your data
    in the diffusion limited current region of your CV.
10. Once parameters are set, click “OK” at the top of the screen and
    take a background scan. You should see this run take place with no
    peaks. \*If there are peaks, you will need to polish the working
    electrode with Micropolish Alumina. If the peaks in your blank are
    not resolved, the WE may require sonication.
11. Once run is complete, press F2 on the keyboard and continue further
    runs. (Remember, each time the solution is swapped, you must bubble
    through with nitrogen gas and stir for at least 3 minutes).
12. The reference electrode should be washed between runs with deionized
    water, though this electrode must always remain wet as to not clog
    the pourous glass with the formation of crystals.

LSV
^^^

ASV
^^^

Amperometry
~~~~~~~~~~~

Impedance
~~~~~~~~~

Data Analysis
-------------

The easiest way to visualize data before exporting to a figure is to
work up the data in Gamry Echem Analyst.


