def check(required,present): return {"missing":[x for x in required if x not in present]}
