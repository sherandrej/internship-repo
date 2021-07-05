#!/bin/bash
#echo -n "What should be the fibonacci limit ? "
fib()
{
	first=0
	second=1
	if (( $1 <1 ))
		then
			echo "Incorrect input"
		exit 1
	elif [[ $1 == 1 ]]
		then 
			echo "Your fibonacci number is: $first"
		exit 0
	fi

	for (( iter=0; iter<$1; iter++ )) ; do
	    (( number=first+second ))
	    (( first=second ))
	    (( second=number ))
	done
	echo "Your fibonacci number is: $first"
}
read -p 'input number: ' numb
fib numb
