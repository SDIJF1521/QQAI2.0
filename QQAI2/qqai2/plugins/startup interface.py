from pyfiglet import Figlet

f = Figlet(font="slant")
png =  open('./qqai2/plugins/toy.txt','r')
print(str(png.readlines()).replace('\\\\n\\n','\n')[2:-2].replace("', '",''))
print("\n"+f.renderText("XBbot"))
print('author：YGXB')
