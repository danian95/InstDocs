Analysis of APC Tablets by UV Absorption and Fluorescence Spectrophotometry
===========================================================================

Theory
++++++

This experiment illustrates solvent extraction, a method for separating
substances that would otherwise interfere in an analysis.  The analyte has
three components (aspirin, caffeine, and phenacetin) and can not be analyzed
spectroscopically due to severe overlap of the absorption peaks.   In a solvent
extraction the sample is dissolved and shaken with a two-phase solvent system.
Solutes will partition between the two phases according to their relative
solubilities in the two solvents.  In favorable cases, an interferent will go
essentially completely into one phase while the solute of interest stays in the
other.  In this experiment aspirin (acetylsalicylic acid) can be extracted from
methylene chloride into aqueous bicarbonate buffer because at the pH of the
bicarbonate, aspirin is ionic and favors the more polar aqueous phase.  After
acidification, the aspirin is no longer ionic and ion can be extracted back
into chloroform.  The other two components, caffeine and phenacetin, are
unaffected by bicarbonate and will remain exclusively in the organic layer.
Considerable care must be exercised to perform an extraction properly!

UV-visible absorption spectrometry can be applied to the analysis of a mixture
of two components left in the original organic layer, caffeine and phenacetin.
These still have overlapping absorption spectra. The analysis is done by
measuring the absorbance at two wavelengths, λ\ :sub:`1` and  λ\ :sub:`2`. Since the
absorbances of the two components C and P are additive:

.. math::
   A_1 &= ε_{\text{C1}}bC_{\text{C}} + ε_{\text{P1}}bC_{\text{P}} \\
   A_2 &= ε_{\text{C2}}bC_{\text{C}} + ε_{\text{P2}}bC_{\text{P}}
   :label: apc-beer

where :math:`b` is the pathlength, and :math:`A_1` and :math:`A_2` are the
absorbances at λ\ :sub:`1` and  λ\ :sub:`2`, respectively. The molar
absorptivities :math:`ε_{\text{C1}}`, :math:`ε_{\text{P1}}`,
:math:`ε_{\text{C2}}`, and :math:`ε_{\text{P2}}`, are determined using standard
solutions. This yields two equations which can be solved for the two unknown
concentrations, :math:`C_{\text{C}}` and :math:`C_{\text{P}}`. Best results are
obtained when λ\ :sub:`1` and  λ\ :sub:`2` are chosen so that there is a large difference in
molar absorptivities at each wavelength and one compound absorbs more strongly
at λ\ :sub:`1` while the other absorbs more strongly at λ\ :sub:`2`.

.. sidebar::

   Some references to instruments here are very old.

The Varian Cary 5000 is a high resolution double beam UV-VIS-NIR
spectrophotometer. The Spectronic 20, used in previous courses, is a single
beam VIS instrument. The Cary has several features which make it a more
versatile and precise instrument.  A typical double beam instrument has two
sources, a D\ :sub:`2` lamp for measurements in the UV and a W lamp for the visible and
the near infrared.  This Cary has an added line source --- a mercury vapor lamp
for low level work in the UV.  It has a photomultiplier tube detector for
measuring low light levels.  Quartz optics permit measurements at wavelengths
in the UV down to 180 nm. Another feature of the high resolution instruments
are variable slits, making it possible to work at narrow bandwidths. The Cary
is a ratio-recording spectrophotometer. The electronics in the instrument
measure the intensities of the reference and sample beams. The ratio is then
displayed on the monitor.  Cost for this much technology --- list price is around
$60K.

The aspirin will be analyzed via fluorescence spectrophotometry.  In
fluorescence, the electronically excited state produced by absorption of a
photon rapidly returns to ground state. In some molecules this relaxation
process is accompanied by the emission of a photon. The resulting light is
called fluorescence. At low concentrations fluorescence intensity is
proportional to concentration and can be used for analysis. In this experiment
the aspirin is hydrolyzed in base using yielding the fluorescent salicylate
anion. The aspirin concentration is determined by comparing analyte
fluorescence to fluorescence intensity from a standard salicylate solution.
Aspirin fluorescence will be measured using the brand spanking new
:doc:`/instruments/PELS-55/docs` (ca $20K)

Experimental
++++++++++++

Apparatus
---------

