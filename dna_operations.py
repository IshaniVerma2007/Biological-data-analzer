# dna_operations.py

def count_nucleotides(dna):
    count = {"A":0, "T":0, "G":0, "C":0}
    for base in dna:
        count[base] += 1

    print("\n🧪 Nucleotide Count:")
    for key in count:
        print(f"{key} ➜ {count[key]}")


def gc_content(dna):
    g = dna.count("G")
    c = dna.count("C")
    total = len(dna)

    gc = ((g + c) / total) * 100
    print(f"🧬 GC Content: {round(gc, 2)}%")

    if gc < 40:
        print("🔻 Low GC Content")
    elif gc <= 60:
        print("⚖️ Moderate GC Content")
    else:
        print("🚀 High GC Content")


def reverse_dna(dna):
    print("🔄 Reversed DNA:", dna[::-1])


def transcribe_dna(dna):
    rna = dna.replace("T", "U")
    print("🧾 RNA Sequence:", rna)
    return rna


def translate_rna(rna):
    codon_table = {
        "AUG": "Met", "UUU": "Phe", "UUC": "Phe",
        "UUA": "Leu", "UUG": "Leu",
        "UAA": "Stop", "UAG": "Stop", "UGA": "Stop"
    }

    protein = []

    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if len(codon) < 3:
            break

        amino = codon_table.get(codon, "X")

        if amino == "Stop":
            break

        protein.append(amino)

    print("🧬 Protein Sequence:", " ➜ ".join(protein))


def most_frequent_base(dna):
    count = {b: dna.count(b) for b in "ATGC"}
    print("🏆 Most Frequent Base:", max(count, key=count.get))


def least_frequent_base(dna):
    count = {b: dna.count(b) for b in "ATGC"}
    print("📉 Least Frequent Base:", min(count, key=count.get))


def mutate_dna(dna):
    try:
        index = int(input("🧪 Enter position to mutate: "))
    except:
        print("❌ Invalid position!")
        return dna

    if index < 0 or index >= len(dna):
        print("❌ Position out of range!")
        return dna

    new_base = input("🔤 Enter new base (A/T/G/C): ").upper()

    if new_base not in "ATGC":
        print("❌ Invalid base!")
        return dna

    dna = dna[:index] + new_base + dna[index+1:]
    print("🧬 Mutated DNA:", dna)
    return dna


def compare_sequences(dna1, dna2):
    matches = 0

    for i in range(min(len(dna1), len(dna2))):
        if dna1[i] == dna2[i]:
            matches += 1

    similarity = (matches / min(len(dna1), len(dna2))) * 100
    print(f"📊 Similarity: {round(similarity, 2)}%")
