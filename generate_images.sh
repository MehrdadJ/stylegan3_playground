#!/bin/sh

# Array of class names
classes=("0" "1" "2" "3" "4")  # Add more class names as needed

# Loop over each class
for class in "${classes[@]}"; do
    # Loop over a range of seed values
    for seed_start in $(seq 1 1 5000); do  # Adjust the range and step as needed
        seed_end=$((seed_start + 99))  # Adjust this to control the range of seeds per command
        outdir="gen_l24_256/train/$class"
        cmd="python gen_images.py --outdir=$outdir --trunc=1 --seeds=$seed_start-$seed_end --class=$class --network=l24-256-snapshot-000660.pkl"
        echo "Running: $cmd"
        eval "$cmd"
    done
done