* UV-Vis spectrophotometer (:doc:`/instruments/PELambda1050/docs`)
* Spectrofluorometer (:doc:`/instruments/PELS-55/docs`)
* Quartz UV-Vis and fluorescence cuvettes
* 100 mL separatory funnel
* Assorted volumetric flasks

Chemicals
---------

* Solid aspirin, caffeine, and phenacetin
* Methylene chloride
* 1% aqueous sodium carbonate solution (or ingredients)
* 0.5 M aqueous NaOH

Procedure
---------

Each Group
~~~~~~~~~~

1. Accurately weigh out about 0.1 g of the APC (aspirin, phenacetin, caffeine)
   powder into a 50 mL beaker.

2. Add 20 mL of methylene chloride, then transfer the mixture to a 100-mL
   separatory funnel, rinsing all undissolved particles into the funnel with
   more methylene chloride.

3. Extract the methylene chloride solution with two separate 10 mL portions of
   1% |Na2CO3| and with a 5 mL portion of deionized |H2O|. (Translation: add 10 mL
   of the carbonate solution to the separatory funnel and shake with occasional
   venting.  Allow it to separate and remove each layer (due to densities) into
   separate containers.  Return the organic layer to the funnel and add fresh
   carbonate.  Repeat operation for deionized water.) Combine all three aqueous
   extracts and wash with three 5 mL portions of fresh methylene chloride.
   (Consider: which is denser, methylene chloride or 1% carbonate!) Combine all
   the organic layers and label as concentrated UV sample.

4. After washing, pour the |Na2CO3| solution into a 50-mL volumetric flask and
   add 20 mL of 0.5 M NaOH, then dilute to the mark with deionized |H2O|. Shake
   well.  Label this as concentrated aspirin.  Perform a 1:250 dilution using
   1% |Na2CO3| as the diluent.  Shake well.  You will use this latter solution
   with the fluorometer.

5. Filter the methylene chloride solution from concentrated UV sample through
   paper previously wet with methylene chloride into a 50-mL volumetric flask.
   Dilute to the mark with methylene chloride, further dilute a 2 mL aliquot in
   a 100-mL volumetric.

Aspirin Group
~~~~~~~~~~~~~

* Prepare a standard solution of aspirin using 1% sodium carbonate as the
  solvent system.  From this, prepare a series of standards that are within the
  PE LS-55's  linear dynamic range (this can be a challenge!).  Use one to
  determine the excitation and emission wavelengths for aspirin printing out a
  combined spectra for your report.  Prepare a calibration curve and measure
  the fluorescence of each of the unknown solutions.  Plot the fluorescence
  calibration curve for aspirin and determine the amount of aspirin in the
  sample correcting for dilution.

Phenacetin/Caffeine Group
~~~~~~~~~~~~~~~~~~~~~~~~~

* Prepare stock solutions and dilute appropriately to determine the lambda max
  values for phenacetin and caffeine using the Varian Cary 5000
  Spectrophotometer.  Check with the instructor/consultant prior to going
  further.  Spectra of each species should be exported to Excel for the
  notebooks and reports.  It is also advisable to obtain the spectrum of
  aspirin (borrow some from the aspirin group) in case the extraction step was
  determined to be in error.

* Prepare 4-5 standards of each compound and measure their absorbances at both
  lambda max values  Also measure absorbances for all extracted methylene
  chloride solutions at both wavelengths.  Use the simultaneous dual Beer’s law
  expressions to calculate the amount of caffeine and phenacetin in the powder
  sample.  Don’t forget to correct for dilution!

Treatment of Data
-----------------

Calculate the percentages of aspirin, phenacetin, and caffeine.  Report the
results as a percentage of total mass.  (The total will probably be less than
100% since pharmaceutical preparations frequently contain starch or other inert
material as a binder.)  Include the class average and error analysis.

Questions
---------

1. Obtain structures of the three analytes and indicate why we can remove
   aspirin from the other two.  Can you suggest a method to separate phenacetin
   and caffeine in large quantities?

2. Looking at the structure of aspirin --- is it logical that it fluoresces?
   Explain.

3. A similar product containing caffeine, acetaminophen, and ibuprofen was
   introduced to market several years ago.   Would this same type of experiment
   work with a CAI tablet?  Why/Why not?

.. |Na2CO3| replace:: Na\ :sub:`2`\ CO\ :sub:`3`
.. |H2O| replace:: H\ :sub:`2`\ O

