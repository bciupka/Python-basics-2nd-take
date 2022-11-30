# dictionary - lista tupli 2-składnikowych

# pop wyrzuca po kluczu, który definiujemy, popitem usuwa ostatni tuple
# dodatkowo w pop mozna zdefiniowac wartosc domyslna, jeżeli w słowniku jeszcze nie została zdefiniowana dla klucza (otrzymamy output),
# podobnie działa setdefaul, tyle że nie usuwa z listy tuple, które wywołamy. get zwróci None


channels = {"Google": 1480, "Email": 300, "Natural Traffic": 440, "TVSpot": 700}
print(channels["Email"])
print(channels.get("Email"))

channelsUpdate = {"Natural Traffic": 520, "News": 600}
channels.update(channelsUpdate)
print(channels)
print(channels.keys())
channels.pop("Email")
print(channels)
