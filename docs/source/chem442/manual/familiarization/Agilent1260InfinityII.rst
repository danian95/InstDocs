Agilent 1260 Infinity II HPLC
=============================

Procedure
---------

#. If the HPLC is not on (as indicated by the illuminated power lights on the
   instrument), turn on all three modules. The power buttons are at the bottom
   left of each module.

#.  Open the :program:`Control Panel` software. Click :guilabel:`HPLC 1` in the pane on
    the left followed by the :guilabel:`Launch` button in the window that opens to open
    the program:`Acquisition` software.

..
  #. In the top ribbon of :program:`Acquisition`, click "Method".
  
  #. Hover the cursor over the icons under "Acquisition Method" to find the "Open
     an Acquisition method" icon. Click the icon and Open
     :file:`CHEM341-Beverages-iso.amx`.
  
  #. Again, hover the cursor over the icons under "Acquisition Method" to find the
     "Send the current method to the instrument" icon. Click the icon to ensure
     the correct method is uploaded to the HPLC.

#. In the top ribbon of :program:`Acquisition`, click :guilabel:`Single Sample`.

#. Name your sample something fun and interesting --- this is just practice.
   Click the :guilabel:`...` icon next to :guilabel:`Acq. method` and find
   :file:`C:\\CDSProjects\\Agilent Project\\Methods\\CHEM341-Beverages-iso.amx` if the
   correct method is not loaded. Change the :guilabel:`Result path` to
   :file:`C:\\CDSProjects\\Agilent Project\\Results\\Practice`. Change the :guilabel:`Data file`
   to :samp:`<D> - <S> - <V>`
   by clicking on the arrow to the right of the field. This allows data files to
   be automatically named based on what you place in here.

#.  Open the autosampler door and inspect the samples available. If you
    took CHEM341 last semester, some of the vials may seem familiar! Pick
    your favorite and note its position --- you will need the following
    information:

    Tray number
        Either "1" or "2" printed on the white plastic of the
        autosampler.

    Vial number
        Note the column (A, B, C, D, E, or F) and row (1--11) of your vial as
        printed on the black sample tray.
       
    You may need to pull the sample holder out to get a better view. The trays
    easily slide out of the autosampler. If you encounter any resistance, *stop*
    and ask for help. Close the door.

#.  Under “Autosampler” on the computer, in the "Vial" field, type in your
    favorite vial using the format :samp:`p{<Tray Number>}-{<Vial Column>}{<Vial
    Row>}`. In other words, if I wanted to inject the vial in position Tray 1, C3, I would
    type :samp:`p1-c3`.

#.  Click :guilabel:`Run`.

#.  Take note of the signal graph at the bottom. You should begin to see data
    collected. The entire run will take 20 min.

#. **If you are the last group of the day**, click on :guilabel:`Status` in the
   :program:`Acquisition` ribbon. Find the :guilabel:`Shutdown Method` field and click the
   :guilabel:`...` button. Find and Open the :file:`Water to Methanol Rinse.amx`
   method. Click :guilabel:`Submit Shutdown`.

   .. note::

      Note that submitting a shutdown method does **not** end your current run.
      Instead, it adds on a new run immediately after the last run in the queue.
      This allows you to generate a long run queue of experiments followed by a
      method to safely shutdown the instrument. This is useful for when you want
      to run something overnight but don't want to stick around until it ends!

#. When your run is finished, click on :guilabel:`Status` in the
   :program:`Acquisition` ribbon. Under the Run Queue, click the
   :guilabel:`History` tab. Find the sample you submitted, right click the row,
   and select :guilabel:`Review Selected Run In Data Analysis`.

#. In the :program:`Data Analysis` program, select the :guilabel:`GC/LC area
   Percent` method configuration and then click :guilabel:`Link and Process`.
   Please be patient while the computer integrates all of your peaks.

#. Under the :guilabel:`Home` tab of the ribbon, click the :guilabel:`Results`
   button under :guilabel:`Layouts`. This will provide you with a summary of
   the peaks detected and their relative areas.

   .. note::

      This information could be written down and manually worked up. During the
      semester, we will attempt to prepare a processing method to automate the
      analysis.

#. If you are **not** the last group of the day, you are all set --- close all
   windows and move on to another station! If you **are** the last group of the
   day, did you submit the shutdown method? 

Questions
---------

1. What type of detector is this instrument using? Unsure? Take a look
   at the wavelengths being used and consider what region of the
   electromagnetic spectrum that falls under.
2. You should have noticed that your data was very noisy in the
   beginning, but after your first peak, it became a lot smoother. What
   happened to all of the noise in the beginning?
3. Our mobile phase is a combination of the solvents in positions "C" and "B".
   What is this mobile phase? Inspect the method to retrieve the actual ratio of
   solvents used.
4. Were your peaks clearly resolved? If not, what might you be able to
   do to increase the resolution?
