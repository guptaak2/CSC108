def can_swim (age, brought_parent):
  '''(int, bool) -> bool
  Returns whether the person is allowed to visit the pool given age
  or if they brought_parent or not.
  >>> can_swim (13, False)
  True
  >>> can_swim (12, True)
  True
  '''
  return age >= 13 or brought_parent == True
    

