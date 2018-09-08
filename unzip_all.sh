files=`ls | grep zip`

for i in $files
        do
               unzip $i 
        done

