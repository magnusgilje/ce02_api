# import vlc # pip install python-vlc
import time

d1 = ['1st','a partridge in a pear tree.']
d2 = ['2nd', '2 turtle doves and ']
d3 = ['3rd', '3 french doves, ']
d4 = ['4th', '4 calling birds, ']
d5 = ['5th', '5 gold rings, ']
d6 = ['6th', '6 geese a laying, ']
d7 = ['7th', '7 swans a swimming, ']
d8 = ['8th', '8 maids a milking, ']
d9 = ['9th', '9 ladies dancing, ']
d10 = ['10th', '10 lords a leaping, ']
d11 = ['11th', '11 pipers piping, ']
d12 = ['12th', '12 drummers drumming, ']

twelvedays = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]
end_string = ''
for i in twelvedays:
    base_string = (f'On the {i[0]} day of christmas, my true love sent to me ')
    end_string = (f'{i[1]}{end_string}')
    updated_day = (f'{base_string}{end_string}')
    # p = vlc.MediaPlayer("twelvedays.mp3")
    # p.play()
    # time.sleep(180)
    # p.stop()
    print(updated_day)