#!/bin/bash

# Path to the BLAST+ executables
blast_path="/path/to/blast/bin/"

# Input FASTA file containing the query sequences
query_file="/PowerBarcoder/data/result/202307012253_sk_four_loci/rbcLC_result/denoiseResult/r1/Abrodictyum_cumingii_ZXC002739_KTHU1461_.fas"

# Output file for storing the BLAST results
output_file="blast_results.xml"

# Database to search against (NR in this example)
database="nr"

# Run BLAST using the blastp program (change as per your requirement)
${blast_path}blastp -db $database -query $query_file -out $output_file -remote

# Print a message after the search is complete
echo "BLAST search completed successfully. Results are stored in $output_file."


#/usr/local/bin/blastn -db "nr" -query "/PowerBarcoder/data/result/202307012253_sk_four_loci/rbcLC_result/denoiseResult/r1/Abrodictyum_cumingii_ZXC002739_KTHU1461_.fas" -out "/PowerBarcoder/data/blast_results.xml" -remote -outfmt 5
