url="http://naver.com"
my_str=url.replace("http://","")
print(my_str)
my_str=my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} {1}".format(url, password))