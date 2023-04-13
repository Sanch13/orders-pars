positive_filter = ["[лЛ]амп.*", '[Сc]ветил.*', '[Сc]четч.*', '[эЭ]лектрот.*', '[тТ]рансформат.*',
                   '[пП]итан.*', "[Вв]ыключа.*", "[рР]озетк.*", "[кК]абел.*", "[уУ]длинител.*",
                   "[кК]орпус", "[эЭ]лектричес.*", "[кК]онтроллер.*", "[зЗ]акупк.*", "[мМ]уфт.*",
                   "[фФ]онар.*", "[фФ]ар[аы]", "[оО]свещен.*", "[эЭ]лектросчет.*",
                   '[Сc]ветильн.*', '[сС]ветодиод.*', '[пП]рибор.*', "[аА]втомати.*"]

negative_filter = ["[уУ]слуг.*", "[оО]бслуживан.*", "[оО]борудован.*", "ТЭН", "Ремонт",
                   "[зЗ]амен.*", "[вВ]ыбор", "[тТ]ермостат.*", "[дД]иагностирован.*",
                   "[шШ]иномонтаж", "[аА]удиоанализатор.*", "[иИ]змерени.*", "[пП]ечатн.*",
                   "[сС]ушилк.*", "[mM]aster", "[пП]ечног.*", "[аА]нтенн.*", "[кК]усторе.*",
                   "[кК]ондицион.*"]
pattern_positive = '|'.join(positive_filter)
pattern_negative = '|'.join(negative_filter)

url_goszakupki = "https://goszakupki.by/tenders/posted?TendersSearch[industry]=599%2C600%2C601%2C602%2C603%2C604%2C605%2C606%2C607%2C608%2C609%2C610%2C611%2C612%2C613%2C614%2C615&TendersSearch[type]=Marketing&TendersSearch[status]=Submission&sort=-price&sort=-request_end"
url_icetrade = "https://icetrade.by/search/auctions?zakup_type%5B1%5D=1&zakup_type%5B2%5D=1&establishment=0&industries=599.600-615&t%5BTrade%5D=1&t%5BsingleSource%5D=1&t%5BRequest%5D=1&t%5BOther%5D=1&r%5B1%5D=1&r%5B2%5D=2&r%5B7%5D=7&r%5B3%5D=3&r%5B4%5D=4&r%5B6%5D=6&r%5B5%5D=5&sort=date%3Adesc&sbm=1&onPage=100"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


