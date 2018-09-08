files=`ls | grep gz`

for i in $files
        do
               tar xvfz $i 
        done

