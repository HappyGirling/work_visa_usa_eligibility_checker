# Visa eligibility checker

print("Welcome to the visa eligibility checker supported by move2usajobs.com job portal.")

# Get country of citizenship

country = input("What is your country of citizenship? ")
non_treaty_visa_matches = []

# Treaty-visa Countries 
countries_e1_set = {"Argentina", "Australia", "Austria", "Belgium", "Bolivia", "Bosnia and Herzegovina", "Brunei", "Canada",
                    "Chile", "China (Taiwan)", "Colombia", "Costa Rica", "Croatia", "Denmark", "Estonia", "Ethiopia",
                    "Finland", "France", "Germany", "Greece", "Honduras", "Iran", "Ireland", "Israel", "Italy", "Japan",
                    "Jordan", "Kazakhstan", "Korea (South)", "Kosovo", "Kyrgyzstan", "Latvia", "Liberia", "Lithuania",
                    "Luxembourg", "Macedonia", "Mexico", "Moldova", "Mongolia", "Montenegro", "Morocco", "Netherlands",
                    "New Zealand", "Norway", "Oman", "Pakistan", "Panama", "Paraguay", "Philippines", "Poland", "Serbia",
                    "Singapore", "Slovak Republic", "Slovenia", "Spain", "Sri Lanka", "Suriname", "Sweden", "Switzerland",
                    "Thailand", "Togo", "Trinidad and Tobago", "Tunisia", "Turkey", "Ukraine", "United Kingdom",
                    "Yugoslavia"}
countries_e2_set = {
                    "Albania", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahrain", "Bangladesh",
                    "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Cameroon", "Canada", "Chile", "China (Taiwan)",
                    "Colombia", "Congo (Brazzaville)", "Congo (Kinshasa)", "Costa Rica", "Croatia", "Czech Republic",
                    "Denmark", "Ecuador", "Egypt", "Estonia", "Ethiopia", "Finland", "France", "Georgia", "Germany",
                    "Greece", "Grenada", "Honduras", "Iran", "Ireland", "Israel", "Italy", "Jamaica", "Japan",
                    "Jordan", "Kazakhstan", "South Korea", "Kosovo", "Kyrgyzstan", "Latvia", "Liberia", "Lithuania",
                    "Luxembourg", "Macedonia", "Mexico", "Moldova", "Mongolia", "Montenegro", "Morocco", "Nepal",
                    "Netherlands", "New Zealand", "Nicaragua", "Nigeria", "Norway", "Oman", "Pakistan", "Panama",
                    "Paraguay", "Philippines", "Poland", "Romania", "Serbia", "Senegal", "Singapore", "Slovak Republic",
                    "Slovenia", "Spain", "Sri Lanka", "Suriname", "Sweden", "Switzerland", "Thailand", "Togo",
                    "Trinidad and Tobago", "Tunisia", "Turkey", "Ukraine", "United Kingdom", "Yugoslavia"
}
countries_h2_set = {"Andorra", "Argentina", "Australia", "Austria", "Barbados", "Belgium", "Brazil", "Brunei", 
                   "Bulgaria", "Canada", "Chile", "Colombia", "Costa Rica", "Croatia", "Czech Republic", 
                   "Denmark", "Dominican Republic", "Ecuador", "El Salvador", "Estonia", "Fiji", "Finland", 
                   "France", "Germany", "Greece", "Grenada", "Guatemala", "Haiti", "Honduras", "Hungary", 
                   "Iceland", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Kiribati", "Latvia", 
                   "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", 
                   "Maldives", "Malta", "Marshall Islands", "Mauritius", "Mexico", "Micronesia", "Moldova", 
                   "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Nauru", "Nepal", "Netherlands", 
                   "New Zealand", "Nicaragua", "Norway", "Panama", "Papua New Guinea", "Paraguay", "Peru", 
                   "Philippines", "Poland", "Portugal", "Romania", "Saint Kitts and Nevis", "Saint Lucia", 
                   "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Serbia", "Seychelles", "Singapore", 
                   "Slovakia", "Slovenia", "Solomon Islands", "South Africa", "South Korea"}

# Get education level

education = input("Do you have a bachelor's degree? (yes/no) ")

# Get information to determine possible visa matches countries

need_training_not_available_in_country = input("Do you need to get a training that is not available in your country? (yes/no) ")
company_in_usa = input("Does the company you work for have an office in the USA? (yes/no) ")
recognized_extraordinary_ability = input("Do you have recognized extraordinary abilities? (yes/no) ")
athlete_or_entertainer_or_artist = input("Are you an athlete, entertainer, or artist? (yes/no) ")
religious = input("Are you a religious worker/student?(yes/no)")
cultural_worker = input("Are you a cultural worker? (yes/no) ")
age_under_35 = input("Is your age less than 35? (yes/no) ")
journalist_or_media_worker = input("Are you a journalist or a media worker? (yes/no) ")
executive_or_top_manager = input("Are you an executive or a top manager in your company? (yes/no) ")
have_100k_dollars = input("Do you have $100,000 or more? (yes/no) ")
exceptional_ability = input("Do you have exceptional ability in arts, science, or business? (yes/no) ")
treaty_e1 = input("Do you participate in an extentional trading activity with the USA? (yes/no)")
treaty_e5 = input("Do you have 1M$ or more (yes/no)")

# Determine possible visa matches for treaty countries

if religious == "yes":
        non_treaty_visa_matches.append("R-1")
        non_treaty_visa_matches.append("E-4")
if education == "no" and countries_h2_set:
        non_treaty_visa_matches.append("H2-A")
        non_treaty_visa_matches.append("H2-B")
if treaty_e1 == "yes" and countries_e1_set:
        non_treaty_visa_matches.append("E-1")
if treaty_e5 == "yes": 
        non_treaty_visa_matches.append("EB-5")
if countries_e2_set and have_100k_dollars == "yes":
        non_treaty_visa_matches.append("E-2")
if age_under_35 == "yes":
        non_treaty_visa_matches.append("J-1")
if recognized_extraordinary_ability == "yes":
        non_treaty_visa_matches.append("O-1")
if country == "Canada" or country == "Mexico" and education == "yes":
        non_treaty_visa_matches.append("TN")
if country == "Chile" or country == "Singapore" and education =="yes":
        non_treaty_visa_matches.append("H1-B1")
if athlete_or_entertainer_or_artist == "yes":
        non_treaty_visa_matches.append("P-1")
        non_treaty_visa_matches.append("P-3")
if cultural_worker == "yes":
        non_treaty_visa_matches.append("Q-1")
if education == "no" or "yes": 
        non_treaty_visa_matches.append("EB-3")
if education == "yes":
        non_treaty_visa_matches.append("H1-B")
        non_treaty_visa_matches.append("EB-2")
        if company_in_usa == "yes":
            non_treaty_visa_matches.append("L-1")
        if journalist_or_media_worker == "yes":
            non_treaty_visa_matches.append("I")
        if executive_or_top_manager == "yes":
            non_treaty_visa_matches.append("L-1")
        if recognized_extraordinary_ability == "yes":
            non_treaty_visa_matches.append("EB-1")
        if country == "Australia":
            non_treaty_visa_matches.append("E-3")
# Combine treaty visa matches

if len(non_treaty_visa_matches) > 0:
    print("You may be eligible for the following visa types:")
    for visa_type in non_treaty_visa_matches:
        print("-", visa_type)
else:
    print("Unfortunately, there are no visa types you are eligible for at this time.")

print("Thank you for using the visa eligibility checker.")