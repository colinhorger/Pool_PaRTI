from create_token_embeddings_esm_protbert import process_fasta_with_esm, parse_fasta
import os
import sys
import argparse
import glob
import torch
from Bio import SeqIO

#fasta = parse_fasta(r'C:\Users\cnhor\Documents\GitHub\Pool_PaRTI\test_opt_temp_sequences_pp.fasta')

#for num in fasta:
#    print(num)

process_fasta_with_esm(r'C:\Users\cnhor\Documents\GitHub\Pool_PaRTI\test_opt_temp_sequences_pp.fasta', r'C:\Users\cnhor\Documents\GitHub\Pool_PaRTI\token_embedding_generator')