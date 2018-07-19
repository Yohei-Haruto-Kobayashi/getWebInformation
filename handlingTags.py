'''
<tag>abc</tag> --> abc
      <tag>def</tag> --> def
no <tag>s --> ignore
'''
#verification
'''
line = "<th scope=\"col\" class=\"name title\">名称</th>"
line2 = "<th scope=\"row\"><a href=\"/lineup/docomo/iphone_se_32gb/\">iPhone SE（32GB）</th>"
line3 = "<td><span class=\"low\">113g</span></td>"
line4 = "<td>522時間（3G）<br />585時間（GSM）<br />435時間（LTE）</td>"
line5 = "@media(max-width: 375px) { .sg-responsive01 { width: 320px; height: 100px; } }"
line6 = "</div>"
line7 = "<div class=\"addthis_sharing_toolbox\"></div>"
line8 = ""
line9 = "<ins class=\"adsbygoogle sg-responsive01\""
line10 = "data-ad-slot=\"5258488018\"></ins>"
line11 = "data-ad-slot=\"5258488018\">"
'''

def removeTags(line):
    try:
        noFrontTag = False
        noBackTag = False
        count = 0

        # delete front tag
        top_char = line[0]
        if top_char != '<':
            noFrontTag = True

        while (top_char == '<') and (count < 20):
            stop = line.find('>')
            if (stop != -1):
                line = line[stop+1:]
            top_char = line[0]
            count += 1

        # delete back tag
        count = 0
        bottom_char = line[-1]
        if bottom_char != '>':
            noBackTag = True

        while (bottom_char == '>') and (count < 20):
            start = line.rfind('<')     # find '<' from the bottom
            if (start != -1):
                line = line[:start]
            bottom_char = line[-1]
            count += 1

        content = ""
        if (noFrontTag == False) and (noBackTag == False):
            content = line      # copy line string to content only when tags exist

        return content

    except IndexError as e:
        print(e)
        return ""

'''
print("--- line ---")
print(line)
print(removeTags(line))
print("")

print("--- line 2---")
print(line2)
print(removeTags(line2))
print("")

print("--- line 3---")
print(line3)
print(removeTags(line3))
print("")

print("--- line 4---")
print(line4)
print(removeTags(line4))
print("")

print("--- line 5---")
print(line5)
print(removeTags(line5))
print("")

print("--- line 6---")
print(line6)
print(removeTags(line6))
print("")

print("--- line 7---")
print(line7)
print(removeTags(line7))
print("")

print("--- line 8---")
print(line8)
print(removeTags(line8))
print("")

print("--- line 9---")
print(line9)
print(removeTags(line9))
print("")

print("--- line 10---")
print(line10)
print(removeTags(line10))
print("")

print("--- line 11---")
print(line11)
print(removeTags(line11))
print("")
'''
