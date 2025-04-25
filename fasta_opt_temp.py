from datasets import load_dataset

# Load the dataset
dataset = load_dataset("GleghornLab/optimal_temperature", split="train")

# Output FASTA file
fasta_filename = "train_opt_temp_sequences_pp.fasta"

# Write sequences to FASTA format with identifiers
with open(fasta_filename, "w") as fasta_file:
    for idx, seq in enumerate(dataset["seqs"]):
        fasta_file.write(f">seq{idx}\n{seq}\n")

print(f"FASTA file saved as '{fasta_filename}'")
