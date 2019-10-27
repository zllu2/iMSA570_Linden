#!/bin/bash

rm -r Lessons
mkdir Lessons
cd Lessons
for i in {1..8}
do
  mkdir Module"$i"
  cp -R ../../lessons/Module"$i"/notebooks/* Module"$i"
done

cd ..
rm -r Assignments
mkdir Assignments
cd Assignments
mkdir release
cd release

for i in {1..8}
do
  mkdir Module"$i"
  cp -R ../../../assignments/release/module"$i"/* Module"$i"
  rm Module"$i"/assignment_high.ipynb
done
