def apply(items): return sorted(items,key=lambda x:x.get('risk',0),reverse=True)
