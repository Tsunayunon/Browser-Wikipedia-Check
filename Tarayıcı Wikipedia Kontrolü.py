from selenium import webdriver

driverChrome = webdriver.Chrome()
driverEdge = webdriver.Edge()

driverChrome.get("https://tr.wikipedia.org/wiki/Python")
driverEdge.get("https://tr.wikipedia.org/wiki/Python")

if "BTK Akademi" in driverChrome.title:
    print("Chrome'da Wikipedia bulundu.")
else:
    print("Chrome'da wikipedia bulundu.")

if "BTK Akademi" in driverEdge.title:
    print("Edge'de wikipedia bulundu.")
else:
    print("Edge'de wikipedia bulunamadı.")

driverChrome.quit()
driverEdge.quit()