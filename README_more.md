ELRI National Relay Station (forked from the ELRC-SHARE SOFTWARE)
=================================================================

Branches
------------

- `master` branch: is the one used to do the different releases for the general ELRI NRS webapp docker images. 

- `DCU` branch: is the one used to do the differente releases for the Irish ELRI NRS webapp docker images, this branch includes the different code adaptations to include the language switch. 

- `VIC` branch: is the main development branch. It usually contains a development version of the code including the latest features implementation. 

- `ELDA` branch: is also a development branch that contains the code developed at ELDA's.

- `FCUL` branch: is a development branch that contains the code developed at FCUL. 


Update Branches
------------

After each milestone or feature complete development, the branches are updated as follows:

01. Pull request and merge from the development branch into `master`. Take into account that this step may need the creation of a temporal branch where we can do a safe merge.
02. Once the `master` is updated and functional, pull and merge into the other branches. Notice that the merge into `DCU` should be done carefully due to the differences from the integration of the language switch.


Create a Release
------------

This part is an easy one, gitHub allows for the creation of code releases with respect to a point of the repository (commit, branch status, etc.)
ELRI releases are made as follow using the gitHub web interface :
01.  Look for `releases` in the  ELRI repository code view
02.  Go to `Draft a new release`
03.  Select the branch from which you want to create the release. General releases are created from `master` branch, Irish releases are created from `DCU` branch.
This is important since the docker images are created using this releases checkpoints. 
04.  Add, if necessary, a commentary explaining the new features, fixes or important changes for the new release.
05.  `Publish release`


Create Docker images
------------
01. Check that the `docker/django/Dockerfile` points towards the release or branch you want to include in the image. If it is a general official image, it should point to the last release made from `master` branch. 
If it is an Irish official image, it should point to the last release made from `DCU`branch. 

02. Check that the docker-compose-runner.yml file contains the correct version of the images.

03. We recommend to first update all this files before drawing the release, to maintain the github as updated as possible. 

04. After updating all the files and generating the corresponding release, then create the docker webapp image from `docker/django` by:
```
$ docker build . --no-cache -t elrinrs/nationalrelaystation:NEWTAG 
```
05. Push the image to DockerHub if necessary by:
```
$ docker push elrinrs/nationalrelaystation:NEWTAG
```

Recall that you will need to be logged-in docker by a user with permission to do this push. 

Manage po files
------------
Each release should need an update of the .po files.
A general guide for managing the .po files can be found [here](https://github.com/ELDAELRA/ELRI/blob/master/internationalization.md). But, there are some extra tips:

- First of all, we recommend to make a backup of the actual status of the .po files by following the step 2 from the [internationalisation guide](https://github.com/ELDAELRA/ELRI/blob/master/internationalization.md) 
- You need to activate the python `virtualenv`  to create/update the .po files
- You can create the .po for only one language by using the option: `makemessages -l es_ES' 
- If there is any problem when generating the .po files, it is usually due to some import errors. Just comment the problematic line, regenerate the .po files and then de-comment the import line (i.e. this [line](https://github.com/ELDAELRA/ELRI/blob/b8081a19712e43bfdbc40415579729f801f48a49/metashare/repository/editor/resource_editor.py#L17))
- In order to generate correctly the .po files for the `ga_IE` language, in the [`accounts/forms.py`](metashare/accounts/forms.py) file, you should replace `_(mark_safe(` by `marksafe(_(` in order to let django recognize the strings to localise
- Editing .po files 
  - We recomend using the poedit to edit the .po files 
  - Just open the file, complete the translation and save it to create the new .mo file 
  - Be carefull with the `Fuzzy` translations: they will appear when there are several translations for the same source string or when the source string has changed a lot. 
  - Notice that at the end of the .po file there is a history of some previous translations, it is maybe easier to look at them using a regular text editor
  
- After generating the new localised content, you must copy the generated .mo and .po files to their original path inside the `metashare` directory tree

- Finally, maintain the backup copy of the .po files into the `ELRI/po_files` folder in this repository



