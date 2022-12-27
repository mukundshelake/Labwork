# Labwork
Everything that I have used/developed for the lab work.

# Quick description
* This module is a part of R&D activities at TIFR on High-Granularity Calorimeter (HGCAL) upgrade of the CMS experiment. 
* HGCAL baseplate QA/QC: The QA/QC studies are performed on the HGCAL baseplates as a part on ongoing R&D. This measurements are performed by an optical Coordinate Measuring Machine (CMM) and the output is stored in a folder (for one batch of baseplates), referred as 'main folder' henceforth. 
* This main folder is named ccording to specific naming scheme Baseplate_Manufacturer_Version_DateOfArrival_NoOfBaseplates, for example Baseplate_MPack_V7_221124_4. This folder (must) contain individual baseplate folders like Baseplate1, Baseplate2 etc. Note that, each baseplate folder must have name starting with 'Baseplate' followed by some unique ID to differentiate it from other baseplates of same batch. 
* Each baseplate folder must have 2 text files: 'Backside_results.txt' and 'Frontside-results.txt'.

# Steps 
1. Install stable branch
```
git clone https://github.com/mukundshelake/Labwork.git
```
2. Place the main folder inside /inputs.
3. Run the CMM_extraction tool by,
```
python CMM_extraction.py inputs/{Main folder} 
```
