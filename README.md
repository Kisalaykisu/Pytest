# Pytest

The pytest framework makes writing tiny tests simple, but it can also handle complex functional testing for apps and libraries.


## Step 1) Kindly create virtual environment.

## Step 2) Activate the virtual environment

## Step 3) kindly execute your test:
         a) pytest 
           (This will print your execution and generate the report of your test function)
          
         b) pytest -v 
            (To print the message in more clearer way)
         
         c) Testing can be started from the command line using the Python interpreter:
            python -m pytest [...]
            
         d) Obtaining assistance with version, option names, and environment variables
             pytest --version   # shows where pytest was imported from
             pytest --fixtures  # show available builtin function arguments
             pytest -h | --help # show help on command line and config file options
            
         e) To put an end to the testing after the first (N) failures, do the following:
             pytest -x           # stop after first failure
             pytest --maxfail=2  # stop after two failures  
             
          f) modifying traceback printing:
             
             pytest --showlocals # show local variables in tracebacks
             pytest -l           # show local variables (shortcut)

             pytest --tb=auto    # (default) 'long' tracebacks for the first and last
                     # entry, but 'short' style for the other entries
             pytest --tb=long    # exhaustive, informative traceback formatting
             pytest --tb=short   # shorter traceback format
             pytest --tb=line    # only one line per failure
             pytest --tb=native  # Python standard library formatting
             pytest --tb=no      # no traceback at all
             
          g) pytest allows one to drop into the PDB prompt immediately at the start of each test via a command line option:
             
             pytest --trace    # This will invoke the Python debugger at the start of every test.
