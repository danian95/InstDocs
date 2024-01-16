Separation of Urinary Compounds by High Performance Liquid Chromatography
=========================================================================

Theory
++++++
Liquid chromatography involves the partitioning of an analyte between two
phases, a mobile phase and a stationary phase.  The chemical identities of these
phases dictates the type of chromatography being performed:

+------------------------+---------------------------------+-----------------------------+---------------------------+
| Type of Chromatography | Stationary Phase                | Mobile Phase                | How Separation Occurs     |
+------------------------+---------------------------------+-----------------------------+---------------------------+
| Adsorption             | solid polar material like       | various depending on        | Competitive equilibria    |
|                        | silica or alumina               | relative strengths of       | where stronger mobile     |
|                        |                                 | solvents and solutes        | phase drives solutes off  |
|                        |                                 |                             | stationary phase: too     |
|                        |                                 |                             | strong yields no          |
|                        |                                 |                             | separation; too weak      |
|                        |                                 |                             | yields no elution.        |
+------------------------+---------------------------------+-----------------------------+---------------------------+
| Partition              | solid core has liquid layer     | ‘normal’ phase has a        | Species dissolve between  |
|                        | coated or chemically bound;     | nonpolar mobile phase (more | bound and mobile liquids. |
|                        | must be immiscible with mobile  | polar column). ‘reversed’   | A higher affinity for     |
|                        | phase                           | phase has a polar mobile    | mobile phase yields rapid |
|                        |                                 | phase (less polar column)   | elution.  Higher affinity |
|                        |                                 |                             | for bound yields slower   |
|                        |                                 |                             | elution.                  |
+------------------------+---------------------------------+-----------------------------+---------------------------+
| Ion-Exchange           | cross-linked polymer beads with | ionic buffer solutions      | Competitive equilibria    |
|                        | charged groups (anionic or      |                             | between analytes and      |
|                        | cationic forms available)       |                             | buffer components for     |
|                        |                                 |                             | charged sites on          |
|                        |                                 |                             | stationary phase.         |
+------------------------+---------------------------------+-----------------------------+---------------------------+
| Size Exclusion         | polymer beads with internal     | any liquid that does not    | Species are separated     |
|                        | pores of tightly regulated size | dissolve the beads nor      | purely on size as they    |
|                        |                                 | react analytes              | traverse pores. Larger    |
|                        |                                 |                             | species elute first as    |
|                        |                                 |                             | they enter fewer pores.   |
+------------------------+---------------------------------+-----------------------------+---------------------------+

As illustrated by this listing, several different types of chromatography are
possible.  All of them share some common attributes.  A sample is injected at
the head of a column and driven through by a mobile phase that is usually
pumped at moderate to high pressures.  It passes a stationary phase and
partitions between the two phases according some degree of separation.  The
sample elutes from the tail of the column and solutes are passed by some form
of detector.  Final output is sent to integrator or computer for display.

As with GC, the area under a peak is proportional to concentration.  For sharp
peaks and carefully controlled flow rates, peak heights will also be
proportional to concentration.  In either case, a calibration curve is the
method of quantitation.

In this experiment, the separation of urinary metabolites will be performed by
reversed phase chromatography.  The stationary phase packing will be small
beads saturated with a chemically bound octadecyl hydrocarbon group (|C18|).
Nonpolar components, which have a high affinity for the |C18| environment, elute
with relatively long retention times whereas more polar materials, including
ionic species, will elute early.  This experiment illustrates how five
clinically important urinary compounds (uracil, uric acid, xanthine,
allopurinol, and nicotinamide) can be separated and determined.  The separation
is achieved via isocratic elution (same mobile phase throughout) with
ultraviolet detection. The order of elution is the same as the order of listing
of the five species.

Experimental
++++++++++++

Apparatus
---------

* Liquid Chromatograph (:doc:`/instruments/Agilent1260InfinityII/docs`) with 25-μL
  sample injection system, UV (254 nm) detection, 30 cm × 4 mm |C18| column or
  whatever is currently available.
 
* Volumetric flasks, six 100 mL, one 10 mL

* Pipets, one 5 mL, four 4 mL, four 3 mL, four 2 mL, four 1 mL
 
* Mohr pipet, 2 mL

* Nalgene membrane filter, 0.2 μL
 
* Several syringe filters

* Centrifuge

Chemicals
---------

* Stock solutions of 

  - Uracil, 2.43 mg/100 mL
  - Uric Acid, 11.74 mg/100 mL

    .. attention::

       Must be fresh each day!

  - Xanthine, 4.67 mg/100 mL
  - Allopurinol, 5.43 mg/100 mL
  - Nicotinamide, 18.09 mg/100 mL

    .. attention::

       Made up with doubly distilled water and with several drops of 40% NaOH
       to enhance solubility; refrigerate until used.

