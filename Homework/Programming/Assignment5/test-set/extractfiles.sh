for dir in *; 
	do for file in $dir/*;
		do cat $file | sed -e 's/\([[:punct:]]\)//g' > ./`basename $file`$dir;
	done; 
done
