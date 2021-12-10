class Test:
  attr = 10
  attr2 = self.loadAttr()

  @staticmethod
  def loadAttr():
    return 'a'

print(Test.attr)
print(Test.attr2)