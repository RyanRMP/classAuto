#!/bin/bash
gam="$HOME/bin/gam/gam"

touch alias.csv 
python classroomCreate.py | sed 's/ , /,/g' | sed '/Cannot/d' > classData.csv
while read f1 f2 f3
	do
		if [[ $f1 == *"Section"* ]]; then
			continue
		fi
		$gam create course alias "$f1" teacher "$f2" name "$f3" | sed 's/Created course //g' >> alias.csv
		sed -i '' -e "$ s/$/,$f1/" alias.csv
done < classData.csv
python studentAssess.py | sed 's/ , /,/g' > studentData.csv
$gam csv studentData.csv gam course ~Alias add student ~Student_email
rm alias.csv
rm classData.csv
rm studentData.csv
