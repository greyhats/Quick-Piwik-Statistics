import urllib.request
UserSelection = input("What would you like to see? \n Enter 1 to see statistics for returning visitors \n Enter 2 to see general info on all visitors: ")
MainUrl = "https://<url.com>/piwik/index.php"
APIKey = "<api_key>"
ReturningVisitors = ("?module=API&method=VisitFrequency.get&idSite=1&period=day&date=yesterday&format=xml&token_auth=" + APIKey)
VisitorInfo = ("?module=API&method=VisitsSummary.get&idSite=1&period=day&date=yesterday&format=xml&token_auth=" + APIKey)
TotalDuration = ("?module=API&method=VisitsSummary.getSumVisitsLengthPretty&idSite=1&period=day&date=yesterday&format=xml&token_auth=" + APIKey)
def UserChoice(request):
    page = urllib.request.urlopen(MainUrl + request)
    readables = page.read().decode("utf8")
    return(readables)
if UserSelection == "1":
    web = UserChoice(ReturningVisitors)
    print("The number of visits from returning IP's: "+(web[web.find("<nb_visits_returning>")+21:web.find("</nb_visits_returning>")]))
    print("Of these, how many were unique (i.e., the number of returning IP's, instead of visits)? "+(web[web.find("<nb_uniq_visitors_returning>")+28:web.find("</nb_uniq_visitors_returning>")]))
    print("The number of actions completed by returning visits: "+(web[web.find("<nb_actions_returning>")+22:web.find("</nb_actions_returning>")]))
    print("The maximum actions performed by a single returning visitor: "+(web[web.find("<max_actions_returning>")+23:web.find("</max_actions_returning>")]))
    print("How many of those returning bounced? "+(web[web.find("<bounce_count_returning>")+24:web.find("</bounce_count_returning>")]))
    print("The rate at which returning visits bounced: "+(web[web.find("<bounce_rate_returning>")+23:web.find("</bounce_rate_returning>")]))
if UserSelection == "2":
    web = UserChoice(VisitorInfo)
    duration = UserChoice(TotalDuration)
    print("The Visitor Info for yesterday: ")
    print("Number of total visits: "+(web[web.find("<nb_visits>")+11:web.find("</nb_visits>")]))
    print("Number of unique visitors: "+(web[web.find("<nb_uniq_visitors>")+18:web.find("</nb_uniq_visitors>")]))
    print("How many of those visitors bounced: "+(web[web.find("<bounce_count>")+14:web.find("</bounce_count>")]))
    print("Maximum actions performed by a single visitor: "+(web[web.find("<max_actions>")+13:web.find("</max_actions>")]))
    print("What percentage of visitors bounced? "+(web[web.find("<bounce_rate>")+13:web.find("</bounce_rate>")]))
    print("Total time spent on site: "+(duration[duration.find("<result>")+8:duration.find("</result>")]))