class Monad:
  # pure :: a -> M a
  @staticmethod
  def pure(x):
    raise Exception("pure method needs to be implemented")
  
  # flat_map :: # M a -> (a -> M b) -> M b
  def flat_map(self, f):
    raise Exception("flat_map method needs to be implemented")

  # map :: # M a -> (a -> b) -> M b
  def map(self, f):
    return self.flat_map(lambda x: self.pure(f(x)))

class Option(Monad):
  # pure :: a -> Option a
  @staticmethod
  def pure(x):
    return Some(x)

  # flat_map :: # Option a -> (a -> Option b) -> Option b
  def flat_map(self, f):
    if self.defined:
      return f(self.value)
    else:
      return nil


class Some(Option):
  def __init__(self, value):
    self.value = value
    self.defined = True

class Nil(Option):
  def __init__(self):
    self.value = None
    self.defined = False

nil = Nil()