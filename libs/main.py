# IOStries v.0.1
# A library created to work abou articles and strings.
# Supported languages Turkish and English
from requests import get
from random import choice, shuffle
from bs4 import BeautifulSoup
from pandas import DataFrame as frame
class IOStr:
    def __init__(self):
        self.lib_properties = {
            "lib":"IOStries",
            "author":"merates",
            "version":"0.0.1",
            "source":"github/fswair"
        }


class IOArticles():
    def __init__(self, articles=[], types={"file_path":True, "plaintext":False}):
        if types["file_path"]:
            with open(articles[0], "r+", encoding="utf8") as file:
                artic = file.read()
            self.artics = artic
            self.length = IOStries("").get_length([x for x in artic])
            self.words = [word for word in artic.replace("\n", " ").split(" ") if word != " " and word != "" and " " not in word]
        else:
            self.length = IOStries("").get_length([x for x in articles])
            self.artics = articles
            self.words = [word for word in str(articles).replace("\n", " ").split(" ") if word != " " and word != "" and " " not in word]


class IOStries():
    def __init__(self, string):
        self.alphabets = {"hl":"all", "uppercase":"ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ", "lowercase":"abcçdefgğhıijklmnoöpqrsştuüvwxyz"}
        self.shuffle = [x for x in "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"]
        shuffle(self.shuffle)
        self.main_alphabet = "".join(self.shuffle)
        self.alphabet = self.replace(self.main_alphabet, ["q", "w", "Q", "W", "x", "X"]) + "üÜğĞşŞçÇİöÖ"

        self.string = string
        self.__lib__    = IOStr().lib_properties["lib"]
        self.__author__ = IOStr().lib_properties["author"]
        self.__version__ = IOStr().lib_properties["version"]
        self.__source__ = IOStr().lib_properties["source"]

        self.string_properties = s = {
            "types": {"n_lower":0, "n_upper":0, "is_upper": False, "is_lower":False, "is_alpha":False, "is_capitalized":False, "upper_and_lower":"" },
            "length":self.get_length(),
            "_":{"binary":self.get_binary(), "ascii": self.get_asc()}
        }

        self.get_type()

        self.types = s["types"]
        self.length = s["length"]
        self._ = s["_"]

        

        return None

    def contents(self):
        method_names = sorted([x for x in dir(IOStries) if not x.startswith("__") and not x == "contents"])
        method_class = ["IOStries" for x in range(len(method_names))]

        return frame({
            "class": method_class,
            "method": method_names
        })


    def get_char_types(self, counter=0) -> dict:
        vowels = "aeıAEIiİÜUOÖ"
        fvowel = self.get_length([x for x in self.string if x in vowels])
        fconsonant = (self.get_length([x for x in self.string if x in self.shuffle]) - fvowel)
        return {"vowels":fvowel, "consonant":fconsonant}
    
    def arr_length(self, e:str | list) -> int:
            x=0
            for x in e:
                self.x+=1
            return x
    def get_length(self, stack=[]) -> int:
        counter=0
        try:
            stack[0]
        except:
            stack = self.string
        for _ in stack:
            counter+=1
        return counter

    def get_type(self):
        for x in self.string:
            if x in self.alphabets["lowercase"]:
                self.string_properties["types"]["n_lower"] += 1
            elif x in self.alphabets["uppercase"]:
                self.string_properties["types"]["n_upper"] += 1
            is_lower = (self.string_properties["types"]["n_lower"] == self.get_length())
            is_upper = (self.string_properties["types"]["n_upper"] == self.get_length())
            is_capitalized = self.string[0] not in self.alphabets["lowercase"] and (((self.string_properties["types"]["n_lower"] +  self.string_properties["types"]["n_upper"]) == self.get_length()) and not is_upper and not is_lower and self.string_properties["types"]["n_upper"] == 1)
            self.string_properties["types"]["is_alpha"] = (self.string_properties["types"]["n_lower"] +  self.string_properties["types"]["n_upper"]) == self.get_length()
            self.string_properties["types"]["is_lower"] = is_lower
            self.string_properties["types"]["is_upper"] = is_upper 
            self.string_properties["types"]["is_capitalized"] = is_capitalized
            self.string_properties["types"]["upper_and_lower"] = not is_capitalized and not is_lower and not is_upper

        pass
    def get_asc(self) -> list[int]:
        return [ord(x) for x in self.string]
    def get_binary(self) -> str:
        return ''.join(format(ord(i), '08b') for i in self.string)
    def replace(self, stack:str, query:list) -> str:
        res = ""
        for q in stack:
            if q not in query:
                res+=q
        return res
    
    def is_global_latin(self) -> bool:
        return (self.get_length([x for x in self.string if x in self.main_alphabet]) == self.get_length())

    def is_includes_turkish(self) -> bool:
        return self.arr_length([x for x in self.string if x in "öüçşğÖÜÇŞĞİı"]) > 0



