import requests
from bs4 import BeautifulSoup

while(True):
        print("A program that tells you the rankings of sports\n\n1.KBO\n2.MLB\n3.K-League\n4.Overseas Football\n5.KBL\n6.NBA")
        menu=int(input("Enter the sport you want!"))
        if(menu==1):
                html = requests.get("https://sports.news.naver.com/kbaseball/record/index?category=kbo")
                soup = BeautifulSoup(html.content, "html.parser")
                selected = soup.find_all(id="regularTeamRecordList_table")[0]
                rows = selected.find_all("tr")
                for item in rows :
                        # tr
                        print(item.find_all("th")[0].text.strip() + " Position : "  # rank
                        +item.find_all("div")[0].text.strip() # team name
                        +" ("
                        +"the number of matches : "+item.find_all("td")[1].text.strip()
                        +"\tWonn : "+item.find_all("td")[2].text.strip()
                        +"\tLoss : "+item.find_all("td")[3].text.strip()
                        +"\tDraw : "+item.find_all("td")[4].text.strip()
                        +"\tWinning % : "+item.find_all("td")[5].text.strip()
                        +"\tGames Behind : "+item.find_all("td")[6].text.strip()
                        +"\tContinuous : "+item.find_all("td")[7].text.strip()
                        +"\ton-base average : "+item.find_all("td")[8].text.strip()
                        +"\tslugging average : "+item.find_all("td")[9].text.strip()
                        +"\tthe last ten games : "+item.find_all("td")[10].text.strip()
                        +")\n")
                
                plrank=int(input("Do you want to check the individual ranking?(1/0)"))
                if(plrank==1):
                        print("\n\na pitcher's ranking\n\n")
                        print("a multiple-win ranking\n")
                        selected = soup.select('#content > div.tb_kbo > div > div.tbl_box.p_head > table.pitcher > tbody > tr > td:nth-child(1) > div')[0]

                        rows = selected.find_all("li")

                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                +item.find_all("strong")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\twin : "+item.find_all("em")[0].text.strip()
                                +")\n"
                                )

                        print("Earned Run Average ranking\n")
                        selected = soup.select('#content > div.tb_kbo > div > div.tbl_box.p_head > table.pitcher > tbody > tr > td:nth-child(2) > div')[0]

                        rows = selected.find_all("li")

                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                +item.find_all("strong")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tearned run : "+item.find_all("em")[0].text.strip()
                                +")\n"
                                )
                        
                        print("strikeout ranking\n")
                        selected = soup.select('#content > div.tb_kbo > div > div.tbl_box.p_head > table.pitcher > tbody > tr > td:nth-child(3) > div')[0]

                        rows = selected.find_all("li")

                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                +item.find_all("strong")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("em")[0].text.strip()
                                +")\n"
                                )
                        
                        print("save\n")
                        selected = soup.select('#content > div.tb_kbo > div > div.tbl_box.p_head > table.pitcher > tbody > tr > td:nth-child(4) > div')[0]

                        rows = selected.find_all("li")

                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                +item.find_all("strong")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("em")[0].text.strip()
                                +")\n"
                                )
                        
                        print("\n\na hitter's ranking\n\n")
                        print("batting average ranking\n")
                        selected = soup.select('#content > div.tb_kbo > div > div.tbl_box.p_head > table.hitter > tbody > tr > td:nth-child(1)')[0]

                        rows = selected.find_all("li")

                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                        +item.find_all("strong")[0].text.strip() # team name
                                        +" ("
                                        +"team : "+item.find_all("span")[1].text.strip()
                                        +"\tbatting average : "+item.find_all("em")[0].text.strip()
                                        +")\n"
                                )
                        
                        print("runs batted in ranking\n")
                        selected = soup.select('#content > div.tb_kbo > div > div.tbl_box.p_head > table.hitter > tbody > tr > td:nth-child(2)')[0]

                        rows = selected.find_all("li")

                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                        +item.find_all("strong")[0].text.strip() # team name
                                        +" ("
                                        +"team : "+item.find_all("span")[1].text.strip()
                                        +"\tnumber : "+item.find_all("em")[0].text.strip()
                                        +")\n"
                                )
                        
                        print("homerun ranking\n")
                        selected = soup.select('#content > div.tb_kbo > div > div.tbl_box.p_head > table.hitter > tbody > tr > td:nth-child(3)')[0]

                        rows = selected.find_all("li")

                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                        +item.find_all("strong")[0].text.strip() # team name
                                        +" ("
                                        +"team : "+item.find_all("span")[1].text.strip()
                                        +"\tnumber : "+item.find_all("em")[0].text.strip()
                                        +")\n"
                                )
                        
                        print("steal base ranking\n")
                        selected = soup.select('#content > div.tb_kbo > div > div.tbl_box.p_head > table.hitter > tbody > tr > td:nth-child(4)')[0]

                        rows = selected.find_all("li")

                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                        +item.find_all("strong")[0].text.strip() # team name
                                        +" ("
                                        +"team : "+item.find_all("span")[1].text.strip()
                                        +"\tnumber : "+item.find_all("em")[0].text.strip()
                                        +")\n"
                                )
        if(menu == 2):
                league=(int)(input("1.National League 2.American League"))
                if(league ==1):
                        html = requests.get("https://sports.news.naver.com/wbaseball/record/index?category=mlb&league=NL&year=2022")
                        soup = BeautifulSoup(html.content, "html.parser")
                        selected = soup.find_all(id="eastDivisionTeamRecordList_table")[0]
                        rows = selected.find_all("tr")
                        print("\neast division\n")
                        for item in rows :
                                # tr
                                print(item.find_all("td")[0].text.strip() + " : "  # rank
                                +item.find_all("div")[1].text.strip() # team name
                                +" ("
                                +"the number of matches : "+item.find_all("td")[2].text.strip()
                                +"\twin : "+item.find_all("td")[3].text.strip()
                                +"\tlose : "+item.find_all("td")[4].text.strip()
                                +"\twinning rate : "+item.find_all("td")[5].text.strip()
                                +"\tgames behind : "+item.find_all("td")[6].text.strip()
                                +"\tContinuous : "+item.find_all("td")[7].text.strip()
                                +"\tbatting average : "+item.find_all("td")[8].text.strip()
                                +"\tEarned Run Average : "+item.find_all("td")[9].text.strip()
                                +"\tthe last ten games : "+item.find_all("td")[10].text.strip()
                                +")\n")

                        selected = soup.find_all(id="centerDivisionTeamRecordList_table")[0]
                        rows = selected.find_all("tr")
                        print("\ncenter division\n")
                        for item in rows :
                                # tr
                                print(item.find_all("td")[0].text.strip() + " : "  # rank
                                +item.find_all("div")[1].text.strip() # team name
                                +" ("
                                +"the number of matches : "+item.find_all("td")[2].text.strip()
                                +"\twin : "+item.find_all("td")[3].text.strip()
                                +"\tlose : "+item.find_all("td")[4].text.strip()
                                +"\twinning rate : "+item.find_all("td")[5].text.strip()
                                +"\tgames behind : "+item.find_all("td")[6].text.strip()
                                +"\tContinuous : "+item.find_all("td")[7].text.strip()
                                +"\tbatting average : "+item.find_all("td")[8].text.strip()
                                +"\tEarned Run Average : "+item.find_all("td")[9].text.strip()
                                +"\tthe last ten games : "+item.find_all("td")[10].text.strip()
                                +")\n")

                        selected = soup.find_all(id="westDivisionTeamRecordList_table")[0]
                        rows = selected.find_all("tr")
                        print("\nwest division\n")
                        for item in rows :
                                # tr
                                print(item.find_all("td")[0].text.strip() + " : "  # rank
                                +item.find_all("div")[1].text.strip() # team name
                                +" ("
                                +"the number of matches : "+item.find_all("td")[2].text.strip()
                                +"\twin : "+item.find_all("td")[3].text.strip()
                                +"\tlose : "+item.find_all("td")[4].text.strip()
                                +"\twinning rate : "+item.find_all("td")[5].text.strip()
                                +"\tgames behind : "+item.find_all("td")[6].text.strip()
                                +"\tContinuous : "+item.find_all("td")[7].text.strip()
                                +"\tbatting average : "+item.find_all("td")[8].text.strip()
                                +"\tEarned Run Average : "+item.find_all("td")[9].text.strip()
                                +"\tthe last ten games : "+item.find_all("td")[10].text.strip()
                                +")\n")

                        selected = soup.find_all(id="wildCardTeamRecordList_table")[0]
                        rows = selected.find_all("tr")
                        print("\nwildCard\n")
                        for item in rows :
                                # tr
                                print(item.find_all("td")[0].text.strip() + " : "  # rank
                                +item.find_all("div")[1].text.strip() # team name
                                +" ("
                                +"the number of matches : "+item.find_all("td")[2].text.strip()
                                +"\twin : "+item.find_all("td")[3].text.strip()
                                +"\tlose : "+item.find_all("td")[4].text.strip()
                                +"\twinning rate : "+item.find_all("td")[5].text.strip()
                                +"\tgames behind : "+item.find_all("td")[6].text.strip()
                                +"\tContinuous : "+item.find_all("td")[7].text.strip()
                                +"\tbatting average : "+item.find_all("td")[8].text.strip()
                                +"\tEarned Run Average : "+item.find_all("td")[9].text.strip()
                                +"\tthe last ten games : "+item.find_all("td")[10].text.strip()
                                +")\n")
                        
                        plrank=int(input("Do you want to check the individual ranking?(1/0)"))
                        if(plrank==1):
                                print("\n\na pitcher's ranking\n\n")
                                selected = soup.select('#content > div.record_lead > ul:nth-child(1) > li:nth-child(1)')[0]
                                rows = selected.find_all("div")
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("a multiple-win ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\twin : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\twin : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\twin : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(1) > li:nth-child(2)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("Earned Run Average ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tEarned Run Average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tEarned Run Average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tEarned Run Average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(1) > li:nth-child(3)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("strikeout ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(1) > li:nth-child(4)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("Save ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )


                                print("a hitter's ranking\n")
                                selected = soup.select('#content > div.record_lead > ul:nth-child(2)')[0]
                                rows = selected.find_all("div")
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("batting average ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tbatting average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tbatting average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tbatting average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(2) > li:nth-child(2)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("runs batted in ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\truns batted in : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\truns batted in : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\truns batted in : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(2) > li:nth-child(3)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("homerun ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(2) > li:nth-child(4)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("a stolen base ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )
                else:        
                        html = requests.get("https://sports.news.naver.com/wbaseball/record/index?category=mlb&league=AL&year=2022")
                        soup = BeautifulSoup(html.content, "html.parser")
                        selected = soup.find_all(id="eastDivisionTeamRecordList_table")[0]
                        rows = selected.find_all("tr")
                        print("\neast division\n")
                        for item in rows :
                                # tr
                                print(item.find_all("td")[0].text.strip() + " : "  # rank
                                +item.find_all("div")[1].text.strip() # team name
                                +" ("
                                +"the number of matches : "+item.find_all("td")[2].text.strip()
                                +"\twin : "+item.find_all("td")[3].text.strip()
                                +"\tlose : "+item.find_all("td")[4].text.strip()
                                +"\twinning rate : "+item.find_all("td")[5].text.strip()
                                +"\tgames behind : "+item.find_all("td")[6].text.strip()
                                +"\tContinuous : "+item.find_all("td")[7].text.strip()
                                +"\tbatting average : "+item.find_all("td")[8].text.strip()
                                +"\tEarned Run Average : "+item.find_all("td")[9].text.strip()
                                +"\tthe last ten games : "+item.find_all("td")[10].text.strip()
                                +")\n")

                        selected = soup.find_all(id="centerDivisionTeamRecordList_table")[0]
                        rows = selected.find_all("tr")
                        print("\ncenter division\n")
                        for item in rows :
                                # tr
                                print(item.find_all("td")[0].text.strip() + " : "  # rank
                                +item.find_all("div")[1].text.strip() # team name
                                +" ("
                                +"the number of matches : "+item.find_all("td")[2].text.strip()
                                +"\twin : "+item.find_all("td")[3].text.strip()
                                +"\tlose : "+item.find_all("td")[4].text.strip()
                                +"\twinning rate : "+item.find_all("td")[5].text.strip()
                                +"\tgames behind : "+item.find_all("td")[6].text.strip()
                                +"\tContinuous : "+item.find_all("td")[7].text.strip()
                                +"\tbatting average : "+item.find_all("td")[8].text.strip()
                                +"\tEarned Run Average : "+item.find_all("td")[9].text.strip()
                                +"\tthe last ten games : "+item.find_all("td")[10].text.strip()
                                +")\n")

                        selected = soup.find_all(id="westDivisionTeamRecordList_table")[0]
                        rows = selected.find_all("tr")
                        print("\nwest division\n")
                        for item in rows :
                                # tr
                                print(item.find_all("td")[0].text.strip() + " : "  # rank
                                +item.find_all("div")[1].text.strip() # team name
                                +" ("
                                +"the number of matches : "+item.find_all("td")[2].text.strip()
                                +"\twin : "+item.find_all("td")[3].text.strip()
                                +"\tlose : "+item.find_all("td")[4].text.strip()
                                +"\twinning rate : "+item.find_all("td")[5].text.strip()
                                +"\tgames behind : "+item.find_all("td")[6].text.strip()
                                +"\tContinuous : "+item.find_all("td")[7].text.strip()
                                +"\tbatting average : "+item.find_all("td")[8].text.strip()
                                +"\tEarned Run Average : "+item.find_all("td")[9].text.strip()
                                +"\tthe last ten games : "+item.find_all("td")[10].text.strip()
                                +")\n")

                        selected = soup.find_all(id="wildCardTeamRecordList_table")[0]
                        rows = selected.find_all("tr")
                        print("\nwildCard\n")
                        for item in rows :
                                # tr
                                print(item.find_all("td")[0].text.strip() + " : "  # rank
                                +item.find_all("div")[1].text.strip() # team name
                                +" ("
                                +"the number of matches : "+item.find_all("td")[2].text.strip()
                                +"\twin : "+item.find_all("td")[3].text.strip()
                                +"\tlose : "+item.find_all("td")[4].text.strip()
                                +"\twinning rate : "+item.find_all("td")[5].text.strip()
                                +"\tgames behind : "+item.find_all("td")[6].text.strip()
                                +"\tContinuous : "+item.find_all("td")[7].text.strip()
                                +"\tbatting average : "+item.find_all("td")[8].text.strip()
                                +"\tEarned Run Average : "+item.find_all("td")[9].text.strip()
                                +"\tthe last ten games : "+item.find_all("td")[10].text.strip()
                                +")\n")
                
                        plrank=int(input("Do you want to check the individual ranking?(1/0)"))
                        if(plrank==1):
                                print("\n\na pitcher's ranking\n\n")
                                selected = soup.select('#content > div.record_lead > ul:nth-child(1) > li:nth-child(1)')[0]
                                rows = selected.find_all("div")
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("a multiple-win ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\twin : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\twin : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\twin : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(1) > li:nth-child(2)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("Earned Run Average ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tEarned Run Average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tEarned Run Average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tEarned Run Average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(1) > li:nth-child(3)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("strikeout ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(1) > li:nth-child(4)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("Save ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )


                                print("a hitter's ranking\n")
                                selected = soup.select('#content > div.record_lead > ul:nth-child(2)')[0]
                                rows = selected.find_all("div")
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("batting average ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tbatting average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tbatting average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tbatting average : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(2) > li:nth-child(2)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("runs batted in ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\truns batted in : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\truns batted in : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\truns batted in : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(2) > li:nth-child(3)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("homerun ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                selected = soup.select('#content > div.record_lead > ul:nth-child(2) > li:nth-child(4)')[0]
                                rows = selected.find_all("div")
                                i=0
                                rows.pop(0)
                                rows.pop(0)
                                rows.pop(0)
                                print("a stolen base ranking")
                                # tr
                                item=rows[0]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[3]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

                                item=rows[6]
                                print(item.find("b", "rank_num").text.strip() + " : "  # rank
                                +item.find_all("span")[0].text.strip() # team name
                                +" ("
                                +"team : "+item.find_all("span")[1].text.strip()
                                +"\tnumber : "+item.find_all("span")[2].text.strip()
                                +")\n"
                                )

        if(menu ==3):
                html = requests.get("https://sports.news.naver.com/kfootball/record/index")
                soup = BeautifulSoup(html.content, "html.parser")
                selected = soup.find_all(id="regularGroup_table")[0]
                rows = selected.find_all("tr")
                for item in rows :
                        # tr
                        print(item.find_all("th")[0].text.strip() + " Position : "  # rank
                        +item.find_all("div")[0].text.strip() # team name
                        +" ("
                        +"Played : "+item.find_all("td")[1].text.strip()
                        +"\tPoints : "+item.find_all("td")[2].text.strip()
                        +"\tWon : "+item.find_all("td")[3].text.strip()
                        +"\tDraw : "+item.find_all("td")[4].text.strip()
                        +"\tLoss : "+item.find_all("td")[5].text.strip()
                        +"\tGoal For : "+item.find_all("td")[6].text.strip()
                        +"\tGoal Against : "+item.find_all("td")[7].text.strip()
                        +"\tGoal Difference : "+item.find_all("td")[8].text.strip()
                        +"\tAssist : "+item.find_all("td")[9].text.strip()
                        +"\tFoul : "+item.find_all("td")[10].text.strip()
                        +")\n")
                
                plrank=int(input("Checking for Personal Rank?(1/0)"))
                if(plrank==1):
                        selected = soup.select('#content > div.rr_wrap > div > div.record_lead > ul > li:nth-child(1)')[0]
                        rows = selected.find_all("div")
                        i=0
                        rows.pop(0)
                        rows.pop(0)
                        rows.pop(0)
                        print("\n Highest scoring")
                        # tr
                        item=rows[0]
                        print(item.find("b", "rank_num").text.strip() + " Position : "  # rank
                        +item.find_all("span")[0].text.strip() # team name
                        +" ("
                        +"team : "+item.find_all("span")[1].text.strip()
                        +"\tnumber : "+item.find_all("span")[2].text.strip()
                        +")\n"
                        )

                        item=rows[3]
                        print(item.find("b", "rank_num").text.strip() + " Position : "  # rank
                        +item.find_all("span")[0].text.strip() # team name
                        +" ("
                        +"team : "+item.find_all("span")[1].text.strip()
                        +"\tnumber : "+item.find_all("span")[2].text.strip()
                        +")\n"
                        )

                        item=rows[6]
                        print(item.find("b", "rank_num").text.strip() + " Position : "  # rank
                        +item.find_all("span")[0].text.strip() # team name
                        +" ("
                        +"team : "+item.find_all("span")[1].text.strip()
                        +"\tnumber : "+item.find_all("span")[2].text.strip()
                        +")\n"
                        )                                

                        selected = soup.select('#content > div.rr_wrap > div > div.record_lead > ul > li:nth-child(3)')[0]
                        rows = selected.find_all("div")
                        i=0
                        rows.pop(0)
                        rows.pop(0)
                        rows.pop(0)
                        print("\n Game MVP")
                        # tr
                        item=rows[0]
                        print(item.find("b", "rank_num").text.strip() + " Position : "  # rank
                        +item.find_all("span")[0].text.strip() # team name
                        +" ("
                        +"team : "+item.find_all("span")[1].text.strip()
                        +"\tnumber : "+item.find_all("span")[2].text.strip()
                        +")\n"
                        )

                        item=rows[3]
                        print(item.find("b", "rank_num").text.strip() + " Position : "  # rank
                        +item.find_all("span")[0].text.strip() # team name
                        +" ("
                        +"team : "+item.find_all("span")[1].text.strip()
                        +"\tnumber : "+item.find_all("span")[2].text.strip()
                        +")\n"
                        )

                        item=rows[6]
                        print(item.find("b", "rank_num").text.strip() + " Position : "  # rank
                        +item.find_all("span")[0].text.strip() # team name
                        +" ("
                        +"team : "+item.find_all("span")[1].text.strip()
                        +"\tnumber : "+item.find_all("span")[2].text.strip()
                        +")\n"
                        )   
                        selected = soup.select('#content > div.rr_wrap > div > div.record_lead > ul > li:nth-child(2)')[0]
                        rows = selected.find_all("div")
                        i=0
                        rows.pop(0)
                        rows.pop(0)
                        rows.pop(0)
                        print("\n Highest Assist")
                        # tr
                        item=rows[0]
                        print(item.find("b", "rank_num").text.strip() + " Position : "  # rank
                        +item.find_all("span")[0].text.strip() # team name
                        +" ("
                        +"team : "+item.find_all("span")[1].text.strip()
                        +"\tnumber : "+item.find_all("span")[2].text.strip()
                        +")\n"
                        )

                        item=rows[3]
                        print(item.find("b", "rank_num").text.strip() + " Position : "  # rank
                        +item.find_all("span")[0].text.strip() # team name
                        +" ("
                        +"team : "+item.find_all("span")[1].text.strip()
                        +"\tnumber : "+item.find_all("span")[2].text.strip()
                        +")\n"
                        )

                        item=rows[6]
                        print(item.find("b", "rank_num").text.strip() + " Position : "  # rank
                        +item.find_all("span")[0].text.strip() # team name
                        +" ("
                        +"team : "+item.find_all("span")[1].text.strip()
                        +"\tnumber : "+item.find_all("span")[2].text.strip()
                        +")\n"
                        )   

        if(menu ==4):
                import requests
                from bs4 import BeautifulSoup
                html = requests.get("https://sports.news.naver.com/wfootball/index")
                soup = BeautifulSoup(html.content, "html.parser")

                league=(int)(input("1.Premier League 2.Bundesliga 3.LaLiga 4.Serie A\n"))
                if(league==1):
                        selected = soup.select('#_team_rank_epl > table > tbody')[0]
                        rows = selected.find_all("tr")
                        print("\nPremier League\n")
                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                +item.find_all("td")[0].text.strip() # team name
                                +" ("
                                +"Played : "+item.find_all("td")[1].text.strip()
                                +"\tWon : "+item.find_all("td")[2].text.strip()
                                +"\tDraw : "+item.find_all("td")[3].text.strip()
                                +"\tLoss : "+item.find_all("td")[4].text.strip()
                                +"\tPoints : "+item.find_all("td")[5].text.strip()
                                +")\n") 
                        plrank=int(input("Checking for Personal Rank?(1/0)"))
                        if(plrank==1):
                                selected = soup.select('#playerRankingList_wfootball_0 > tbody')[0]
                                rows = selected.find_all("tr")
                                print("\nScore Ranking\n")
                                for item in rows :
                                        # tr
                                        print(item.find_all("span")[0].text.strip() + " : "  # rank
                                        +item.find_all("td")[0].text.strip() # team name
                                        +" ("
                                        +"team : "+item.find_all("td")[1].text.strip()
                                        +"\tGoal For : "+item.find_all("td")[2].text.strip()
                                        +")\n") 
                
                if(league==2):
                        selected = soup.select('#_team_rank_bundesliga > table > tbody')[0]
                        rows = selected.find_all("tr")
                        print("\nBundesliga\n")
                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                +item.find_all("td")[0].text.strip() # team name
                                +" ("
                                +"Played : "+item.find_all("td")[1].text.strip()
                                +"\tWon : "+item.find_all("td")[2].text.strip()
                                +"\tDraw : "+item.find_all("td")[3].text.strip()
                                +"\tLoss : "+item.find_all("td")[4].text.strip()
                                +"\tPoints : "+item.find_all("td")[5].text.strip()
                                +")\n")
                        plrank=int(input("Checking for Personal Rank?(1/0)"))
                        if(plrank==1):
                                selected = soup.select('#playerRankingList_wfootball_2 > tbody')[0]
                                rows = selected.find_all("tr")
                                print("\nScore Ranking\n")
                                for item in rows :
                                        # tr
                                        print(item.find_all("span")[0].text.strip() + " : "  # rank
                                        +item.find_all("td")[0].text.strip() # team name
                                        +" ("
                                        +"team : "+item.find_all("td")[1].text.strip()
                                        +"\tGoal For : "+item.find_all("td")[2].text.strip()
                                        +")\n")                                 
                if(league==3):
                        selected = soup.select('#_team_rank_primera > table > tbody')[0]
                        rows = selected.find_all("tr")
                        print("\nLaLiga\n")
                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                +item.find_all("td")[0].text.strip() # team name
                                +" ("
                                +"Played : "+item.find_all("td")[1].text.strip()
                                +"\tWon : "+item.find_all("td")[2].text.strip()
                                +"\tDraw : "+item.find_all("td")[3].text.strip()
                                +"\tLoss : "+item.find_all("td")[4].text.strip()
                                +"\tPoints : "+item.find_all("td")[5].text.strip()
                                +")\n")
                        plrank=int(input("Checking for Personal Rank?(1/0)"))
                        if(plrank==1):
                                selected = soup.select('#playerRankingList_wfootball_1 > tbody')[0]
                                rows = selected.find_all("tr")
                                print("\nScore Ranking\n")
                                for item in rows :
                                        # tr
                                        print(item.find_all("span")[0].text.strip() + ": "  # rank
                                        +item.find_all("td")[0].text.strip() # team name
                                        +" ("
                                        +"team : "+item.find_all("td")[1].text.strip()
                                        +"\tGoal For : "+item.find_all("td")[2].text.strip()
                                        +")\n")                         
                if(league==4):
                        selected = soup.select('#_team_rank_seria > table > tbody')[0]
                        rows = selected.find_all("tr")
                        print("\nSerie A\n")
                        for item in rows :
                        # tr
                                print(item.find_all("span")[0].text.strip() + " : "  # rank
                                +item.find_all("td")[0].text.strip() # team name
                                +" ("
                                +"Played : "+item.find_all("td")[1].text.strip()
                                +"\tWon : "+item.find_all("td")[2].text.strip()
                                +"\tDraw : "+item.find_all("td")[3].text.strip()
                                +"\tLoss : "+item.find_all("td")[4].text.strip()
                                +"\tPoints : "+item.find_all("td")[5].text.strip()
                                +")\n") 
                        plrank=int(input("Checking for Personal Rank?(1/0)"))
                        if(plrank==1):
                                selected = soup.select('#playerRankingList_wfootball_3 > tbody')[0]
                                rows = selected.find_all("tr")
                                print("\nScore Ranking\n")
                                for item in rows :
                                        # tr
                                        print(item.find_all("span")[0].text.strip() + ": "  # rank
                                        +item.find_all("td")[0].text.strip() # team name
                                        +" ("
                                        +"team : "+item.find_all("td")[1].text.strip()
                                        +"\tGoal For : "+item.find_all("td")[2].text.strip()
                                        +")\n")
        if(menu==5):
                html = requests.get("https://sports.news.naver.com/basketball/record/index?category=kbl")
                soup = BeautifulSoup(html.content, "html.parser")

                selected = soup.select('#regularTeamRecordList_table')[0]
                rows = selected.find_all("tr")
                print("\nKBL\n")
                for item in rows :
                        # tr
                        print(item.find_all("strong")[0].text.strip() + " : "  # rank
                        +item.find_all("td")[0].text.strip() # team name
                        +" ("
                        +"Played : "+item.find_all("td")[1].text.strip()
                        +"\tWinning % : "+item.find_all("td")[2].text.strip()
                        +"\tWon : "+item.find_all("td")[3].text.strip()
                        +"\tLoss : "+item.find_all("td")[4].text.strip()
                        +"Game Behind : "+item.find_all("td")[5].text.strip()
                        +"\tPoints : "+item.find_all("td")[6].text.strip()
                        +"\tAS : "+item.find_all("td")[7].text.strip()
                        +"\tRebound : "+item.find_all("td")[8].text.strip()
                        +"\tSteal : "+item.find_all("td")[9].text.strip()
                        +"Block : "+item.find_all("td")[10].text.strip()
                        +"\t3 Point Goal : "+item.find_all("td")[11].text.strip()
                        +"\tFree Throw : "+item.find_all("td")[12].text.strip()
                        +"\tFree Throw % : "+item.find_all("td")[13].text.strip()
                        +")\n")
                plrank=int(input("Checking for Personal Rank?(1/0)"))
                if(plrank==1):
                        print("Player Position\n")
                        selected = soup.select('#playerRecordTable')[0]
                        rows = selected.find_all("tr")
                        for item in rows :
                                # tr
                                print(item.find_all("strong")[0].text.strip() + " Position : "  # rank
                                +item.find_all("td")[0].text.strip() # team name
                                +" ("
                                +"Played : "+item.find_all("td")[1].text.strip()
                                +"\tPoints : "+item.find_all("td")[2].text.strip()
                                +"\tAS : "+item.find_all("td")[3].text.strip()
                                +"\tRebound : "+item.find_all("td")[4].text.strip()
                                +"Steal : "+item.find_all("td")[5].text.strip()
                                +"\tBlock : "+item.find_all("td")[6].text.strip()
                                +"\t2 Point : "+item.find_all("td")[7].text.strip()
                                +"\t3 Point : "+item.find_all("td")[8].text.strip()
                                +"\tFree Throw : "+item.find_all("td")[9].text.strip()
                                +"\tField Made : "+item.find_all("td")[10].text.strip()
                                +"\t3 Point Made : "+item.find_all("td")[11].text.strip()
                                +"\tFree Throw Made : "+item.find_all("td")[12].text.strip()
                                +")\n")
        if(menu==6):
                html = requests.get("https://sports.news.naver.com/basketball/record/index?category=nba&year=2022&conference=EAST")
                soup = BeautifulSoup(html.content, "html.parser")

                selected = soup.select('#regularTeamRecordList_table')[0]
                rows = selected.find_all("tr")
                print("\nNBA\nEast Coast\n")
                for item in rows :
                        # tr
                        print(item.find_all("strong")[0].text.strip() + " Position : "  # rank
                        +item.find_all("td")[0].text.strip() # team name
                        +" ("
                        +"Played : "+item.find_all("td")[1].text.strip()
                        +"\tWinning % : "+item.find_all("td")[2].text.strip()
                        +"\tWon : "+item.find_all("td")[3].text.strip()
                        +"\tLoss : "+item.find_all("td")[4].text.strip()
                        +"Game Bebind : "+item.find_all("td")[5].text.strip()
                        +"\tPoints : "+item.find_all("td")[6].text.strip()
                        +"\tAS : "+item.find_all("td")[7].text.strip()
                        +"\tRebound : "+item.find_all("td")[8].text.strip()
                        +"\tSteal : "+item.find_all("td")[9].text.strip()
                        +"Block : "+item.find_all("td")[10].text.strip()
                        +"\t3 Point : "+item.find_all("td")[11].text.strip()
                        +"\tFree Throw : "+item.find_all("td")[12].text.strip()
                        +"\tFree Throw % : "+item.find_all("td")[13].text.strip()
                        +")\n")

                html = requests.get("https://sports.news.naver.com/basketball/record/index?category=nba&year=2022&conference=WEST")
                soup = BeautifulSoup(html.content, "html.parser")

                selected = soup.select('#regularTeamRecordList_table')[0]
                rows = selected.find_all("tr")
                print("\nNBA\nWest Coast\n")
                for item in rows :
                        # tr
                        print(item.find_all("strong")[0].text.strip() + " Postion : "  # rank
                        +item.find_all("td")[0].text.strip() # team name
                        +" ("
                        +"Played : "+item.find_all("td")[1].text.strip()
                        +"\tWinning % : "+item.find_all("td")[2].text.strip()
                        +"\tWon : "+item.find_all("td")[3].text.strip()
                        +"\tLoss : "+item.find_all("td")[4].text.strip()
                        +"Game Behind : "+item.find_all("td")[5].text.strip()
                        +"\tPoints : "+item.find_all("td")[6].text.strip()
                        +"\tAS : "+item.find_all("td")[7].text.strip()
                        +"\tRebound : "+item.find_all("td")[8].text.strip()
                        +"\tSteal : "+item.find_all("td")[9].text.strip()
                        +"Block : "+item.find_all("td")[10].text.strip()
                        +"\t3 Point : "+item.find_all("td")[11].text.strip()
                        +"\tFree Throw : "+item.find_all("td")[12].text.strip()
                        +"\tFree Throw % : "+item.find_all("td")[13].text.strip()
                        +")\n")     
                plrank=int(input("Checking for Personal Rank?(1/0)"))
                if(plrank==1):
                        print("Player Position\n")
                        selected = soup.select('#playerRecordTable')[0]
                        rows = selected.find_all("tr")
                        for item in rows :
                                # tr
                                print(item.find_all("strong")[0].text.strip() + " Position : "  # rank
                                +item.find_all("td")[0].text.strip() # team name
                                +" ("
                                +"Played : "+item.find_all("td")[1].text.strip()
                                +"\tPoints : "+item.find_all("td")[2].text.strip()
                                +"\tAS : "+item.find_all("td")[3].text.strip()
                                +"\tRebound : "+item.find_all("td")[4].text.strip()
                                +"Steal : "+item.find_all("td")[5].text.strip()
                                +"\tBlock : "+item.find_all("td")[6].text.strip()
                                +"\t2 Point : "+item.find_all("td")[7].text.strip()
                                +"\t3 Point : "+item.find_all("td")[8].text.strip()
                                +"\tFree Throw : "+item.find_all("td")[9].text.strip()
                                +"\tField Made : "+item.find_all("td")[10].text.strip()
                                +"\t3 Point Made : "+item.find_all("td")[11].text.strip()
                                +"\tFree Throw Made : "+item.find_all("td")[12].text.strip()
                                +")\n")                                                   

        regame=int(input("Starting Over?(1/0)"))
        if(regame==0) :
                break
        
