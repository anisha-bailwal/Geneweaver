def find_pam_sites(sequence):
    sequence = sequence.upper()
    if not sequence:
        raise ValueError("DNA sequence cannot be empty")

    if set(sequence) - {"A", "T", "G", "C"}:
       raise ValueError("Invalid DNA sequence")
    pam_sites = []

    for i in range(len(sequence) - 2):
        if sequence[i + 1:i + 3] == "GG":
            pam_sites.append(i)

    return [
    (i, sequence[i:i + 3])
    for i in pam_sites
]

def generate_guide_rnas(sequence):
    sequence = sequence.upper()
    guide_rnas = []

    pam_sites = find_pam_sites(sequence)

    for position, pam in pam_sites:
        if position >= 20:
            guide = sequence[position - 20:position]

            guide_rnas.append({
               "guide": guide,
               "pam": pam,
               "position": position,
               "gc_content": calculate_guide_gc(guide)
  })
    return guide_rnas

def calculate_guide_gc(guide):
    guide = guide.upper()

    if not guide:
      raise ValueError("Guide RNA cannot be empty")

    if set(guide) - {"A", "T", "G", "C"}:
       raise ValueError("Invalid guide RNA")
    gc_count = guide.count("G") + guide.count("C")
    return (gc_count / len(guide)) * 100

def classify_guide(guide):
    gc_content = calculate_guide_gc(guide)

    if gc_content < 40:
        return "Low GC"

    elif gc_content <= 60:
        return "Optimal GC"

    else:
        return "High GC"

 