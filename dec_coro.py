def coroutine(func):
  """装饰器：向前执行到第一个`yield`表达式，预激`func`"""
  @wraps(func)
    def primer(*args,**kwargs): ➊
    gen = func(*args,**kwargs) ➋
    next(gen) ➌
    return gen ➍
  return primer
