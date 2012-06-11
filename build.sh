# file variables
python=true
java=false

inFile="RunCollatz.in"
outFile="RunCollatz.out"
compile=false
grep=false
noError=false

if $python; then
	echo PYTHON UNIT TESTS...
	python TestCollatz.py &> TestCollatz.py.out

	echo RUNNING PYTHON CODE...
	python Collatz.py < $inFile > $outFile
	
	echo CHECKING OUTPUT...
	diff -lc RunCollatz.out RunCollatz.in
fi

if $java; then
	if $compile; then
		echo COMPILING...
		javac *.java
		noError=([ $? == 0 ])
	fi

	if $noError; then		# don't exectute if there were compilation errors
		echo COMPILED successfully.
		echo EXECTUTING...
		java -ea strMatch $pattern $source $outFile
	fi

	if $grep; then
		echo GREP for string in $source...
		time grep -nm 1 'Can you find ThIs?' $source
	fi
fi
<< '--MULTICOMMENT--'

free 
comments!
--MULTICOMMENT--

echo GENERATING COMMIT LOG...
git log > Collatz.log

echo UPDATING SPHERECOLLATZ FILE...
cp Collatz.py SphereCollatz.py

echo RUNNING PYDOC...
pydoc -w ./Collatz.py

#echo ZIPPING FILE...

