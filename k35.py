from stanfordkarel import *


class ktools:
   def m(self):
    """move"""
    move()

   def tl(self):
    """turn left"""
    turn_left()

   def tr(self):
    """turn right"""
    self.tl()
    self.tl()
    self.tl()

   def ta(self):
    """turn around"""
    self.tl()
    self.tl()

   def pick(self):
    """pick beeper"""
    pick_beeper()


   def put(self):
    """put beeper"""
    put_beeper()

   def put2(self):
    """put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

   def put5(self):
    """put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

   def h(self):
    """print it using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m3()
    self.tr()
    self.put5()
    self.ta()
    self.m2()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m2()
    self.tl()
    self.m4()

   def m3(self):
    """move three times"""
    self.m()
    self.m()
    self.m()

   def m2(self):
    """move two times"""
    self.m()
    self.m()

   def m4(self):
    """move four times"""
    self.m()
    self.m()
    self.m()
    self.m()
    

     
def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.h()
    kt.put2()
    kt.m()
    kt.put()
    kt.tl()
    kt.tl()
    kt.m2()
    kt.tr()
    kt.put5()
    kt.tr()
    kt.m()
    kt.put2()
    kt.tr()
    kt.m2()
    kt.put()
    kt.tr()
    kt.m()
    kt.put()
    kt.tl()
    kt.m2()
    kt.tl()
    kt.m3()
    kt.put2()
    kt.m()
    kt.put()
    kt.tl()
    kt.tl()
    kt.m2()
    kt.tr()
    kt.put5()
    kt.tr()
    kt.m2()
    kt.m2()
    kt.tr()
    kt.put5()
    kt.tl()
    kt.m()
    kt.put2()
    kt.m2()
    kt.tl()
    kt.put5()
    kt.tr()
    kt.m()
    kt.put2()
    kt.tr()
    kt.put5()
    kt.tr()
    kt.m()
    kt.put2()
    
    pass


if __name__ == "__main__":
    run_karel_program()