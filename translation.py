from translate  import Translator

data = Translator(from_lang="French" ,to_lang="English")
res = data.translate('salut! c\'est ma premiere application de traduction ')
print(res)