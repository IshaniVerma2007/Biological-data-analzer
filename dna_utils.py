# dna_utils.py

def display_title():
    print("=" * 45)
    print("          🎯 PYTHON PROJECT")
    print("=" * 45)
    print("     👩‍💻 ISHANI VERMA 25BOE10013")
    print("=" * 45 + "\n")


def validate_dna(dna):
    for base in dna:
        if base not in "ATGC":
            return False
    return True


def menu():
    print("\n===== 📋 MENU =====")
    print("1️⃣ Count Nucleotides")
    print("2️⃣ GC Content")
    print("3️⃣ Reverse DNA")
    print("4️⃣ Transcribe DNA")
    print("5️⃣ Translate to Protein")
    print("6️⃣ Most Frequent Base")
    print("7️⃣ Least Frequent Base")
    print("8️⃣ Mutate DNA")
    print("9️⃣ Compare with Another Sequence")
    print("🔟 Enter New DNA")
    print("🚪 11. Exit")
