# multiBLAST
multiple sequence BLAST tool

## Python environment

Use Python 3.10 or newer and install `requirements.txt`. The Docker image
continues to use Python 3.10.

The dependency list covers the checked-in `pipeline/`, `util/`, and `legacy/`
scripts: Biopython, NumPy, pandas, requests, and Selenium. NumPy remains on
1.26.4 because legacy scripts import `numpy.lib.shape_base`. Dependencies from
unrelated ML, image-processing, and chatbot environments are not installed.

The pipeline scripts contain top-level batch execution with hard-coded data
paths. Do not import or run them as an installation check: a real batch can
submit NCBI requests and write result files. Validation of the dependency
update used the bundled XML fixture and synthetic FASTA/CSV data offline;
live NCBI jobs and browser automation still require their normal environment.
