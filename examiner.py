def analyze_legislation(text):
    text = text.lower()
    analysis = []

    if "tax" in text:
        if "increase" in text or "rais" in text:
            analysis.append("This bill may reduce incentives to work and invest due to higher taxes.")
        elif "cut" in text or "decrease" in text:
            analysis.append("This bill may increase incentives to work and invest by lowering taxes.")

    if "subsidy" in text:
        analysis.append("Subsidies can distort market signals and misallocate resources.")

    if "regulation" in text:
        if "increase" in text or "add" in text:
            analysis.append("Increased regulation may raise costs for businesses and reduce innovation.")
        elif "reduce" in text or "eliminate" in text:
            analysis.append("Reduced regulation may enhance efficiency and promote growth.")

    if "spending" in text or "expenditure" in text:
        if "increase" in text:
            analysis.append("Increased government spending may require higher future taxes or borrowing.")
        elif "reduce" in text:
            analysis.append("Reducing spending could improve long-term fiscal health.")

    if not analysis:
        analysis.append("No major economic impact detected based on the given description.")

    return "\n".join(analysis)

if __name__ == "__main__": 
    print(analyze_legislation(input("Enter Legislation Proposal Summary:\n > ")))

