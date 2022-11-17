def main():
  W = int(input("Enter weight in kilograms:"))
  L = int(input("Enter length in cubic centimeters:"))
  H = int(input("Enter height in cubic centimeters:"))
  w = int(input("Enter width in cubic centimeters:"))

  if W > 0 and  W <= 27: print("")
  else: print("too heavy")

  if L * H * w > 0 and L * H * w <= 100000: print("")
  else: print("too large")

  if W > 27 and L * H * w > 100000: print("too heavy and large")
  
  pass


if __name__=="__main__":
  main()