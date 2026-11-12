from compute_kpi import load_extracted

def compute_average_kpi(postings):
    if not postings:
        return 0.0

    total = sum(
        len({skill.strip().lower()
             for skill in p.get("required_skills", [])
             if skill.strip()})
        for p in postings
    )
    return round(total / len(postings), 2)

print("Average distinct skills per posting:",
      compute_average_kpi(load_extracted()))