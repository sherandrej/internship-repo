#!/bin/bash
#echo -n "What should be the fibonacci limit ? "
fib()
{
	i=0
	j=1
	if (( $1 <1 ))
		then
			echo "Incorrect input"
		exit 1
	elif [[ $1 == 1 ]]
		then 
			echo "Your fibonacci number is: $i"
		exit 0
	fi

	for (( c=0; c<$1; c++ )) ; do
	    (( n=i+j ))
	    (( i=j ))
	    (( j=n ))
	done
	echo "Your fibonacci number is: $i"
}
read -p 'input number: ' numb
fib numb
