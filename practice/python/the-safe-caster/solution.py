def safe_cast(value, type_name): 
  types = {
    "int" : int,
    "float" : float,
    "bool" : bool,
    }
  
  if type_name not in types:
    return None
  
  try:
    return types[type_name](value)
  except (ValueError, TypeError):
    return None
    
  
