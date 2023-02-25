from googletrans import Translator
translator=Translator()
import nltk
from inscriptis import get_text
from nltk import word_tokenize, sent_tokenize

#nltk.download()

text = """A pumpkin is a vernacular term for mature winter squash of species and varieties in the genus Cucurbita that has
 culinary and cultural significance[1][2] but no agreed upon botanical or scientific meaning.[3] The term pumpkin is 
 sometimes used interchangeably with squash winter squash, and is commonly used for cultivars of Cucurbita argyrosperma, 
 Cucurbita ficifolia, Cucurbita maxima, Cucurbita moschata, and Cucurbita pepo.[1] Native to North America 
 (northeastern Mexico and the southern United States), C. pepo pumpkins are one of the oldest domesticated plants, 
 having been used as early as 7,000 to 5,500 BC. Today, pumpkins of varied species are widely grown for food, 
 as well as for aesthetic and recreational purposes.[4] The pumpkin's thick shell contains edible seeds and pulp. 
 Pumpkin pie, for instance, is a traditional part of Thanksgiving meals in Canada and the United States, and 
 pumpkins are frequently carved as jack-o-lanterns for decoration around Halloween, although commercially canned 
 pumpkin purée and pumpkin pie fillings are usually made of different pumpkin varieties from those used for 
 jack-o-lanterns. According to the Oxford English Dictionary, the English word pumpkin derives from the Ancient 
 Greek word πέπων (romanized pepōn), meaning 'melon'.[6][7] Under this theory, the term transitioned through the 
 Latin word peponem and the Middle French word pompon to the Early Modern English pompion, which was changed to 
 pumpkin by 17th-century English colonists, shortly after encountering pumpkins upon their arrival in what is now 
 the northeastern United States.[6] An alternate derivation for pumpkin is the Massachusett word pôhpukun, meaning 
 'grows forth round'.[8] This term would likely have been used by the Wampanoag people (who speak the Wôpanâak dialect 
 of Massachusett) when introducing pumpkins to English Pilgrims at Plymouth Colony, located in present-day 
 Massachusetts.[9] The English word squash is also derived from a Massachusett word, variously transcribed as 
 askꝏtasquash,[10] ashk8tasqash, or, in the closely-related Narragansett language, askútasquash.[11] Researchers 
 have noted that the term pumpkin and related terms like ayote and calabaza are applied to a range of winter squash 
 with varying size and shape.[1] The term tropical pumpkin is sometimes used for pumpkin cultivars of the species
   Cucurbita moschata"""
text = get_text(text)

print("############################################")

sentence_list = nltk.sent_tokenize(text)
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

#CALCULA LA FRASE QUE MAS SE REPITE
sentence_scores ={}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 20:
                if sent not in  sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

#REALIZA EL RESUMEN CON LAS MEJORES FRASES
import heapq
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
summary=translator.translate(summary, dest='es').text
print(summary)