* Urine samples --- Unknown samples that contain the above components (plus uracil)

* Methanol, HPLC grade in LC solvent bottle
* Water, HPLC grade in LC solvent bottle
* 0.05 M acetic acid, buffered to pH 4.5; filtered (0.45 μm) into solvent bottle
* |ZnSO4| solution, 100 g/L
* 0.1 M NaOH

Procedures
----------

.. note::

   This below procedures have been written for an older model HPLC (Integral
   4000). They will need to be adapted for the new
   :doc:`/instruments/Agilent1260InfinityII/docs`.

Instrument Parameters
~~~~~~~~~~~~~~~~~~~~~

Mobile phase will be the acetic acid buffer at approximately 2000 psi (or
whatever yields 2.0 mL/min). This phase and all solvents must be degassed by
helium purge for 15 minutes prior to starting the pump. The absorption maxima
reported in the literature (:ref:`Senftleber et al. <hplc-ref>`) are uracil, 258 nm; uric acid, 292 nm; xanthine,
267 nm; allopurinol, 251 nm; and nicotinamide, 262 nm.  The literature also
reports that 254 nm is effective for detection.  Since the Integral 4000 has a
diode array, we can collect spectra for each peak.  The manual has more
information.  A method should be prepared to run the 5 standards and 2 samples.

Calibration
~~~~~~~~~~~

* Uracil is used as an internal standard because of its stability and its short
  retention time.
* Pipet 5.00-mL aliquots of the uracil stock solution into each of six 100-mL
  volumetric flasks.  Into one, pipet 1.00 mL of each of the other four stock
  solutions.  Similarly pipet 2.00, 3.00, 4.00, and 5.00 mL of each stock
  solution into four other flasks.  Ask the instructor to place an unknown into
  the sixth flask. Fill all flasks to the mark with doubly distilled water.
* Filter a few mL of each solution into an auto sampler vial and firmly attach
  the top. Place these into the tray being very careful not to touch the sampler
  arm (which easily knocks out of calibration costing needles and downtime).
  Run the method and collect the print outs.

Urine Sample
~~~~~~~~~~~~

Pipet 5.0 mL of urine into a centrifuge tube that contains 15 mL of doubly
distilled  water.  Precipitate the urinary proteins by addition of 1.5 mL
|ZnSO4| solution (100 g/L) and 0.8 mL of 0.1 M NaOH. Centrifuge (see Dr. M) for
10 minutes at 5000 rpm.  Filter the supernatant liquid through 0.2 μm Nalgene
membrane filter to remove any remaining particulate matter. Dilute 1 mL of the
filtrate to 10 mL and inject with no further pretreatment. Stop the run after 20
minutes of elution time.

After the run, purge the column with 1:1 methanol-water for 20 minutes followed
by 20 minutes of pure methanol.

Treatment of Data
-----------------

Determine the efficiency of the column by calculating the number of theoretical
plates (:math:`N`) using the retention time (|tr|) and the base peak width (|wB|):

.. math:: N  =  16 \left( \frac{t_r}{w_b} \right)^2
   :label: hplc-N

Typical results for a reverse phase column vary from 1500 to 2000 plates for a
flow rate of 2.0 mL/min.

Prepare standard additions working curves for allopurinol, nicotinamide, uric
acid, and xanthine (plot all on the same axes).  Determine the components in the
unknown and the concentration of each from these curves.  Similarly, identify
the individual compounds and their concentrations in the urine sample.

Questions
---------

1. Are any of the analytes (or other species in unknown) studied in this
   experiment amenable to separation on an ion-exchange column?  Explain.

2. Calculate the analytical sensitivities for each analyte compound.  For which
   species is the HPLC method used in this experiment most sensitive?

3. Calculate the efficiency of the column for each species as well as the height
   equivalent to a theoretical plate (see text, class notes, or :doc:`GC lab
   <GC>` for equations).

4. Explain the function of the mobile phase in GC vs. LC.  Be specific with
   details --- this is not a 1 or 2 point answer!

5. How could this experiment be performed to get better resolution between the
   peaks for uric acid and uracil?

References
----------

1. Bastian, D.W., Miller, R.L., Halline, A.G., Senftleber, F.C., and Veening, H.,J. Chem. Ed., 54, 766(1977).

.. _hplc-ref:

2. Senftleber, F.C., Halline, A.G., Veening, H., and Dayton, D.A., *Clin. Chem.*, **22**, 1522 (1976).

.. |C18| replace:: C\ :sub:`18`
.. |ZnSO4| replace:: ZnSO\ :sub:`4`
.. |tr| replace:: :math:`t_r`
.. |wb| replace:: :math:`w_b`
