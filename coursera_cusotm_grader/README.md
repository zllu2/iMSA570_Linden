# Build low engagement assignments for release on Coursera MOOC ACCY576/577

# Major steps:

1. Create assignments with nbgrader, generate release(generate_assignment)
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

-----
# build docker image
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
$ conda activate p27 OR
$ source activate p27

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