class IOAnySEO():
    def __init__(self, keyword, limit=0):
        self.fkeyword = keyword
        self.n = limit

    def contents(self):
        method_names = sorted([x for x in dir(IOAnySEO) if not x.startswith("__") and not x == "contents"])
        method_class = ["IOAnySEO" for x in range(len(method_names))]

        return frame({
            "class": method_class,
            "method": method_names
        })
    def get_pages(self, fkey="") -> list:
        fkey = fkey if not fkey == "" else self.fkeyword
        r = get(f"https://www.google.com/search?q={fkey.strip().replace(' ', '+')}", headers={"User-Agent":""})
        soup = BeautifulSoup(r.content, "html.parser")
        datas = [x[:x.find('ed=')] for x in [x.replace("/url?q=", "").replace("&sa=U&v", "") for x in [x["href"] for x in soup.select("a[href]")] if x.startswith("/url?q=")][:5]]
        if len(datas) > self.n and self.n > 0:
            return datas[0:self.n]
        return datas


class IOSEOMetrics():
    def __init__(self, url, fkeyword):
        self.iourl = url
        self.obj = IOAnySEO(fkeyword)
        self.fkeyword = fkeyword

    def contents(self):
        method_names = sorted([x for x in dir(IOSEOMetrics) if not x.startswith("__") and not x == "contents"])
        method_class = ["IOSEOMetrics" for x in range(len(method_names))]

        return frame({
            "class": method_class,
            "method": method_names
        })
    

    def is_mysite_lead(self,  found=[], return_all=False) -> list | bool:
        obj = self.obj
        sitename = self.iourl
        fkeyword = self.fkeyword
        p = sitename.replace("https://", "").replace("http://", "").replace("www.", "")
        url = p[:p.find("/")] if "/" in p else p
        results = obj.get_pages(fkeyword)
        results = [((index,True) if url in res else (index,False)) for index, res in enumerate(results) ]
        for index,res in (results):
            if res == True:
                found.append(index+1)
        if not return_all:
            try:
                return found[0] == 1
            except:
                return False
        else:
            if len(found) == 1:
                return found[0]
            else:
                return found
    def get_alexa_stats(self) -> dict:
        url = str(self.iourl).replace("https://", "").replace("http://", "").replace("www.", "")
        r = get(f"https://www.alexa.com/siteinfo/{url}",headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_7) AppleWebKit/5352 (KHTML, like Gecko) Chrome/36.0.843.0 Mobile Safari/5352"})
        soup = BeautifulSoup(r.content, "html.parser")

        top_keywords = soup.find_all("section", {"class":"table"})
        top_keywords = BeautifulSoup(str(top_keywords), "html.parser")
        top_keywords = top_keywords.find_all("div", {"class":"keyword"})
        top_keywords = BeautifulSoup(str(top_keywords), "html.parser")
        top_keywords = [x.text for x in top_keywords.find_all("span", {"class":"truncation"})]

        rank = soup.find("p", {"class":"big data"}).text.replace("\n", "").replace("\t","").replace(" ","")[1:]
        daily_time = soup.find("div",{"class":"rankmini-daily"}).text.split("\n\t\t\t\t\t\t\t")[1].replace("\n", "").replace("\t","").replace(" ","").replace(":",",")

        tr = BeautifulSoup(str(soup.find_all("a", {"class":"truncation"})), "html.parser")

        urls = ["https://www.alexa.com"+str(t)[str(t).find('href="')+6:str(t).find('">')] for t in tr.select("a")]

        return {"similar-sites":list(set([curl for curl in urls if curl.startswith("https://www.alexa.com/siteinfo") and url not in curl])) , "top-keywords":top_keywords[0:3], "rank":rank, "daily-time-in-website":daily_time}
    def get_rivals(self) -> list:
        rivals = self.get_alexa_stats()["similar-sites"]
        return rivals