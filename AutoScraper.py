#import libraries 
import csv 

from bs4 import BeautifulSoup 

#Algorithm 
    #(open our page 
    #grab all the information for the ads 
    #put all the ad data into an list 
    #create a csv file 
    #write each line into a csv file ) 

#make an empty arry/list for the data 
rows = []

#set foldername 
foldername = "facebook-joshcerutti/ads_information" # this folder is where our data is held. saved it to folder
#name so it can be easier if we want to do it with someone elses data 

#open messages 
with open ("%s/advertisers_you've_interacted_with.html" % foldername) as page: #The we open 
    #the HTML file and store its information in the page variable.
    # the "%s" in ("%s/advertisers_you've_interacted_with.html" % foldername) makes it insert whats stored
    # in the foldername varibale 
    
    soup = BeautifulSoup(page, "html.parser") # we pass page into the BeautifulSoup function, which parses 
    #the HTML into a list of elements that we can work with . The second argument "html.parser" tells Beautiful
    #Soup to process page as HTML

    contents = soup.find("div", class_="_a706") # Only grab content that is relevant to us on the page using 
    # the class named "contents". First we look for this class "_a706" that we know contains all the <div> tags
    # with ad information.  Then we'll assign the results to the contents variable.

    ad_list = contents.find_all("div", class_="_3-95 _a6-g") # isolate all the lists of ads 
    
    # {check if it is collecting date (print("\n")
    # print(ad_list)
    # print("\n")}
    ads_list = []
    times_list = []
    for item in ad_list: # goes through the list ad_list item by item storing the current
        #item in to the item variable. Then we run the process we specify inside the loop.
        #In this case the item holds a <div> tag for ads.

        #print(item.text)
        
        #advert = item.find("div", class_="_2ph_ _a6-p").get_text() # now we grab <div> tag with the class
        # _a6-p and get the text of those items and store into adver. These are the name of the Ads
        #print(item.text[10:])
        #print(item.text[:-22])
        ads_andTime = (item.text[10:])
        time = ads_andTime[-22:]
        ads_list.append(ads_andTime[:-22])
        times_list.append(time)
        #ads_list.append(ads_andTime[0:5:2])
        #print(ads_andTime)
        #print('\n')
        #print(ads_andTime[0])
        #timeaccessed = item.find("div", class_="_a6-o").get_text()# now we grab <div> tag with the class
        # _a6-o and get the text of those items and store into timeaccessed. This the time passed while
        # on those Ads.

        #print(advert)to check if its working 
        #print(timeaccessed) to check if its working
        #print(item) to check if its working 

        
        #row = {
            #"advert" : advert, #the keys "advert" & "timeaccessed" represent the type of data we are 
            #"timeaccessed" : timeaccessed #collecting. The equivalent of column headers in a spreadsheet.
            #each key is paired with its variable. "advert" key is paired with advert.
        #}    
        
        #rows.append(row) # This allows us to grab the latest values from each list item, and assign those 
        #values to the correct keys and append the keys and values to our rows variable.

print("\n")
ads_list.pop(1)
ads_list.pop(1)
#print(ads_list)
times_list.pop(1)
times_list.pop(1)
# print(ads_list)
#print('\n')
#print(times_list)
rows.append(ads_list)
rows.append(times_list)
print(rows)

#Time to write and create our csv file. We are going to write each row to it.
with open ("%s-all-advertisers.csv" % foldername, "w+") as csvfile : #This creates and opens the file. 
    #Then we open the csv file and refer to is as csvfile.
    
    fieldnames = ["advert", "timeaccessed"] # create this variable to store the list of strings. 
    #this corresponds to the keys we defined in the dictionary name row. This important because 
    #in the next step we use Dictwriter() function that needs parameter fieldnames to know what
    #the column headers of our .csv file will be and which part of our data rows it should access. 
    
    print(csv)

    writer = csv.Dictwrite(csvfile, fieldnames=fieldnames) #in other words, the field names that 
    #we list and store in our filednames variable represent the parts of the data we want 
    #DictWriter function to write into the .csv file.
    
    writer.writeheader() # Then we use the writerheader() function to write the first row 
    #of our .csv file, the headers of for each column. Since write knows those field names
    #from the previous line, we dont need to specify anything
    print(writer)
    #for row in rows:
        #writer.writerow(row)
