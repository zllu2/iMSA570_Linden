# Build low engagement assignments for release on Coursera MOOC ACCY576/577

# Major steps:

1. Create assignments with nbgrader, generate release(nbgrader generate_assignment module1 --force)
2. Create programming assignment on Coursera, get graded_item_id from URL. ie. 5FK0X (/programming/5FK0X?versionId=..), partId and file name(ie. m1_assignment.ipynb)
3. Create notebook assignment, get launchid from URL, ie. w5fdK(.../notebook/w5fdK/launcher?)
4. Modify assignment notebook metadata, add coursera block including course_slug, graded_item_id and launch_item_id.
5. Create nbgrader_config.py
6. Create execute_grader.sh, update partID, generate_assignment to create gradebook.db, copy submitted assignment from coursera to nbgrader env.
7. Create exporter.py
8. Create Dockerfile, add nose, nbgrader on top of jupyter/scipy-notebook tag, create grader dir, copy source assignment
9. Generate docker image "sudo docker build -t accy576_grader .", folder need to have:
    - Dockerfile
    - execute_grader.sh
    - exporter.py
    - nbgrader_config.py
    - source(only keep low assignment in each module)
10. Run test.sh to test
    - Make sure shared/submissions/assignmenti_low.ipynb exists in current folder
11. Build and Upload docker tar file to coursera program assignment

# Refresh notebook on coursera
1. Upload new notebook from Instructor workspace
2. Open the file with Learner's view, rename file
3. In the url, add ?forceRefresh=true at the end and reload page
4. Delete renamed file

-----
# build docker image
# in iMSA570_Redesign/coursera_nbgrader_setup/build_grader/ run:
sudo docker build -t accy576_grader .
# list docker image
docker image list
#delete docker image
docker rmi dockerid
# build tar file
sudo docker save accy576_grader -o accy576_grader.tar

# test
# Set python 2.7 env
$ conda create -n p27 python=2.7
$ conda activate p27

# Install courseraprogramming
$ git clone https://github.com/coursera/courseraprogramming
# Need to run following to install in p27 every time
$ cd courseraprogramming/
$ python setup.py develop
$ pip install -r test_requirements.txt

# put /Users/lindenlu/uiuc/Spring_2019/iMSA570_Redesign/coursera_nbgrader_setup/shared/submission to docker file sharing

sudo ./test.sh






Grader output:
================================================================================
{"fractionalScore": 1.0, "feedback":"Congrats! All test cases passed!"}
================================================================================

Now upload assignments in the release directory to Coursera JupyterHub server

- Stop Server
- Logout
- Publish Workspace
- Publish  and return to course

Next, upload autograder and assign it to assignments

Install [courseraprogramming](https://github.com/coursera/courseraprogramming#grade)

sudo pip install courseraprogramming

-----

# custom grader doc(https://github.com/coursera/programming-assignments-demo/tree/master/custom-graders)
# Upload grader to coursera using courseraprogramming(https://github.com/coursera/courseraprogramming#upload)
1. Find out course id(id in returned json) with slug: https://api.coursera.org/api/onDemandCourses.v1?q=slug&slug=accounting-data-analytics-python
2. courseraprogramming upload $MY_CONTAINER_IMAGE $COURSE_ID $ITEM_ID $PART_ID --additional_item_and_part $ITEM_ID2 $PART_ID2 $ITEM_ID3 $PART_ID3

ACCY576:
course id: wBp37bIYEemRtxIG3uYysg
module 1 itemid: 5FK0X partid:tldMu
module 2 itemid: UGexs partid:sm6HU
module 3 itemid: YJqmG partid:0jC1R
module 4 itemid: LAhNW partid:uBbcH
module 5 itemid: LJxSb partid:hJtGd
module 6 itemid: EpcDF partid:cyaV2
module 7 itemid: Ju9jZ partid:Csvn3
module 8 itemid: T61Ru partid:Sll1A

# full command for 576
courseraprogramming upload accy576_grader wBp37bIYEemRtxIG3uYysg 5FK0X tldMu --additional_item_and_part UGexs sm6HU --additional_item_and_part YJqmG 0jC1R --additional_item_and_part LAhNW uBbcH --additional_item_and_part LJxSb hJtGd --additional_item_and_part EpcDF cyaV2 --additional_item_and_part Ju9jZ Csvn3 --additional_item_and_part T61Ru Sll1A

# Copy files to coursera
Run ./copy_files.sh to create zip files for lesson and assignments
Upload zip files to coursera through instructor Workspace
Open a new notebook and run following.
Remove existing folder first with !rm -r Assignments/Lessons if necessary.
```
import zipfile as zf
files = zf.ZipFile("Lessons.zip", 'r')
files.extractall('.')
files.close()

files = zf.ZipFile("Assignments.zip", 'r')
files.extractall('.')
files.close()
```
# if create readonly folder, delete coursera part in assignment notebook metadata.
