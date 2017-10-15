from selenium import webdriver

#enter location to chrome driver here
driver = webdriver.Chrome("/home/suryatej/Documents/chromedriver")

#website addresses
driver.get("https://10fastfingers.com/typing-test/english")
driver.maximize_window()

# timer_element = driver.find_element_by_xpath('//*[@id="timer"]')
# timer = timer_element.get_attribute("innerHTML")

#find the text box to start typing
input_element = driver.find_element_by_xpath('//*[@id="inputfield"]')

#words are usually not over 350 
for i in range(1,350):
	try:

		#each word can be loaded using the following xpath in the source code
		current_word_element = driver.find_element_by_xpath('//*[@id="row1"]/span[' + str(i) +']' )


		current_word = current_word_element.get_attribute("innerHTML") 

		#type the word in the text box followed by a space
		input_element.send_keys(current_word + " ")
	except:
		break




