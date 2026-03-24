# main.py

from dna_utils import display_title, validate_dna, menu
from dna_operations import *

def main():
    display_title()

    dna = input("🧬 Enter DNA sequence: ").upper()

    if not validate_dna(dna):
        print("❌ Invalid DNA!")
        return

    while True:
        menu()

        try:
            choice = int(input("👉 Enter choice: "))
        except:
            print("❌ Invalid input!")
            continue

        if choice == 1:
            count_nucleotides(dna)
        elif choice == 2:
            gc_content(dna)
        elif choice == 3:
            reverse_dna(dna)
        elif choice == 4:
            transcribe_dna(dna)
        elif choice == 5:
            rna = transcribe_dna(dna)
            translate_rna(rna)
        elif choice == 6:
            most_frequent_base(dna)
        elif choice == 7:
            least_frequent_base(dna)
        elif choice == 8:
            dna = mutate_dna(dna)
        elif choice == 9:
            dna2 = input("🧬 Enter second DNA: ").upper()
            compare_sequences(dna, dna2)
        elif choice == 10:
            dna = input("🧬 Enter new DNA: ").upper()
        elif choice == 11:
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

main()
