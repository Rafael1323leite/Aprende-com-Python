# minicas.py
def poly_div(n, d):
    """Returns (quotient, remainder) lists."""
    # Clean up trailing zeros from inputs
    while len(n) > 1 and n[-1] == 0: n.pop()
    while len(d) > 1 and d[-1] == 0: d.pop()
    
    if not d or (len(d) == 1 and d[0] == 0):
        return "Error", "Div by Zero"

    # Work with copies to avoid mutating original lists
    res_n = [float(x) for x in n]
    res_d = [float(x) for x in d]
    
    q = [0.0] * (len(res_n) - len(res_d) + 1)
    
    for i in range(len(q) - 1, -1, -1):
        # Divide highest degree terms
        q[i] = res_n[i + len(res_d) - 1] / res_d[-1]
        # Multiply and subtract
        for j in range(len(res_d)):
            res_n[i + j] -= q[i] * res_d[j]
            
    # Clean up remainder (strip zeros)
    remainder = res_n[:len(res_d)-1]
    return q, remainder

def poly_to_str(p):
    """Converts [ -30, 1, -10 ] to '-10x^2 + 1x - 30'"""
    if not p or all(c == 0 for c in p): return "0"
    terms = []
    for i in range(len(p)-1, -1, -1):
        c = round(p[i], 5) # Rounds to 5 decimals for screen space
        if c == 0: continue
        
        # Format the power
        if i == 0: pwr = ""
        elif i == 1: pwr = "x"
        else: pwr = "x^" + str(i)
        
        # Handle signs
        prefix = " + " if c > 0 and terms else ""
        if c < 0: prefix = " - " if terms else "-"
        
        val = str(abs(c)).replace(".0", "") if abs(c) != 1 or i == 0 else ""
        terms.append(prefix + val + pwr)
        
    return "".join(terms)