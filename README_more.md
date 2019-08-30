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