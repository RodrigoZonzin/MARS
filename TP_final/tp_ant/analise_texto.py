

# Inicializa o analisador
analyzer = SentimentIntensityAnalyzer()

# Texto curto
texto = "Esse serviço é horrível, me deixou muito irritado!"

# Análise
sentimento = analyzer.polarity_scores(texto)

print(sentimento)