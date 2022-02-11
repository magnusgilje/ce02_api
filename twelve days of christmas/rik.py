'''The Twelve Days of Christmas'''
giftList = ["partridge in a pear tree","turtle doves","french hens","calling birds","gold rings","geese a laying","swans a swimming","maids a milking","ladies dancing","lords of leaping","pipers piping","drummers drumming"]
# Remember arrays are zero indexed and thus so is len([]).#
numberOfDays = len(giftList) + 1 # 12 days, 1 gift per day
def ordinalIndicator (i: int) -> str:
  '''  
  In English orthography, this corresponds to the suffixes -st, -nd, -rd, -th in written ordinals  
  ''' 
   # For values <= 0, just return "" as the concept of ordinal indicators doesn't apply.  # 
  if i <= 0:
    return ""  
  if i==1:
    return "st"  
  if i==2:
    return "nd"  
  if i==3:
    return "rd"  
  return "th"

def verse(day:int) -> str:
  '''  
  Return the given line of the verse corresponding to the specified `day`.  
  '''  
  if day <= 0:
    return "Doesn't look like it's Christmas."  
  if day > numberOfDays:
    return "Past Twelth Night, don't be greedy."  
  line: str = f"On the {day}{ordinalIndicator(day)} day of Christmas my true love sent to me"  
  # Looping through the list of gifts, in reverse order  #  
  for giftNumber in range(day-1,-1,-1):
    if giftNumber==0:
      if day==1:
        line += f" a {giftList[giftNumber]}."      
      else:
        line = line[:-1] # remove the last comma        line += f" and a {giftList[giftNumber]}."    else:
        line += f" {str(giftNumber+1)} {giftList[giftNumber]},"  
  return line
def main():
  for day in range(1,numberOfDays):
    print(verse(day))
if __name__ == "__main__":
  main()