import spacy

def download_spacy_models():
    models = [
        "nl_core_news_lg",
        "en_core_web_trf",
        "fr_dep_news_trf",
        "de_dep_news_trf",
        "it_core_news_lg",
        "xx_sent_ud_sm",
        "pt_core_news_lg",
        "es_dep_news_trf"
    ]
    for model in models:
        print(f"Downloading {model}...")
        spacy.cli.download(model)

if __name__ == "__main__":
    download_spacy_models()