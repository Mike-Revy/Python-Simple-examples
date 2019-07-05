from models import Challenge


def create_challenge(name, language, steps=1):
    Challenge.create(name=name,
                     language=language,
                     steps=steps)
    
def search_challenges(name_s, language_s):
    return Challenge.select().where(Challenge.name == name_s and Challenge.language == language_s)