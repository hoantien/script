In order to view the images taken from the RDI capture, you will need to use the split_image.py script and quick_phase utility. I have included the split_image script to this email. You can pull the quick_phase utility from bitbucket, located here:

https://bitbucket.org/lightco/quick_phase/src

Clone the repository, and then use the makefile to make the executable.

To split the images and apply the Bayer phase shift:

python split_image.py -f <filename> -g <capture group>

The filename is the path to the RDI file. The capture group is AB cameras, or BC cameras.

The split_image script will output ten different files, each named for the corresponding camera. To view them, you must apply the Bayer phase shift, which John wrote the quick_phase utility for. To apply the correct shift, invoke the quick phase utility as follows:

./quick_phase --fmt=5 -x  <filename>

where <filename> represents one of the ten results from split_image.py. You will need to run quick_phase for each of the 10 images.

Once you have applied both steps, you can use a raw image viewer to view the output files. We use ufraw (available on Macs through MacPorts), but you can use whatever tool you feel is appropriate.
