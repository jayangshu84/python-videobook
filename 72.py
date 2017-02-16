import webbrowser

query = raw_input("Enter your Google search query: ")
url = "https://www.google.co.uk/search?q=%s" % str(query)
webbrowser.open_new(url)
